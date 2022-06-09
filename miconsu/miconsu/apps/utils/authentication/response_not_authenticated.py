from rest_framework.response import Response

def response_not_authenticated(request):
    if not (request.user and request.user.is_authenticated):
        return Response(data={'Error': 'Debes iniciar sesión para visitar esta página.'}, status=403)
