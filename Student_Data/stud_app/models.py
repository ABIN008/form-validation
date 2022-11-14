from django.db import models

# Create your models here.
from django.db import models

from stud_app.validators import gmail_validation

class Student(models.Model):
    options = [
    ('1st std', '1st std'),
    ('2nd std', '2nd std'),
    ('3rd std', '3rd std'),
    ('4th std', '4th std'),
    ('5th std', '5th std'),
    ('6th std', '6th std'),
    ('7th std', '7th std'),
    ('8th std', '8th std'),
    ('9th std', '9th std'),
    ('10th std', '10th std'),
    ('11th std', '11th std'),
    ('12th std', '12th std'),

    ]
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        validators=[gmail_validation],
    )
    age = models.IntegerField(
        blank=False,
        null=True,
    )
    Class = models.CharField(
        max_length = 20,
        choices = options,
        default = '1'
        )

    description = models.TextField(
    
        
    )
