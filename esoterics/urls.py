from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('user/', include('user.urls')),
	path('data/', include('data.urls')),
	path('', include('frontend.urls')),
	*static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
]
