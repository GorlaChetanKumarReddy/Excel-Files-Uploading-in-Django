from django import forms
from User_app.models import Files_Data

class Excel_Fileform(forms.ModelForm):
    class Meta:
        model = Files_Data
        fields = '__all__'