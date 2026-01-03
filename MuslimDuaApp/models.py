from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Dua(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='duas')

    title = models.CharField(max_length=200, help_text="e.g., Dua for anxiety")
    
    arabic_text = models.TextField(help_text="The actual Arabic script")
    transliteration = models.TextField(blank=True, help_text="English pronunciation")
    
    translation_en = models.TextField(help_text="English meaning")
    translation_ur = models.TextField(blank=True, help_text="Urdu meaning") 

    reference = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title