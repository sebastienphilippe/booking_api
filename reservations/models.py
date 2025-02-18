from django.db import models
from django.utils import timezone
# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.SmallIntegerField(default=1)
    BookingDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.Name}: {self.BookingDate.date()}'

class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2) 
    Inventory = models.SmallIntegerField(default=5)

    def __str__(self):
        return f'{self.Title}: ${self.Price:.2f}'