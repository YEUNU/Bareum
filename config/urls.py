from django.contrib import admin
from django.urls import path, include
from community import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("api/account/",include('account.urls')),
    path("api/product/",include('product.urls')),
    path("api/community/",include('community.urls')),
    path("api/shop/",include('shop.urls')),
    path("api/community-search/result", views.search_posts),
]
