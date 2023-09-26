from django import forms
from django.contrib.auth.models import User
from . import models 
from django import forms

class bookform(forms.ModelForm):
        class Meta:
            model=models.Bookinfo
            fields=['book_name','author','genre','language']
            
class yourForm(forms.Form):
    options = forms.MultipleChoiceField(
        choices=[(option, option) for option in
                models.Bookinfo.objects.values_list('genre')], widget=forms.CheckboxSelectMultiple(),
        label="myLabel", required=True, error_messages={'required': 'myRequiredMessage'})