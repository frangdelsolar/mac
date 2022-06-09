from client.models import Client
from users.models import Profile

def append_metadata_create_object(request, validated_data):
    user = None
    if request and hasattr(request, "user"):
        user = request.user
        profile = Profile.get_profile_by_user(user)
        validated_data['created_by'] = user
        validated_data['updated_by'] = user
        validated_data['client'] = profile.client

    return validated_data

def append_metadata_update_object(request, instance, validated_data):
    user = None
    if request and hasattr(request, "user"):
        user = request.user
        instance.updated_by = user
    for k,v in validated_data.items():
        setattr(instance, k, v)
        instance.save()
    return instance