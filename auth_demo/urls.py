from django.conf.urls import include, url

from auth_app.views import home

urlpatterns = [
    url(r'login/', include('shopify_auth.urls')),
    url(r'^$', home),
]
