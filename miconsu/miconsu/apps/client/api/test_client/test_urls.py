from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from client.api.views import ClientViewSet
from client.models import Client, ClientPlan, ClientType
from django.contrib.auth import get_user_model 
from users.enum import UserRoles
from users.models import Profile


User = get_user_model()

class URLTest(TestCase):
    fixtures = ['clients.json']

    def setUp(self):
        self.professional_user = User.objects.get(username="Professional")
        self.no_profile_user = User.objects.get(username='NoProfileUser')
        self.no_client_profile = User.objects.get(username='NoClientProfileUser')
        self.app_admin = User.objects.get(username='AppAdmin')

    def test_list__403__null__not_authenticated(self):
        """List View should return Forbidden if user is not authenticated"""
        api_request = APIRequestFactory().get("")
        list_view = ClientViewSet.as_view({'get': 'list'})
        response = list_view(api_request)
        self.assertEqual(response.status_code, 403)

    def test_list__500__empty__no_profile_user(self):
        """List View should return status 500 if user has no profile"""
        api_request = APIRequestFactory().get("")
        list_view = ClientViewSet.as_view({'get': 'list'})
        force_authenticate(api_request, user=self.no_profile_user)
        response = list_view(api_request)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, {'Error': 'El usuario no tiene un perfil configurado'})

    def test_list__200__all_clients__app_administrator(self):
        """List View should return all clients if user is app administrator"""
        api_request = APIRequestFactory().get("")
        list_view = ClientViewSet.as_view({'get': 'list'})
        force_authenticate(api_request, user=self.app_admin)
        response = list_view(api_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_list__200__self_client__not_app_administrator(self):
        """List View should return corresponding client if user is not administrator"""
        api_request = APIRequestFactory().get("")
        detail_view = ClientViewSet.as_view({'get': 'list'})
        force_authenticate(api_request, user=self.professional_user)
        response = detail_view(api_request)
        self.assertEqual(response.status_code, 200)
        profile = Profile.get_by_user(self.professional_user)
        self.assertEqual(response.data[0]['id'], profile.client.id)

    def test_list__500__empty__profile_no_client(self):
        """List View should return status 500 if profile has no client"""
        api_request = APIRequestFactory().get("")
        list_view = ClientViewSet.as_view({'get': 'list'})
        force_authenticate(api_request, user=self.no_profile_user)
        response = list_view(api_request)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.data, {'Error': 'El usuario no tiene un perfil configurado'})

    # def test_create_should_return_403_if_not_super_administrator(self):
    #     api_request = APIRequestFactory().get("")
    #     detail_view = ClientViewSet.as_view({'get': 'create'})
    #     data = {
    #         'name': 'Novo Cliente',
    #         'administrator': {
    #             'username': 'pepitohonguito'
    #         },
    #         'client_type': {
    #             'name': 'Otro Tipo'
    #         },
    #         'client_plan':{
    #             'name': "Plan Nuevo"
    #         }
    #     }
    #     response = detail_view(api_request, data=data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.data), Client.objects.all().count())

    
    # def test_detail_should_return_403_if_user_not_authenticated(self):
    #     api_request = APIRequestFactory().get("")
    #     detail_view = ClientViewSet.as_view({'get': 'retrieve'})
    #     response = detail_view(api_request, self.client_one.id)
    #     self.assertEqual(response.status_code, 403)

    # def test_detail_should_return_200_if_user_access_self_client(self):
    #     api_request = APIRequestFactory().get("")
    #     detail_view = ClientViewSet.as_view({'get': 'retrieve'})
    #     response = detail_view(api_request, self.client_one.id)
    #     self.assertEqual(response.status_code, 200)
    #     response = detail_view(api_request, self.client_two.id)
    #     self.assertEqual(response.status_code, 403)

    # def test_detail_should_return_403_if_user_access_other_client(self):
    #     api_request = APIRequestFactory().get("")
    #     detail_view = ClientViewSet.as_view({'get': 'retrieve'})
    #     response = detail_view(api_request, self.client_one.id)
    #     self.assertEqual(response.status_code, 200)
    #     response = detail_view(api_request, self.client_two.id)
    #     self.assertEqual(response.status_code, 403)

    # def test_detail_should_return_202_if_user_super_administrator(self):
    #     api_request = APIRequestFactory().get("")
    #     detail_view = ClientViewSet.as_view({'get': 'retrieve'})
    #     response = detail_view(api_request, self.client_one.id)
    #     self.assertEqual(response.status_code, 200)
    #     response = detail_view(api_request, self.client_two.id)
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
    #     api_request = APIRequestFactory().get("")
    #     delete_view = ClientViewSet.as_view({'get': 'destroy'})
    #     response = delete_view(api_request, pk=self.client_one.id)
    #     self.assertEqual(response.status_code, 403)


    # def test_destroy_should_return_200_if_super_administrator(self):
    #     api_request = APIRequestFactory().get("")
    #     delete_view = ClientViewSet.as_view({'get': 'destroy'})
    #     response = delete_view(api_request, pk=self.client_one.id)
    #     print(response.data)
    #     self.assertEqual(response.status_code, 200)