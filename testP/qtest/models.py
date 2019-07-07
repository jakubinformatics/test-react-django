from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField('Name', max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Office(models.Model):
    name = models.CharField('Name', max_length=256)
    street = models.CharField('Street', max_length=256, blank=True)
    postal_code = models.CharField('Postal Code', max_length=32, blank=True)
    city = models.CharField('City', max_length=128, blank=True, null=True)
    monthly_rent = models.DecimalField(decimal_places=2, max_digits=10, blank=True, null=True)  # noqa
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    headquarter = models.BooleanField('Is headquarter?', default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.headquarter:
            super(Office, self).save(*args, **kwargs)
        elif Office.objects.filter(company=self.company, headquarter=self.headquarter).exists():  # noqa
            pass
        else:
            super(Office, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name', )


    
