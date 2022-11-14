from django import forms
from django.core.exceptions import ValidationError
from stud_app.models import Student

class DetailForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"
       

    def clean(self):
       
        cleaned_data = super().clean() 
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        age = cleaned_data.get("age")

        if age <18:
             raise ValidationError("Must be greater than 18.")

        if not name and not email:
            raise ValidationError("Please provide name or email.")
        
        return cleaned_data
       

