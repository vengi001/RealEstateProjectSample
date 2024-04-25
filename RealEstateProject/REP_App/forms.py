from django import forms

from .models import property_profile, tenant_profile
from django.contrib.admin.widgets import AdminDateWidget

class propertyform(forms.ModelForm):
    class Meta:
        model = property_profile
        fields = ['property_name','address','location','unit_type','rent']

class tenantform(forms.ModelForm):
    class Meta:
        model = tenant_profile
        fields = ['tenant_name','address','unit_type','property','document','agreementend_date','monthly_rent','monthly_rent_date']
        document = forms.FileField(
        label='Select a file',
    )
        widgets = {
        'agreementend_date': forms.DateInput(attrs={'type': 'date'}),
        'monthly_rent_date': forms.DateInput(attrs={'type': 'date'}),

    }
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['document'].widget.attrs['accept'] = 'application/pdf'
        


    

# class tenantrentalform(forms.ModelForm):
#     class Meta:
#         model = tenant_rental_info
#         fields = ['tenant','agreementend_date','monthly_rent','monthly_rent_date']