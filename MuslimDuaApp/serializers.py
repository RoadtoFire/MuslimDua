from rest_framework import serializers
from .models import Category, Dua

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # We want all fields: id, name, slug
        fields = '__all__'

class DuaSerializer(serializers.ModelSerializer):
    # This is a cool trick: 
    # Instead of just showing the category ID (e.g., "Category: 1"), 
    # we can use the depth option to show the Category details too.
    # But for now, let's keep it simple and just show the Category ID.
    
    class Meta:
        model = Dua
        # This will include: id, category, title, arabic_text, 
        # translation_en, translation_ur, reference
        fields = '__all__'