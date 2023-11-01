from django.contrib import admin
from .models import Booking,Service
#

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','serv_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)
admin.site.register(Service)
