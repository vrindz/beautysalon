from django.shortcuts import render

from .forms import BookingForm

from .models import Service


# Create your views here.
def index(request):
     #return HttpResponse("Home Page")
     return render(request, "index.html")
def base(request):
    #return HttpResponse("Home Page")
    return render(request, "base.html")
def about(request):

    #return HttpResponse("About Page")


    return render(request, "about.html")
def service(request):
    serv_dict = {
        'service': Service.objects.all()
                }
    return render(request, "service.html", serv_dict)


def contact(request):

    #return HttpResponse("About Page")


    return render(request, "contact.html")

def booking(request):
    #form = forms.BookingForm()
    if request.method == "POST":
        formdemo= BookingForm(request.POST)
        if formdemo.is_valid():
            formdemo.save()
            return render(request,'c.html')
    myform1 = BookingForm()
    dict_book = {
        'formkey': myform1

    }
    return render(request, "booking.html",dict_book)

