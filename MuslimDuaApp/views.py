from rest_framework import generics
from .models import Category, Dua
from .serializers import CategorySerializer, DuaSerializer

# 1. View to list all Categories
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# 2. View to list all Duas
class DuaListView(generics.ListAPIView):
    queryset = Dua.objects.all()
    serializer_class = DuaSerializer

# 3. View to list Duas for a specific Category
# Example: Only show "Morning" duas
class CategoryDuaListView(generics.ListAPIView):
    serializer_class = DuaSerializer

    def get_queryset(self):
        # We get the category ID from the URL
        category_id = self.kwargs['category_id']
        # We filter the Duas to find only those belonging to that category
        return Dua.objects.filter(category__id=category_id)