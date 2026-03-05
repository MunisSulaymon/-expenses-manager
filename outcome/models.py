from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

class Outcome(models.Model):

    amount      = models.DecimalField(max_digits=10, decimal_places=2)
    date        = models.DateField()
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.date}"

    class Meta:
        verbose_name_plural = "Outcomes"