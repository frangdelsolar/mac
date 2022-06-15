from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from client.api.views import ClientViewSet
from client.models import Client, ClientPlan, ClientType
from django.contrib.auth import get_user_model 
from users.enum import UserRoles
from users.models import Profile
from collections import OrderedDict


User = get_user_model()

class URLTest(APITestCase):
    fixtures = ['clients.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.get_request = self.factory.get("")
        self.post_request = self.factory.post("", {}, format="json")
        self.put_request = self.factory.put("", {}, format="json")
        self.delete_request = self.factory.delete("")

        self.list_view = ClientViewSet.as_view({'get': 'list'})
        self.create_view = ClientViewSet.as_view({'post': 'create'})
        self.detail_view = ClientViewSet.as_view({'get': 'retrieve'})
        self.update_view = ClientViewSet.as_view({'put': 'update'})
        self.delete_view = ClientViewSet.as_view({'delete': 'destroy'})

        self.professional_user = User.objects.get(username="Professional")
        self.no_profile_user = User.objects.get(username='NoProfileUser')
        self.no_client_profile = User.objects.get(username='NoClientProfileUser')
        self.app_admin = User.objects.get(username='AppAdmin')

    def test_list__403__null__not_authenticated(self):
        """List View should return Forbidden if user is not authenticated"""
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 403)

    def test_list__500__empty__no_profile_user(self):
        """List View should return status 500 if user has no profile"""
        force_authenticate(self.get_request, user=self.no_profile_user)
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, {'Error': 'El usuario no tiene un perfil configurado'})

    def test_list__200__all_clients__app_administrator(self):
        """List View should return all clients if user is app administrator"""
        force_authenticate(self.get_request, user=self.app_admin)
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

    def test_list__500__empty__profile_no_client(self):
        """List View should return status 500 if profile has no client"""
        force_authenticate(self.get_request, user=self.no_profile_user)
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, {'Error': 'El usuario no tiene un perfil configurado'})

    def test_list__200__self_client__not_app_administrator(self):
        """List View should return corresponding client if user is not administrator"""
        force_authenticate(self.get_request, user=self.professional_user)
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 200)
        profile = Profile.get_by_user(self.professional_user)
        self.assertEqual(response.data['results'][0]['id'], profile.client.id)

    def test_create__403__not_authenticated(self):
        """Create View should not be available for Anonymous user"""
        response = self.create_view(self.post_request, data={})
        self.assertEqual(response.status_code, 403)

    def test_create__403__not_app_administrator(self):
        """Create View should not be available for not AppAdministrator user"""
        force_authenticate(self.post_request, user=self.professional_user)
        response = self.create_view(self.post_request)
        self.assertEqual(response.status_code, 403)

    def test_create__200__app_administrator(self):
        """Create View should be available for AppAdministrator user"""
        data = {
            'name': 'Novo Cliente',
            'administrator_id': 1,
            'client_type_id': 2,
            'client_plan_id': 2
        }
        post_request = self.factory.post("", data, format="json")
        force_authenticate(post_request, user=self.app_admin)
        response = self.create_view(post_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id': 5, 'name': 'Novo Cliente', 'administrator': OrderedDict([('id', 1), ('username', 'admin'), ('first_name', 'Super'), ('last_name', 'Admin'), ('email', 'super@admin.com'), ('roles', [])]), 'client_plan': OrderedDict([('id', 2), ('name', 'Suscripción Mensual')]), 'client_type': OrderedDict([('id', 2), ('name', 'Professional')])})


    def test_detail__403__not_authenticated(self):
        """Detail View should not be available for Anonymous user"""
        response = self.detail_view(self.get_request, Client.objects.last().id)
        self.assertEqual(response.status_code, 403)

    def test_detail__200__user_self_client(self):
        """Detail View should return self client detail"""
        force_authenticate(self.get_request, user=self.professional_user)
        profile = Profile.get_by_user(self.professional_user)
        response = self.detail_view(self.get_request, pk=profile.client.id)
        self.assertEqual(response.status_code, 200)

    def test_detail__403__user_other_client(self):
        """Detail View should not be available for other client"""
        force_authenticate(self.get_request, user=self.professional_user)
        request = self.factory.get("")
        response = self.detail_view(request, pk=3)
        self.assertEqual(response.status_code, 403)

    def test_detail__200__app_administrator__any_client(self):
        """Detail View should return self client detail"""
        force_authenticate(self.get_request, user=self.app_admin)
        response = self.detail_view(self.get_request, pk=4)
        self.assertEqual(response.status_code, 200)
        response = self.detail_view(self.get_request, pk=3)
        self.assertEqual(response.status_code, 200)


    def test_update__403__not_authenticated(self): 
        """Update View should not be available for anonymous user"""
        response = self.update_view(self.put_request, pk=4)
        self.assertEqual(response.status_code, 403)

    def test_update__403__not_app_admin(self):
        """Update View should not be available for other than app admin"""
        force_authenticate(self.put_request, user=self.professional_user)
        response = self.update_view(self.put_request, pk=4)
        self.assertEqual(response.status_code, 403)

    def test_update__200__app_admin(self):
        """Update View should be available for app admin"""
        force_authenticate(self.put_request, user=self.app_admin)
        response = self.update_view(self.put_request, pk=4)
        self.assertEqual(response.status_code, 200)

    def test_update__object_is_updated(self):
        """Object is updated"""
        client_id = 4
        client = Client.objects.get(id=client_id)
        original_name = client.name
        original_administrator_id = client.administrator.id
        original_client_type_id = client.client_type.id
        original_client_plan_id = client.client_plan.id
        data = {
            'name': 'Cliente Modificado',
            'administrator_id': 5,
            'client_type_id': 3,
            'client_plan_id': 2
        }
        put_request = self.factory.put("", data, format="json")
        force_authenticate(put_request, user=self.app_admin)
        response = self.update_view(put_request, pk=client_id)
        self.assertNotEqual(original_name, response.data.get('name'))
        self.assertNotEqual(original_administrator_id, response.data.get('administrator_id'))
        self.assertNotEqual(original_client_type_id, response.data.get('client_type_id'))
        self.assertNotEqual(original_client_plan_id, response.data.get('client_plan_id'))
        self.assertEqual(data['name'], response.data.get('name'))
        self.assertEqual(data['administrator_id'], response.data.get('administrator')['id'])
        self.assertEqual(data['client_type_id'], response.data.get('client_type')['id'])
        self.assertEqual(data['client_plan_id'], response.data.get('client_plan')['id'])


    def test_delete__403__not_authenticated(self): 
        """Delete View should not be available for anonymous user"""
        response = self.delete_view(self.delete_request, pk=4)
        self.assertEqual(response.status_code, 403)

    def test_update__403__not_app_admin(self):
        """Delete View should not be available for other than app admin"""
        force_authenticate(self.delete_request, user=self.professional_user)
        response = self.delete_view(self.delete_request, pk=4)
        self.assertEqual(response.status_code, 403)

    def test_delete__200__app_admin(self):
        """Delete View should be available for app admin"""
        force_authenticate(self.delete_request, user=self.app_admin)
        response = self.delete_view(self.delete_request, pk=4)
        self.assertEqual(response.status_code, 200)

    def test_delete__object_is_deleted(self):
        """Object is deleted"""
        client_id =4
        instance = Client.objects.get(id=client_id)
        force_authenticate(self.delete_request, user=self.app_admin)
        response = self.delete_view(self.delete_request, pk=client_id)
        filtered_client = Client.objects.filter(id=client_id)
        self.assertEqual(filtered_client.count(), 0)