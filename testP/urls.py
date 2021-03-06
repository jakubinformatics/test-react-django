from django.urls import include, path
from rest_framework import routers
from testP.qtest import views
from django.contrib import admin

router = routers.DefaultRouter()
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/v1/', include('testP.qtest.urls', namespace='testP.qtest')),
]