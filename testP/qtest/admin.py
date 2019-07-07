from django.contrib import admin, messages
from testP.qtest.models import Office, Company


# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    pass


class HeadQuarterAdmin(admin.ModelAdmin):
    pass


class OfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'street', 'city', 'company', 'headquarter']

    def save_model(self, request, obj, form, change):
        if not obj.headquarter:
            obj.save()
        elif Office.objects.filter(company=obj.company, headquarter=obj.headquarter).exists():  # noqa
            messages.set_level(request, messages.ERROR)
            messages.error(request, 'This company has already headquarter!')
            return
        else:
            obj.save()


admin.site.register(Office, OfficeAdmin)
admin.site.register(Company, CompanyAdmin)
