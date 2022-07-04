from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from professional.api.views import ProfessionalViewSet
from professional.models import Professional
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

        self.list_view = ProfessionalViewSet.as_view({'get': 'list'})
        self.create_view = ProfessionalViewSet.as_view({'post': 'create'})
        self.detail_view = ProfessionalViewSet.as_view({'get': 'retrieve'})
        self.update_view = ProfessionalViewSet.as_view({'put': 'update'})
        self.delete_view = ProfessionalViewSet.as_view({'delete': 'destroy'})

        self.no_profile_user = User.objects.get(username='NoProfileUser')
        self.no_client_profile = User.objects.get(username='NoClientProfileUser')
        self.app_admin = User.objects.get(username='AppAdmin')
        self.org_admin = User.objects.get(username='OrganizationAdmin')
        self.professional_user = User.objects.get(username="Professional")


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

    def test_list__500__empty__profile_no_client(self):
        """List View should return status 500 if profile has no client"""
        force_authenticate(self.get_request, user=self.no_profile_user)
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, {'Error': 'El usuario no tiene un cliente configurado'})

    def test_list__200__all_professionals__app_administrator(self):
        """List View should return all professionals if user is app administrator"""
        force_authenticate(self.get_request, user=self.app_admin)
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 6)

    def test_list__200__self_client_professionals__not_app_administrator(self):
        """List View should return corresponding client professionals if user is not administrator"""
        force_authenticate(self.get_request, user=self.professional_user)
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(response.data['results'][0]['id'], self.professional_user.id)


    def test_create__403__not_authenticated(self):
        """Create View should not be available for Anonymous user"""
        response = self.create_view(self.post_request, data={})
        self.assertEqual(response.status_code, 403)

    def test_create__200__app_administrator(self):
        """Create View should be available for AppAdministrator user"""
        data = {
            'profile': 'NuevoUsuario',
            'contact': 'Nuevo',
        }
        post_request = self.factory.post("", data, format="json")
        force_authenticate(post_request, user=self.app_admin)
        response = self.create_view(post_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id': 9, 'username': 'NuevoUsuario', 'first_name': 'Nuevo', 'last_name': 'Usuario', 'email': 'nuevo@usuario.com', 'roles': ['AppAdministrator']})

    def test_create__200__org_administrator(self):
        """Create View should be available for AppAdministrator user"""
        data = {
            'profile': 'NuevoUsuario',
            'contact': 'Nuevo',
        }
        post_request = self.factory.post("", data, format="json")
        force_authenticate(post_request, user=self.org_admin)
        response = self.create_view(post_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id': 9, 'username': 'NuevoUsuario', 'first_name': 'Nuevo', 'last_name': 'Usuario', 'email': 'nuevo@usuario.com', 'roles': ['AppAdministrator']})

    def test_create__403__not_org_administrator(self):
        """Create View should not be available for not AppAdministrator user"""
        force_authenticate(self.post_request, user=self.professional_user)
        response = self.create_view(self.post_request)
        self.assertEqual(response.status_code, 403)
    

    def test_detail__403__not_authenticated(self):
        """Detail View should not be available for Anonymous user"""
        response = self.detail_view(self.get_request, User.objects.last().id)
        self.assertEqual(response.status_code, 403)

    def test_detail__200__self_professional(self):
        """Detail View should return self user detail"""
        force_authenticate(self.get_request, user=self.professional_user)
        response = self.detail_view(self.get_request, pk=self.professional_user.id)
        self.assertEqual(response.status_code, 200)

    def test_detail__403__professional_other_client(self):
        """Detail View should not be available for other client"""
        force_authenticate(self.get_request, user=self.professional_user)
        request = self.factory.get("")
        response = self.detail_view(request, pk=self.app_admin.id)
        self.assertEqual(response.status_code, 403)

    def test_detail__200__app_administrator__any_user(self):
        """Detail View should return any user if app administrator"""
        force_authenticate(self.get_request, user=self.app_admin)
        response = self.detail_view(self.get_request, pk=self.app_admin.id)
        self.assertEqual(response.status_code, 200)
        response = self.detail_view(self.get_request, pk=self.professional_user.id)
        self.assertEqual(response.status_code, 200)


    def test_update__403__not_authenticated(self): 
        """Update View should not be available for anonymous user"""
        response = self.update_view(self.put_request, pk=4)
        self.assertEqual(response.status_code, 403)

    def test_update__200__self_user(self):
        """Update View should be available for self user"""
        force_authenticate(self.put_request, user=self.professional_user)
        response = self.update_view(self.put_request, pk=self.professional_user.id)
        self.assertEqual(response.status_code, 200)

    def test_update__403__other_user(self):
        """Update View should not be available for other user"""
        force_authenticate(self.put_request, user=self.professional_user)
        request = self.factory.get("")
        response = self.update_view(request, pk=self.app_admin.id)
        self.assertEqual(response.status_code, 403)

    def test_update__200__app_administrator__any_user(self):
        """Update View should return any user if app administrator"""
        force_authenticate(self.put_request, user=self.app_admin)
        response = self.update_view(self.put_request, pk=self.professional_user.id)
        self.assertEqual(response.status_code, 200)

    def test_update__object_is_updated(self):
        """Object is updated"""
        object_id = 7
        object_instance = User.objects.get(id=object_id)
        original_username = object_instance.username
        original_first_name = object_instance.first_name
        original_last_name = object_instance.last_name
        original_email = object_instance.email
        original_roles = object_instance.groups.all()
        data = {
            'username': 'UsuarioModificado',
            'first_name': 'Usuario',
            'last_name': 'Modificado',
            'email': 'usuario@modificado.com',
            'roles': ['AppAdministrator', 'OrganizationAdministrator']
        }
        put_request = self.factory.put("", data, format="json")
        force_authenticate(put_request, user=self.app_admin)
        response = self.update_view(put_request, pk=object_id)
        self.assertNotEqual(original_username, response.data.get('username'))
        self.assertNotEqual(original_first_name, response.data.get('first_name'))
        self.assertNotEqual(original_last_name, response.data.get('last_name'))
        self.assertNotEqual(original_email, response.data.get('email'))
        self.assertNotEqual(original_roles, response.data.get('roles'))
        self.assertEqual(data['username'], response.data.get('username'))
        self.assertEqual(data['first_name'], response.data.get('first_name'))
        self.assertEqual(data['last_name'], response.data.get('last_name'))
        self.assertEqual(data['email'], response.data.get('email'))
        self.assertEqual(data['roles'], response.data.get('roles'))


    def test_delete__403__not_authenticated(self): 
        """Delete View should not be available for anonymous user"""
        response = self.delete_view(self.delete_request, pk=7)
        self.assertEqual(response.status_code, 403)

    def test_delete__403__not_app_admin(self):
        """Delete View should not be available for other than app admin"""
        force_authenticate(self.delete_request, user=self.professional_user)
        response = self.delete_view(self.delete_request, pk=7)
        self.assertEqual(response.status_code, 403)

    def test_delete__200__app_admin(self):
        """Delete View should be available for app admin"""
        force_authenticate(self.delete_request, user=self.app_admin)
        response = self.delete_view(self.delete_request, pk=7)
        self.assertEqual(response.status_code, 200)

    def test_delete__object_is_deleted(self):
        """Object is deleted"""
        instance_id =4
        instance = User.objects.get(id=instance_id)
        force_authenticate(self.delete_request, user=self.app_admin)
        response = self.delete_view(self.delete_request, pk=instance_id)
        filtered = User.objects.filter(id=instance_id)
        self.assertEqual(filtered.count(), 0)