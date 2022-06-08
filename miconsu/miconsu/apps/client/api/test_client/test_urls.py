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

        self.list_view = ClientViewSet.as_view({'get': 'list'})
        self.create_view = ClientViewSet.as_view({'post': 'create'})
        self.detail_view = ClientViewSet.as_view({'get': 'retrieve'})

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
        self.assertEqual(len(response.data), 2)

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
        self.assertEqual(response.data[0]['id'], profile.client.id)

    def test_create__403__not_authenticated(self):
        """Create View should not be available for Anonymous user"""
        data = {
            'name': 'Novo Cliente',
            'administrator_id': 1,
            'client_type_id': 2,
            'client_plan_id': 2
            }
        post_request = self.factory.post("", data, format="json")
        response = self.create_view(post_request, data=data)
        self.assertEqual(response.status_code, 403)

    def test_create__403__not_app_administrator(self):
        """Create View should not be available for not AppAdministrator user"""
        data = {
            'name': 'Novo Cliente',
            'administrator_id': 1,
            'client_type_id': 2,
            'client_plan_id': 2
        }
        post_request = self.factory.post("", data, format="json")
        force_authenticate(post_request, user=self.professional_user)
        response = self.create_view(post_request)
        self.assertEqual(response.status_code, 403)

    def test_create__200__app_administrator(self):
        """Create View should not be available for not AppAdministrator user"""
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
        self.assertEqual(response.data, {'id': 5, 'name': 'Novo Cliente', 'administrator': OrderedDict([('id', 1), ('username', 'admin'), ('first_name', 'Super'), ('last_name', 'Admin'), ('email', 'super@admin.com')]), 'client_plan': OrderedDict([('id', 2), ('name', 'Suscripción Mensual')]), 'client_type': OrderedDict([('id', 2), ('name', 'Professional')])})

    
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

    # def test_detail_should_return_403_if_user_access_other_client(self):
    #     get_request = APIRequestFactory().get("")
    #     detail_view = ClientViewSet.as_view({'get': 'retrieve'})
    #     response = detail_view(get_request, self.client_one.id)
    #     self.assertEqual(response.status_code, 200)
    #     response = detail_view(get_request, self.client_two.id)
    #     self.assertEqual(response.status_code, 403)

    # def test_detail_should_return_202_if_user_super_administrator(self):
    #     get_request = APIRequestFactory().get("")
    #     detail_view = ClientViewSet.as_view({'get': 'retrieve'})
    #     response = detail_view(get_request, self.client_one.id)
    #     self.assertEqual(response.status_code, 200)
    #     response = detail_view(get_request, self.client_two.id)
    #     self.assertEqual(response.status_code, 200)

    
    # def test_update_should_return_202_if_user_access_self_client(self):
    #     pass

    # def test_update_should_return_403_if_user_access_other_client(self):
    #     pass

    # def test_update_should_return_202_if_user_super_administrator(self):
    #     pass
    
    
    # def test_partial_update_should_return_202_if_user_access_self_client(self):
    #     pass

    # def test_partial_update_should_return_403_if_user_access_other_client(self):
    #     pass

    # def test_partial_update_should_return_202_if_user_super_administrator(self):
    #     pass


    # def test_destroy_should_return_403_if_not_super_administrator(self):
    #     get_request = APIRequestFactory().get("")
    #     delete_view = ClientViewSet.as_view({'get': 'destroy'})
    #     response = delete_view(get_request, pk=self.client_one.id)
    #     self.assertEqual(response.status_code, 403)


    # def test_destroy_should_return_200_if_super_administrator(self):
    #     get_request = APIRequestFactory().get("")
    #     delete_view = ClientViewSet.as_view({'get': 'destroy'})
    #     response = delete_view(get_request, pk=self.client_one.id)
    #     print(response.data)
    #     self.assertEqual(response.status_code, 200)