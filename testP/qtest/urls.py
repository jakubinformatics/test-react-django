from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from testP.qtest.views import CompanyListViewSet, OfficeListViewSet, \
                      UpdateHeadquarter, CreateCompanyOffice

app_name = 'qtest'

urlpatterns = [
    url(r'^company/(?P<pk>\d+)/$', UpdateHeadquarter.as_view()),
    url(r'^company/', CompanyListViewSet.as_view()),
    url(r'^register_company/', CreateCompanyOffice.as_view()),
    url(r'^office/', OfficeListViewSet.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
