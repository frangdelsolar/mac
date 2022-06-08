from users.models import Profile


def get_profile_and_roles(request):
    profile = Profile.get_by_user(request.user)
    user_roles = profile.get_user_groups_list()
    return profile, user_roles
