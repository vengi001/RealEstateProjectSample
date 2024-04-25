from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

units = [('1BHK','1BHK'),
        ('2BHK','2BHK'),
        ('3BHK','3BHK'),
        ('4BHK','4BHK'),]

name_validator = RegexValidator(
        regex = r'^[a-zA-Z\s]*$',
        message='Name should be only in letters',
        code = 'invalidname'
    )
class property_profile(models.Model):
    property_name = models.CharField(max_length=100,validators=[name_validator])
    address = models.CharField(max_length=255)
    location = models.CharField(max_length=50)
    unit_type = models.CharField(max_length=4,choices=units)
    rent = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.property_name

class tenant_profile(models.Model):
    tenant_name = models.CharField(max_length=100,validators=[name_validator])
    address = models.CharField(max_length=255)
    unit_type = models.CharField(max_length=4,choices=units)
    property = models.ForeignKey(property_profile,on_delete=models.CASCADE)
    document = models.FileField(upload_to='property_documents/',blank=True,null=True)
    agreementend_date = models.DateField(blank=True,null=True)
    monthly_rent = models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    monthly_rent_date = models.DateField(blank=True,null=True)

    
    # def save(self, *args, **kwargs):
    #     self.property = self.property.property_name
    #     super().save(*args, **kwargs)
    # def __str__(self):
    #     return "(%s) %s" % (self.property.short, self.note)
    # def __unicode__(self):
    #     return u'(%s) %s' % (self.property.short, self.note)

# class tenant_rental_info(models.Model):
#     tenant = models.ForeignKey(tenant_profile,on_delete=models.CASCADE)
    
