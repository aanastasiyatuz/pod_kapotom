from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, action
from .models import *
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Comment
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import CommentSerializer, ProductSerializer

class CommentViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
    
class ProductViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
    
    @action(methods=["GET"], detail=False)
    def search(self, request):
        title = request.query_params.get("title")
        queryset = self.get_queryset()
        if title:
            queryset = queryset.filter(title_icontains=title)
        
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, 200)

@api_view(["GET"])
def toggle_like(request, p_id):
    user = request.user
    product = get_object_or_404(Product, id=p_id)

    if Like.objects.filter(user=user, product=product).exists():
        Like.objects.filter(user=user, product=product).delete()
    else:
        Like.objects.create(user=user, product=product)
    return Response("Like toggled", 200)

@api_view 
def add_rating(request, p_id):
    user = request.user
    value = request.POST.get('value')
    product = get_object_or_404(Product, id=p_id)
    if not value:
        raise ValueError('value is required')

    if Rating.objects.filter(user=user, product=product).exists():
        rating = Rating.objects.get(user=user, product=product)
        rating.value = value
        rating.save()
    else:
        Rating.objects.create(user=user, product=product, value=value)
    
    return Response('rating created', 201)

