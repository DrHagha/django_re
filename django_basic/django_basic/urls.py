from django.contrib import admin
from django.urls import path, include
import myapp.views
import staticapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', staticapp.views.home),
    path('st', staticapp.views.home),
    path('dd', myapp.views.first),
    path('second/', myapp.views.second),
     
    path('products/', include('product.urls')),
    path('board/', include('product.urls')),
    
   
    
]
