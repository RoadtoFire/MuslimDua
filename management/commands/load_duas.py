import json
import os
from django.core.management.base import BaseCommand
from MuslimDuaApp.models import Dua, Category 
# ^^^ MAKE SURE 'api' matches your actual app name (e.g., 'duas' or 'main')

class Command(BaseCommand):
    help = 'Load Duas from the Fortress of the Muslim JSON'

    def handle(self, *args, **kwargs):
        # path to your JSON file
        file_path = os.path.join(os.getcwd(), 'data', 'duas.json')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR('File not found at: ' + file_path))
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # The JSON root key is "English" based on your file
        chapters = data.get('English', [])

        for chapter in chapters:
            # 1. Create or Get the Category (The "TITLE" in JSON)
            category_name = chapter.get('TITLE', 'Uncategorized').strip()
            category, created = Category.objects.get_or_create(
                name=category_name,
                defaults={'slug': category_name.lower().replace(' ', '-')}
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Category: {category_name}'))

            # 2. Process each Dua in this Chapter
            duas_list = chapter.get('TEXT', [])
            for index, item in enumerate(duas_list):
                
                arabic = item.get('ARABIC_TEXT', '')
                english = item.get('TRANSLATED_TEXT', '')
                transliteration = item.get('LANGUAGE_ARABIC_TRANSLATED_TEXT', '')

                # Clean up the text (remove HTML or extra spaces if any)
                arabic = arabic.strip()
                english = english.strip()

                # Generate a title since JSON doesn't have specific dua titles
                # We use the Category name + number (e.g., "Morning Dua #1")
                dua_title = f"{category_name} - {index + 1}"

                # 3. Create the Dua
                # We use update_or_create to avoid duplicates if you run script twice
                Dua.objects.update_or_create(
                    arabic_text=arabic,
                    category=category,
                    defaults={
                        'title': dua_title,
                        'translation_en': english,
                        'translation_ur': '', # Leaving Urdu blank for now
                        # If you have a transliteration field in your model, uncomment below:
                        # 'transliteration': transliteration 
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded all Duas!'))