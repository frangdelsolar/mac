from utils.authentication.response_not_authenticated import response_not_authenticated as not_auth
from utils.authentication.response_no_profile import response_no_profile as no_profile
from utils.authentication.response_no_client_and_not_app_admin import response_no_client_and_not_app_admin as no_client


def user_has_client(view_func):

    def _decorated(view, request, *args, **kwargs):
        not_auth_response = not_auth(request)
        if not_auth_response:
            return not_auth_response

        no_profile_response = no_profile(request)
        if no_profile_response:
            return no_profile_response

        no_client_response = no_client(request)
        if no_client_response:
            return no_client_response
        
        return view_func(view, request, *args, **kwargs)

    return _decorated 