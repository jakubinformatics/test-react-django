from rest_framework import serializers
from .models import Company, Office
from django.db.models import Sum


class CompanySerializer(serializers.ModelSerializer):
    headquarter_office = serializers.SerializerMethodField()
    sum_office_rent = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ('id', 'name', 'headquarter_office', 'sum_office_rent', )

    def get_headquarter_office(self, obj):
        query_set = Office.objects.filter(company=obj, headquarter=True)
        serializer = OfficeSerializer(query_set, many=True)
        print(serializer.data)
        result = {}

        if len(serializer.data) > 0:
            result['street'] = serializer.data[0]['street']
            result['city'] = serializer.data[0]['city']
            result['postal_code'] = serializer.data[0]['postal_code']

        return result

    def get_sum_office_rent(self, obj):
        query_set = Office.objects.filter(company=obj).aggregate(Sum('monthly_rent'))  # noqa
        print(query_set)
        return query_set['monthly_rent__sum']


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = "__all__"
