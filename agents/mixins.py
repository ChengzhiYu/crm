from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect
class OrganizerAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is organizer."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            return redirect("leads:lead-list")
        return super().dispatch(request, *args, **kwargs)