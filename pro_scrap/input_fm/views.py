from django.shortcuts import render, HttpResponse
from .models import *


# Create your views here.
def index(request):
    if request.method == "POST":
        select_center = request.POST.get("select_center")
        select_category = request.POST.get("select_category")
        date = request.POST.get("trip-start")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")

        obj = applicant_data.objects.create(center=select_center, category=select_category, dob=date, first_name=fname,
                                            last_name=lname, email=email)
        obj.save()
        return render(request, 'index.html',{'resp':"message"})

    return render(request, 'index.html')


def applicant_detail(request):
    obj = applicant_data.objects.all()
    return render(request,'applicant_record.html',{'obj':obj})
