from django.shortcuts import render
from .models import Register
from .models import Food
from .models import FoodMaxmam
from .models import FoodAmmount
from .models import Fooditems
from app.form import FoodReg
from .models import Fooitem
def index(request):
    return render(request,"index.html")


def fooditems(request):
    qr=Register.objects.filter()
    return render(request,"food.html",{"qr":qr})


def foodidno(request,pk):
    qr=Register.objects.get(name=pk)
    qra=int(qr.cost)
    qrb=int(qr.discount)
    qrc=qra-qrb
    qrd = Register.objects.filter()
    return render(request, "foodidno.html", {"qr": qr, "qrc": qrc, "qrd": qrd})




def send(request,pk):
    Quality=request.POST.get("Quality")
    qr = Register.objects.get(name=pk)
    qra = int(qr.cost)
    qrb = int(qr.discount)
    qrc = qra - qrb
    qrf=int(Quality)
    qrd=qrc*qrf
    qre = Register.objects.filter()
    Fooitem(name=qr.name,Quality=Quality).save()
    FoodMaxmam(foodname=qr.foodname, Booking=qr.Booking).save()
    reg=Fooitem.objects.get(name=pk)
    if qr.name==reg.name:
        RegBook=int(qr.Booking)-int(Quality)
        Register(name=qr.name,foodname=qr.foodname,cost=qr.cost,Total=qr.Total,Booking=RegBook,discount=qr.discount,Date=qr.Date).save()
        if RegBook==0:
            qr = Register.objects.filter()
            return render(request, "Success.html", {"message":"This Food Items Complited Select Next Items Food","qr":qr})
        elif RegBook==1:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook==2:
             qr = Register.objects.filter()
             return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook==3:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook==4:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})

        elif RegBook==5:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook==6:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook==7:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook==8:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook == 9:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality,"qr": qr})
        elif RegBook == 10:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook == 11:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook == 12:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message":"Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})

        elif RegBook == 13:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality,"qr": qr})
        elif RegBook == 14:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook == 15:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook == 16:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook == 17:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook == 18:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook == 19:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "Thank You  Your Seleceted 1 Items Plates:","Quality":Quality, "qr": qr})
        elif RegBook == 20:
            qr = Register.objects.filter()
            return render(request, "Success.html",{"message": "This Food Items Complited Select Next Items Food", "qr": qr})
        else:
            return render(request, "foodid.html", {"qr": qr, "qrc": qrc, "qrd": qrd, "qre": qre, "RegBook": RegBook})


    else:
        pass


def show(request):
    Total=request.POST.get("Total")
    FoodAmmount(Total=Total).save()
    qr = Register.objects.filter()
    return render(request,"Successfull.html",{"message":"Successfull Register","qr":qr})

def update(request):
    qr=Register.objects.filter()
    return render(request,"Successfull.html")