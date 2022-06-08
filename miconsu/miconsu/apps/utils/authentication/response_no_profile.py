from rest_framework.response import Response
from users.models import Profile

def response_no_profile(request):
    profile = Profile.get_by_user(request.user)
    if not profile:
        return Response(data={'Error': 'El usuario no tiene un perfil configurado'}, status=500)