from django.shortcuts import render
from django.conf import settings
from shopify_auth.decorators import login_required


@login_required
def home(request, *args, **kwargs):
    return render(request, "auth_app/index.html", {
        'SHOPIFY_APP_API_KEY': settings.SHOPIFY_APP_API_KEY,
        'SHOPIFY_APP_NAME': settings.SHOPIFY_APP_NAME,
    })
