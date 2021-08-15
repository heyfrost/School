from django import forms
from .models import *
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class Messageform(forms.ModelForm):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    content = models.TextField()

    class Meta:
        model = Messages
        fields = ('name', 'email', 'mobile', 'content',)

class AdmissionForm(ModelForm):
    class Meta:
        model = Admission_form
        fields = '__all__'
        widgets = {
            'dob':DateInput(),
            'g_caddress': forms.Textarea(attrs={'rows':4, }),
            'g_paddress': forms.Textarea(attrs={'rows':4, }),
            'c_address': forms.Textarea(attrs={'rows':4, }),
        }