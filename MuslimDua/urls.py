from django.contrib import admin
from django.urls import path, include  # <-- Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Add this line. This prefixes all your app's URLs with 'api/'
    path('api/', include('MuslimDuaApp.urls')), 
]