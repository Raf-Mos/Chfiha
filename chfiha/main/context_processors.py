# chfiha/main/context_processors.py

from .models import Profile

def profile_context(request):
    profile = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            profile = None
    return {'profile': profile}

