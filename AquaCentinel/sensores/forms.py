from django import forms
from .models import Boya, RegistroSensor

#class UserForm(forms.Form):
#    username = forms.CharField(min_length=3)
#    email = forms.EmailField()
#    age = forms.IntegerField(min_value=18)
#
#@csrf_exempt

class BoyaForm(forms.ModelForm):
    class Meta:
        model = Boya
        fields = [
            "codigo_boya",
            "usuario"
        ]


class RegistroSensorForm(forms.ModelForm):
    class Meta:
        model = RegistroSensor
        fields = [
            "boya",
            "ph",
            "turbidez",
            "temperatura",
            "conductividad",
        ]
    
    
    
    
    


