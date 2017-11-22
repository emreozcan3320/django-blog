from django.shortcuts import render

# Create your views here.

def index(request):
    # Because we use view.py, we use render but generally people dont use view.py

    #We can enter three field first obligatory field request second html
    # and third a dictionary that keep data for jinja and when rendering they rendered by jinja
    return render(request,'personal/home.html')

def contact(request):
    return render(request,'personal/basic.html', {'content':['If you would like to contact me, please email me ','emreozcan3320@gmail.com']})
