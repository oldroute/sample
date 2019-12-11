from django.views.generic import ListView
from django.contrib import admin
from django.urls import path
from sample.models import Planet

admin.site.site_header = 'Солнечная система'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListView.as_view(template_name='index.html', model=Planet))
]
