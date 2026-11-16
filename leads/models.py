from django.db import models
from accounts.models import User

# Create your models here.

class Lead(models.Model):

    name=models.CharField(max_length=200)

    email=models.EmailField()

    phone=models.CharField(max_length=20)

    company_name=models.CharField(max_length=200,null=True)

    SOURCE_CHOICES=[
        ("website","website"),
        ("social media","social media"),
        ("referral","refferal"),
        ("advertisement","advertisement"),
        ("other","other")
    ]

    source=models.CharField(max_length=200,choices=SOURCE_CHOICES)

    STATUS_CHOICES=[
        ("new","new"),
        ("contacted","contacted"),
        ("interested","interested"),
        ("lost","lost")
    ]

    status=models.CharField(max_length=200,choices=STATUS_CHOICES,default="new")

    description=models.TextField(null=True)

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now_add=True)

    created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="leads")

    def __str__(self):

        return self.name

