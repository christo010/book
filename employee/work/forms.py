from django import forms
from work.models import bookdb,personal,studentdb
class Empform(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.IntegerField()
    contact=forms.IntegerField()

class bookform(forms.ModelForm):
    class Meta:
        model=bookdb
        fields="__all__"


        #fields=['title','author','year','genere']

class persform(forms.ModelForm):
    class Meta:
        model=personal
        fields="__all__"


class studentform(forms.ModelForm):
    class Meta:
        model=studentdb
        fields="__all__"


    
