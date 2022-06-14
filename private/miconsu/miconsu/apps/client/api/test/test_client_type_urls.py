from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from client.api.views import ClientTypeViewSet
from client.models import ClientType
from django.contrib.auth import get_user_model 


User = get_user_model()

class URLTest(APITestCase):
    fixtures = ['clients.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.get_request = self.factory.get("")
        self.post_request = self.factory.post("", {}, format="json")
        self.put_request = self.factory.put("", {}, format="json")
        self.delete_request = self.factory.delete("")

        self.list_view = ClientTypeViewSet.as_view({'get': 'list'})
        self.create_view = ClientTypeViewSet.as_view({'post': 'create'})
        self.detail_view = ClientTypeViewSet.as_view({'get': 'retrieve'})
        self.update_view = ClientTypeViewSet.as_view({'put': 'update'})
        self.delete_view = ClientTypeViewSet.as_view({'delete': 'destroy'})

        self.professional_user = User.objects.get(username="Professional")
        self.no_profile_user = User.objects.get(username='NoProfileUser')
        self.no_client_profile = User.objects.get(username='NoClientProfileUser')
        self.app_admin = User.objects.get(username='AppAdmin')

    def test_list__403__not_authenticated(self):
        """List View should return Forbidden if user is not authenticated"""
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 403)

    def test_list__500__no_profile(self):
        """List View should return status 500 if user has no profile"""
        force_authenticate(self.get_request, user=self.no_profile_user)
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 500)

    def test_list__200__authenticated(self):
        """List View should return status 200 if user is valid"""
        force_authenticate(self.get_request, user=self.professional_user)
        response = self.list_view(self.get_request)
        self.assertEqual(response.status_code, 200)

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
            'name': 'Nuevo Tipo de cliente',
        }
        post_request = self.factory.post("", data, format="json")
        force_authenticate(post_request, user=self.app_admin)
        response = self.create_view(post_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'id': 4, 'name': 'Nuevo Tipo de cliente'})


    def test_detail__403__not_authenticated(self):
        """Detail View should not be available for Anonymous user"""
        response = self.detail_view(self.get_request, ClientType.objects.last().id)
        self.assertEqual(response.status_code, 403)

    def test_detail__200__authenticated(self):
        """Detail View should return detail if user is auth"""
        force_authenticate(self.get_request, user=self.professional_user)
        response = self.detail_view(self.get_request, pk=2)
        self.assertEqual(response.status_code, 200)


    def test_upate__403__not_authenticated(self):
        """Update View should not be available for anonymous user"""
        response = self.update_view(self.put_request, pk=4)
        self.assertEqual(response.status_code, 403)

    def test_upate__403__not_app_administrator(self):
        """Update View should not be available for other than app admin"""
        force_authenticate(self.put_request, user=self.professional_user)
        response = self.update_view(self.put_request, pk=4)
        self.assertEqual(response.status_code, 403)

    def test_upate__200__app_administrator(self):
        """Update View should be available for app admin"""
        force_authenticate(self.put_request, user=self.app_admin)
        response = self.update_view(self.put_request, pk=2)
        self.assertEqual(response.status_code, 200)

    def test_update__object_is_updated(self):
        """Object is updated"""
        client_type_id = 2
        client_type = ClientType.objects.get(id=client_type_id)
        original_name = client_type.name
        data = {
            'name': 'Plan Modificado',
        }
        put_request = self.factory.put("", data, format="json")
        force_authenticate(put_request, user=self.app_admin)
        response = self.update_view(put_request, pk=client_type_id)
        self.assertNotEqual(original_name, response.data.get('name'))
        self.assertEqual(data['name'], response.data.get('name'))


    def test_delete__403__not_authenticated(self):
        """Delete View should not be available for anonymous user"""
        response = self.delete_view(self.delete_request, pk=2)
        self.assertEqual(response.status_code, 403)

    def test_delete__403__not_app_administrator(self):
        """Delete View should not be available for other than app admin"""
        force_authenticate(self.delete_request, user=self.professional_user)
        response = self.delete_view(self.delete_request, pk=2)
        self.assertEqual(response.status_code, 403)

    def test_delete__200__app_administrator(self):
        """Delete View should be available for app admin"""
        force_authenticate(self.delete_request, user=self.app_admin)
        response = self.delete_view(self.delete_request, pk=3)
        self.assertEqual(response.status_code, 200)

    def test_delete__object_is_deleted(self):
        """Object is deleted"""
        object_id = 3
        instance = ClientType.objects.get(id=object_id)

        force_authenticate(self.delete_request, user=self.app_admin)
        response = self.delete_view(self.delete_request, pk=object_id)

        filtered_objects = ClientType.objects.filter(id=object_id)
        self.assertEqual(filtered_objects.count(), 0)