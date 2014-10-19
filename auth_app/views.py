from django.shortcuts import render
from django.conf import settings
from shopify_auth.decorators import login_required
import shopify


@login_required
def home(request, *args, **kwargs):

    # Get a list of the user's products.
    with request.user.session:
        products = shopify.Product.find()

    return render(request, "auth_app/index.html", {
        'products': products,
        'SHOPIFY_APP_API_KEY': settings.SHOPIFY_APP_API_KEY,
        'SHOPIFY_APP_NAME': settings.SHOPIFY_APP_NAME,
    })
