from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from allauth.account.views import confirm_email

from .views import CheckAuthView

admin.autodiscover()

urlpatterns = [
    path('accounts/check-auth/', CheckAuthView.as_view(), name='check-auth'),
    
    re_path(r'accounts/verify-email/(?P<key>\w+)/$',
        confirm_email, name="account_confirm_email"),
    path("", TemplateView.as_view(template_name="index.html")),
    path("accounts/", include("allauth.urls")),
    path("accounts/profile/", TemplateView.as_view(template_name="profile.html")),
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
]
