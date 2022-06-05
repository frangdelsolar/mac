from rest_framework.serializers import (
    HyperlinkedModelSerializer, 
    SerializerMethodField
)
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import Profile

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        profile = Profile.get_by_user_id(self.user.id)
        # professional = Professional.get_professional_by_user(self.user)
        data['user'] = self.user.id
        data['client'] = profile.client.id if profile.client else -1
        # data['professional'] = professional.id if professional else -1
        data['roles'] = list(self.user.groups.all().values_list('name',flat = True))
        return data

class UserSerializer(HyperlinkedModelSerializer):
    # roles = SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email',
            # 'roles'
        ]

    # def get_roles(self, obj):
    #     groups = []
    #     for group in obj.groups.all():
    #         groups.append(group.name)
    #     return groups