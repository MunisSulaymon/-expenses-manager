from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    TYPE_CHOICES = [
        ('income', 'Income'),
        ('outcome', 'Outcome'),
    ]

    name        = models.CharField(max_length=100)
    type        = models.CharField(max_length=20, choices=TYPE_CHOICES)
    icon        = models.CharField(max_length=10)
    is_private  = models.BooleanField(default=False)
    created_by  = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"