from django import forms
from .models import Booking

class DateInput(forms.DateInput):
    input_type = 'date'
class BookingForm(forms.ModelForm) :
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'booking_date': DateInput(),
        }
        labels = {
            'name': " Name :",
            'phone': " Contact number :",
            'email': " Email:",
            'service_name': "Services:",
            'message': "Message:",
            'booking_date': "Booking Date:",
        }
