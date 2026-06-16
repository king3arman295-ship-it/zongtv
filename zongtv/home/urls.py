from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
     path(
        'video/<int:id>/',
        views.video_detail,
        name='video_detail'
    ),
    path(
    'show/<int:id>/',
    views.show_detail,
    name='show_detail'
),
path(
    'channel/<int:id>/',
    views.channel_detail,
    name='channel_detail'
),
path(
    'shows/',
    views.all_shows,
    name='all_shows'
),
path(
    'category/<int:id>/',
    views.category_detail,
    name='category_detail'
),
path(
    'channels/',
    views.all_channels,
    name='all_channels'
),
path(
    "lazy-category/<int:id>/",
    views.lazy_category,
    name="lazy_category"
),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )