from django.contrib import admin
from django.urls import path, include,re_path
from community import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/account/",include('account.urls')),
    path("api/product/",include('product.urls')),
    path("api/community/",include('community.urls')),
    path("api/shop/",include('shop.urls')),
    path("api/community-search/result", views.search_posts),
    path("api/ocr/",include('ocr.urls')),
    path("api/taking/",include('taking.urls')),

    
    
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^registerSW.js$', serve, {'path': 'registerSW.js', 'document_root': settings.STATIC_ROOT}),
    re_path(r'^manifest.webmanifest$', serve, {'path': 'manifest.webmanifest', 'document_root': settings.STATIC_ROOT}),
    re_path(r'^sw.js$', serve, {'path': 'sw.js', 'document_root': settings.STATIC_ROOT}),
    re_path(r'^workbox-fa446783.js$', serve, {'path': 'workbox-fa446783.js', 'document_root': settings.STATIC_ROOT}),
    re_path(r'^icons/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'front', 'public', 'icons')}),
    re_path(r'^.*', TemplateView.as_view(template_name="index.html")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

