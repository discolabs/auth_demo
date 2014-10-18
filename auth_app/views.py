from django.http import HttpResponse
from shopify_auth.decorators import login_required


@login_required
def home(request, *args, **kwargs):
    message = "Welcome to my application, {0}!".format(request.user)
    return HttpResponse(message)
