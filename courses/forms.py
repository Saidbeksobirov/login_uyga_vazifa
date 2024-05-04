from django import forms


class CoursesForm(forms.Form):
    full_name = forms.CharField()
    phone_number = forms.CharField()
    age = forms.IntegerField()
