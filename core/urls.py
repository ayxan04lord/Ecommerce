from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from product.views import page_not_found

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("product.urls", namespace="product")),

    path("api/product/", include("product.api.urls")),
]

handler404 = page_not_found

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
