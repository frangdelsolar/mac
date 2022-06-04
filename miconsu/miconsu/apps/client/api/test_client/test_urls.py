from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.reverse import reverse
from client.api.views import ClientViewSet
from client.models import Client, ClientPlan, ClientType
from django.contrib.auth import get_user_model 


User = get_user_model()

class URLTest(TestCase):
    def setUp(self):
        self.user_one = User.objects.create(
            username="pepito",
            first_name="Pepe",
            last_name="Honguito",
            email="pepe@honguito.com"
        )
        self.cp = ClientPlan.objects.create(name="Plan Nuevo")
        self.ct = ClientType.objects.create(name="Professional")
        self.client_one = Client.objects.create(
            name="Cliente 1",
            administrator=self.user_one,
            client_plan=self.cp,
            client_type=self.ct
        )

        self.client_two = Client.objects.create(
            name="Cliente 2",
            administrator=self.user_one,
            client_plan=self.cp,
            client_type=self.ct
        )

    def test_list__403__null__not_authenticated(self):
        """List View should return Forbidden if user is not authenticated"""
        api_request = APIRequestFactory().get("")
        list_view = ClientViewSet.as_view({'get': 'list'})
        response = list_view(api_request)
        self.assertEqual(response.status_code, 403)

    def test_list__200__all_clients__super_administrator(self):
        """List View should return all clients if user is super administrator"""
        api_request = APIRequestFactory().get("")
        list_view = ClientViewSet.as_view({'get': 'list'})
        response = list_view(api_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    # def test_list_should_return_self_client_if_user_not_super_administrator(self):
    #     api_request = APIRequestFactory().get("")
    #     detail_view = ClientViewSet.as_view({'get': 'list'})
    #     response = detail_view(api_request)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.data), Client.objects.all().count())

    
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