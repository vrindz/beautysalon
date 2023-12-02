from django.contrib import admin
from .models import Booking,Service
#

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','email','service_name','message','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)
admin.site.register(Service)
