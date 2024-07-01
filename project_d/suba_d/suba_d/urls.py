from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('suba_a.urls')),  # Include the URLs from the app
]
