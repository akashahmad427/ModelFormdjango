from django.shortcuts import render
from .forms import Student
# Create your views here.
def show(request):
    if request.method == 'POST':
        fm = Student(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print(name)
            print(email)
            print(password)


    else:
        fm = Student()
    return render(request,'enroll/first.html',{'forms':fm})

