from rest_framework.response import Response
from utils.authentication.get_profile_and_roles import get_profile_and_roles
from users.enum import UserRoles

def response_no_client_and_not_app_admin(request):
    profile, user_roles = get_profile_and_roles(request)

    if not profile.client and not UserRoles.APP_ADMINISTRATOR.value in user_roles:
        return Response(data={'Error': 'El perfil de usuario no tiene un cliente configurado'}, status=500)