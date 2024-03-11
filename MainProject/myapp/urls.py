from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pagedetail/<int:id>', views.page_detail, name='page_detail'),
    path('pagedetail/<int:id>', views.page_detail, name='page_detail')
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
