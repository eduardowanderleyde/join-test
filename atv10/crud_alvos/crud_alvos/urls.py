from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('targets/', include('targets.api.v1.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]