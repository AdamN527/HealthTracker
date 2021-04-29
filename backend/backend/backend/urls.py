from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend1.urls', namespace='backend1')),
    path('api/', include('backend_api.urls', namespace='backend_api')),
]
