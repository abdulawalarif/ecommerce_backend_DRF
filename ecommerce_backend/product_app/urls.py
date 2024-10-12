from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import ProductView

#here settings import can generate errors

urlpatterns = [
    path('products', ProductView.as_view(), name='product_list'),
    path('product/<int:pk>', ProductView.as_view(), name='product_detail'),
    path('product/delete/<int:pk>', ProductView.as_view(), name='product_delete'), 

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)