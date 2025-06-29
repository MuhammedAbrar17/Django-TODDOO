from django . shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from todo import models
from todo.models import TODOO
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method=='POST':
     fnm=request.POST.get('fnm')
     emailid=request.POST.get('email')
     pwd=request.POST.get('pwd')
     my_user=User.objects.create_user(fnm,emailid,pwd)
     my_user.save()
     print(fnm,emailid,pwd)
     return redirect('/login')

    return render(request,'signup.html')

def Login(request):
    if request.method == 'POST':
       fnm=request.POST.get('fnm')
       pwd=request.POST.get('pwd')
       user = authenticate(request, username=fnm,password=pwd)
       if user is not None:
          login(request,user)
          return redirect("/todopage")
       else:
          return redirect('/login')
    return render(request,'login.html')

@login_required(login_url='/login')

def todo(request):
   if request.method == 'POST':
      title=request.POST.get('title')
      print(title)
      models.TODOO.objects.create(title = title, user= request.user)
      return redirect('/todopage')
      
   todos = TODOO.objects.filter(user=request.user).order_by('-date')
   return render(request,'todo.html',{'todos': todos})


@login_required(login_url='/login')
def edit_todo(request,srno):
   todo_item = get_object_or_404(TODOO, srno=srno, user=request.user)

   if request.method == 'POST':
      new_title = request.POST.get('title')
      todo_item.title = new_title
      todo_item.save()
      return redirect('/todopage')
    
   return render(request,'edit_todo.html',{"todo":todo_item})

@login_required(login_url='/login')
def delete_todo(request,srno):
   todo = models.TODOO(srno = srno , user=request.user)
   todo.delete()
   print("todo was deleted")
   return redirect('/todopage')


def signout(request):
   logout(request)
   return redirect('/login')