from django.urls import path
from .views import CategoryListView, DuaListView, CategoryDuaListView

urlpatterns = [
    # Endpoint: http://127.0.0.1:8000/api/categories/
    path('categories/', CategoryListView.as_view(), name='category-list'),

    # Endpoint: http://127.0.0.1:8000/api/duas/
    path('duas/', DuaListView.as_view(), name='dua-list'),

    # Endpoint: http://127.0.0.1:8000/api/duas/category/1/
    # This <int:category_id> part is dynamic. It captures the number you type.
    path('duas/category/<int:category_id>/', CategoryDuaListView.as_view(), name='category-dua-list'),
]