from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, Office
from .serializers import CompanySerializer, OfficeSerializer


# Create your views here.
class CompanyListViewSet(APIView):
    def get(self, request, format=None):
        '''
        METHOD: GET
        ENDPOINT: /api/v1/company/        
        '''
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)


class OfficeListViewSet(APIView):
    def get(self, request, format=None):
        '''
        REQUEST_METHOD: GET
        ENDPOINT: /api/v1/office/?company=<company_name>
        '''
        
        if request.GET['company']:
            offices = Office.objects.filter(company__name=request.GET['company']).all()  # noqa
        else:
            offices = Office.objects.all()

        serializer = OfficeSerializer(offices, many=True)
        return Response(serializer.data)


class UpdateHeadquarter(APIView):
    def put(self, request, pk, format=None):
        '''
        REQUEST_METHOD: PUT,
        ENDPOINT: /api/v1/company/<company_id>/
        REQUEST_PARAM:
        {
            "office_id": 1
        }
        '''
        Office.objects.filter(company__pk=pk).update(headquarter=False)
        Office.objects.filter(id=request.data['office_id']).update(headquarter=True)  # noqa
        query_set = Office.objects.filter(company__pk=pk, headquarter=True).all()  # noqa
        serializer = OfficeSerializer(query_set, many=True)

        return Response(serializer.data)


class CreateCompanyOffice(APIView):
    def post(self, request):
        '''
        METHOD: POST
        ENDPOINT: /api/v1/add_company/
        REQEST PARAM:
        {
            "name": "company01",
            "offices": [
                {
                    "name": "Office - 1",
                    "street": "Street - 1",
                    "postal_code": "POST-1",
                    "city": "City - 1",
                    "monthly_rent": "10",
                    "headquarter": true
                },
                {
                    "name": "Office - 2",
                    "street": "Street -2",
                    "postal_code": "Post - 2",
                    "city": "City - 2",
                    "monthly_rent": "12",
                    "headquarter": false
                }
            ]
        }
        '''
        company = Company.objects.create(name=request.data['name'])
        for office in request.data['offices']:
            Office.objects.create(
                name=office['name'],
                street=office['street'],
                postal_code=office['postal_code'],
                city=office['city'],
                monthly_rent=office['monthly_rent'],
                company=company,
                headquarter=office['headquarter'],
            )
        query_set = Company.objects.filter(name=request.data['name'])
        serializer = CompanySerializer(query_set, many=True)

        return Response(serializer.data)
