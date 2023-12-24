from django.contrib import admin
# from django.template.defaulttags import url

# from django.views.static import serve
# from onlineshop.settings import DEBUG,MEDIA_ROOT
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('sellerlog/', ),
# ]
#
#
# if DEBUG:
#     urlpatterns.append(url(r'^/media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}))


from django.urls import include
from django.conf.urls.static import static
from django.urls import path
from onlineshop import settings
from shop import views

urlpatterns = [
    path('',views.index),
    path('index/',views.index),
    path('seller/', include('seller.urls')),
    path('buyer/', include('buyer.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)