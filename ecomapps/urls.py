from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='ecomapps'
urlpatterns = [
  path('list/', views.ProductList.as_view(), name='list'),
  path('details/<int:pk>', views.ProductDetail.as_view(), name='detail'),
  path('base/',views.Base.as_view(),name='base'),
   path('create/',views.ProductCreateView.as_view(),name='create'),
   path('price/list/', views.ProductPriceList.as_view(), name='price_list'),
   path('category/list/', views.CategoryList.as_view(), name='category_list'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)