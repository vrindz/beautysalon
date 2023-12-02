from django.db import models

# Create your models here.
class Service(models.Model):
    serv_name = models.CharField(max_length=100)
    serv_image = models.ImageField(upload_to='services')
    serv_desc = models.TextField()


    def __str__(self):
        return self.serv_name
class Booking(models.Model) :
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField()
    service_name = models.ForeignKey(Service, on_delete=models.CASCADE)
    message = models.CharField(max_length=400)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)
