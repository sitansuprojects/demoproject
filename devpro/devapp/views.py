from django.shortcuts import render
from datetime import datetime
# Create your views here.
def Home(request):
    name='Sitansu'
    datetime1=datetime.date(datetime.now())
    return render(request,'home.html',{'name':name,'datetime1':datetime1})
