from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from salesapp.models import Student


# Create your views here.
def login(request):
    # Only display the error message if login fails during POST request
    if request.method == 'POST':
        name = request.POST['loginname']
        password = request.POST['loginpsw']
        print(request.POST)
        exist_user = authenticate(request, username=name, password=password)

        if exist_user is not None:
            if exist_user.is_superuser:
                return render(request,'home.html',{'name':name})
            elif exist_user.is_authenticated:
                return render(request, 'home.html',{'name':name})
                #   return HttpResponse(f'<h1>welcome to {name} sales person</h1>')
        else:
            # Authentication failed: show the error message
            return render(request, 'login.html', {'message': True})

    # For GET requests, just render the login page without any error context
    return render(request, 'login.html')




def signin(request):
    if request.method=='POST':
        name=request.POST['signinname']
        email=request.POST['signinemail']
        password=request.POST['signinpsw']

        if User.objects.filter(Q(username=name) | Q(email=email)).exists():
            return render(request,'signin.html',{'message': True})
        else:
            user=User.objects.create_user(username=name,email=email,password=password)
            user.save()
            return redirect('login')
    else:
        print('failer')

    return render(request,'signin.html')


def home(request):
    return render(request,'home.html')


def add_student(request):
    if request.method == 'POST':
        s1=Student()

        s1.salse_person_id= request.POST.get('salesperson')
        s1.date_of_join = request.POST.get('date')
        s1.name = request.POST.get('txtname')
        s1.email = request.POST.get('email')
        s1.age = request.POST.get('age')
        s1.place = request.POST.get('place')
        s1.education = request.POST.get('education')
        s1.skills = request.POST.get('skills')
        s1.save()

        return redirect('display')

    else:
        salsedata = User.objects.all()

        return render(request, 'add_student.html',{'salsedata':salsedata})


def display(request):
    studenetdata=Student.objects.all()
    return render(request,'display.html',{'studentdata':studenetdata})


def logout(request):
    return render(request,'logout.html')


def update(request,id):
    salsedata = User.objects.all()
    s1=Student.objects.get(id=id)

    if request.method=="POST":
        s1.salse_person_id = request.POST.get('salesperson')
        s1.date_of_join = request.POST.get('date')
        s1.name = request.POST.get('txtname')
        s1.email = request.POST.get('email')
        s1.age = request.POST.get('age')
        s1.place = request.POST.get('place')
        s1.education = request.POST.get('education')
        s1.skills = request.POST.get('skills')
        s1.save()

        return redirect('display')
    else:
        return render(request,'add_student.html',{'salsedata':salsedata,'student':s1})






def delete(request,id):
    # return HttpResponse(id)

    st_data=Student.objects.get(id=id)
    st_data.delete()
    return redirect('display')