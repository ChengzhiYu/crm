from django.conf import settings
from django.conf.urls.static import static
from leads.views import LandingPageView, landing_page, SignupView
from django.contrib import admin
from django.urls import path, include
from leads.views import landing_page
from django.contrib.auth.views import LoginView,LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/', include('leads.urls', namespace="leads")),
    path('', LandingPageView.as_view(), name="landing-page"),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('agents/', include('agents.urls', namespace="agents")),
    # password reset form template is not being triggered for some reason
    path('reset-password/', PasswordResetView.as_view(), name="reset-password"),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)