from utils.authentication.response_not_authenticated import response_not_authenticated as not_auth
from utils.authentication.response_no_profile import response_no_profile as no_profile
from utils.authentication.response_no_client_and_not_app_admin import response_no_client_and_not_app_admin as no_client
from users.models import Profile


def response_auth_profile_client_valid(request):
    not_auth_response = not_auth(request)
    if not_auth_response:
        return not_auth_response

    no_profile_response = no_profile(request)
    if no_profile_response:
        return no_profile_response

    no_client_response = no_client(request)
    if no_client_response:
        return no_client_response

