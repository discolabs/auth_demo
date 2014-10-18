from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'login/$', include('shopify_auth.urls')),
    url(r'^$', 'auth_app.views.home'),
)
