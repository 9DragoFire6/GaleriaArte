from django.contrib import admin
from django.urls import path, include
from core import urls as todo_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('todos/', include(todo_urls))
]
