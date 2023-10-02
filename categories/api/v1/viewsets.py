from rest_framework.viewsets import ModelViewSet
from categories.api.v1.serializers import CategorySerializer
from categories.models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer

    def get_queryset(self):
        parent = self.request.query_params.get("parent")
        queryset = Category.objects.filter(parent=parent).select_related("parent") if parent else self.queryset
        return queryset
