from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views  # main 함수 가져오기

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
