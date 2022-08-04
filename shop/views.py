from rest_framework import mixins
from .models import Comment, Product
from .serializers import CommentSerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class CommentViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permissions_classes = [IsAuthenticated]

class ProductViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permissions_classes = [IsAuthenticatedOrReadOnly]