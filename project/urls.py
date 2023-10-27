from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView

admin.site.site_header = "Qjango by Quxdev"
admin.site.site_title = "Quxdev | Qjango"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("impersonate/", include("impersonate.urls")),
    path("", include("qux.auth.urls.appurls", namespace="qux_auth")),
    path("", TemplateView.as_view(template_name="qjango.html"), name="home"),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
