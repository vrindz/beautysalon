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
            'p_name': " Name :",
            'p_phone': " Contact number :",
            'p_email': " Email:",
             'serv_name': "Services:",
            'booking_date': "Booking Date:",
        }
