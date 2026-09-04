from django.db import models

# Create your models here.
class Registration(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    NATIONALITY = [
        ('Ugandan','Ugandan'),
        ('Kenyan','Kenyan'),
        ('Tanzanian','Tanzanian'),
        ('Burundian', 'Burundian'),
        ('Rwandese', 'Rwandese'),
        ('Somali','Somali'),
        ('South Sudanese','South Sudanese'),
    ]

    MARITAL_STATUS = [
        ('Single','Single'),
        ('Married','Married'),
        ('Divorced','Divorced'),
        ('Widowed','Widowed'),
        ('Separated','Separated'),
    ]

    SETTELEMENT_CAMP = [
        ('Gulu settlement camp','Gulu settlement camp'),
        ('Arua settlement camp','Arua settlement camp'),
        ('Mbarara settlement camp','Mbarara settlement camp'),
        ('Kasese settlement camp','Kasese settlement camp'),
        ('Busia settlement camp','Busia settlement camp'),
        ('Mbale settlement camp','Mbale settlement camp'),
        ('Kigezi settlement camp','Kigezi settlement camp'),
    ]
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Date_of_Birth = models.DateField(auto_now_add=False)
    Place_of_Birth = models.CharField(max_length=50)
    Gender = models.CharField(max_length=50,choices= GENDER)
    Nationality = models.CharField(max_length=50,choices= NATIONALITY)
    Marital_Status = models.CharField(max_length=50,choices= MARITAL_STATUS)
    Settlement_camp = models.CharField(max_length=50,choices= SETTELEMENT_CAMP)
    Date_of_joining_Settlement_camp = models.DateField(auto_now_add=False)

    def __str__(self):
        f'{self.First_Name} {self.Last_Name}'
