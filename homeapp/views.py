from django.shortcuts import render ,redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate ,login ,logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.


@never_cache
@login_required
def index(request):
    
    data = User.objects.all() # all objects from student table is passed to data
    context ={"data":data}
    return render(request,"index.html",context)

def insertData(request):
    if request.method =="POST":# if we are doing a POST hhtp 
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name') # assinging the values to a variable as name from html page from input tag's name
        email= request.POST.get('email')
        password= request.POST.get('password')

        query =User(username=first_name,last_name=last_name,email=email,password =password)# storing values from front-end to modeltable
        query.save()
        messages.info(request," Data Inserted Successfully")
        return redirect("/")
    return render(request,"index.html")

@never_cache
def updateData(request,id):
    if request.method =="POST": # if we are doing a POST hhtp 
        first_name_update = request.POST['first_name']
        last_name_update = request.POST['last_name'] # assinging the values to a variable as name from html page from input tag's name
        email_update= request.POST['email']
        password_update= request.POST['password']
       
        edit =User.objects.get(id=id)
        edit.first_name= first_name_update
        edit.last_name =last_name_update
        edit.email =email_update
        edit.password =password_update
        edit.save()
        
        messages.warning(request," Data Updated Successfully")
        return redirect('index')
    d = User.objects.get(id=id) # all objects from student table is passed to d variable
    context ={"d":d}
    return render(request,"update.html",context)

def deleteData(request,id):
    d = User.objects.get(id=id) # all objects from student table is passed to data
    d.delete()
    messages.warning(request," Data Deleted Successfully")
    return redirect('index')

"""def admin_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if .is_superuser:
           request.session['username'] = username
           login(request,user)
           return redirect('index')
        else:
            return redirect('admin_login')
    return render(request,"adminlogin.html")"""



@never_cache
def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('index')
            else:
                return redirect('admin_login')
        else:
            # Handle the case when authentication fails
            return redirect('admin_login')

    return render(request, "adminlogin.html")


@never_cache
def logoutpage(request):
    
    logout(request)
    return redirect('admin_login')

@never_cache
def registration(request):
    if 'first_name' in request.session:
       return redirect(home_page)
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        if password1 == password2:
           myuser = User.objects.create_user(username = first_name,last_name =last_name, email = email, password=password1)
           myuser.save()
           print(myuser,'0000000000000')
           #request.session['first_name'] = first_name
           return redirect(login_page)
        messages.warning(request," Password mismatching")
        return redirect(registration)

    return render(request,"registration.html")
@never_cache
def login_page(request):
    if request.user.is_authenticated and 'first_name' in request.session:
        return redirect(home_page)

    
    if request.method =="POST":
        first_name = request.POST['first_name']
        password3 = request.POST['password']
        user = authenticate(request,username= first_name,password =password3)
        if user is not None:
            login(request, user)
            request.session['first_name'] = first_name
            return redirect(home_page)
    return render(request,"login.html")



         
@never_cache
@login_required
def home_page(request):
    if request.user.is_authenticated:
        if 'first_name' in request.session:
            return render(request,"home.html")
    return redirect(login)
#    return render(request,"home.html")
   

@never_cache
def signout(request):
    if 'first_name' in request.session:
       request.session.flush() 
       logout(request)
    return redirect(login_page)
""" if 'first_name' in request.session:
        del request.session['first_name'] 
        request.session.flush()"""



    
