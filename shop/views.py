from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import *
from rest_framework.response import Response
@api_view(["GET"])
def toggle_like(request, p_id):
    user = request.user
    product = get_object_or_404(Product, id=p_id)

    if Like.objects.filter(user=user, product=product).exists():
        Like.objects.filter(user=user, product=product).delete()
    else:
        Like.objects.filter(user=user, product=product)
    return Response("Like toggled", 200)