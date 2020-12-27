from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 





def home(request):

    return render(request, 'home.html')


def physics11(request):
    return render(request, 'physics11.html', {'title': 'Physics11'})


def login(request):
    return render(request, 'login.html', {'title': 'Login'})


# def register(request):
#     return render(request, 'register.html', {'title': 'Register'})


def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, password)
        myuser.user_name= username
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('/login')

    else:
        return HttpResponse("404 - Not found")


    


    

  



