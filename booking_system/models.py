from django.db import models

class Booking(models.Model):
    customer_name = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return f"{self.customer_name} - {self.destination}"
