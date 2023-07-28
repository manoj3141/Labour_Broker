from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import *
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.db.models import Q
# Create your views here.
def home(request):
 if request.user.is_authenticated:
    try:
        Labour_type.objects.get(user__username=request.user)
    except:
        if Labour_type.DoesNotExist: 
               return render(request,'basic/choice.html')
    l=Labour_type.objects.get(user__username=request.user)       
    if l.reg_type=='labour':        
     try:
        Labour_data.objects.get(user__username=request.user)    
     except:
        if Labour_data.DoesNotExist: 
               return redirect('labourform')       
    
    return render(request,'basic/home.html')
 else:
     return redirect('/')   
    

def usignup(request):
   if not request.user.is_authenticated:
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return render(request,'basic/choice.html')
        
    else: 
        form=signupform()   
    return render(request,'basic/signup.html',{'form':form})
   else:
       return redirect('home')
   
def ulogin(request):
   if not request.user.is_authenticated: 
    if request.method=='POST':
        #print('hi')
        form=loginform(request=request,data=request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request,user)
                return redirect('home')
        
    else: 
        form=loginform()   
    return render(request,'basic/login.html',{'form':form})
   else:
       return redirect('home')
    
def ulogout(request):
    logout(request)
    return redirect('login')

def choosechoice(request):
    if request.user.is_authenticated:
        user=request.user
        userdata=User.objects.get(username=user.username)
        #print(userdata)
        type=request.GET.get('type')
        if type == 'labour':
            a=Labour_type.objects.create(reg_type=type,user=userdata)
            a.save()
            return redirect('labourform')
        else:
           a=Labour_type(reg_type=type,user=userdata)
           a.save()
           return redirect('home')
        
def showchoice(request):
    return render(request,'basic/choice.html')     
    
        
        
def labour_form(request):  
   if request.user.is_authenticated:
        try:
            Labour_type.objects.get(user__username=request.user)
        except:
           if Labour_type.DoesNotExist: 
               return render(request,'basic/choice.html') 
        if request.method=='POST':
                   form=labourform(request.POST)
                   if form.is_valid():
                       data=form.save(commit=False)
                       data.user=request.user
                       data.save()
                       return redirect('home')
                   else:
                       error=messages.error(request,'not valid')
                       form=labourform()
                       return render(request,'basic/labourform.html',{'form':form})
        else: 
                    form=labourform()
                    return render(request,'basic/labourform.html',{'form':form})                             
   else:                   
       return redirect('signup') #redirct to singup page
       
       
    
def ai(request):
    if request.method=='POST':
        l=-1
        out=request.POST.get("ai")
        out=out.replace(' ','')
        qus=[ ['hi','namaste'],['howareyou'],['aboutyou'],['aboutlabourbroker','labourbroker'],['seemydetails','seedetails'],['phonenumber']]
        ans=['Hi','I am fine','I am an A.I',"It's acts an interface between worker and owner.The Worker can register his details like no of labours he have at current time,salary per worker, contact details and his location so on...The owner or a person who has necessity of doing works like construction,agricultural etc..  can search workers on his nearby location by using our app and workers also can get job by this app ",'you can see by clicking the profile in the home page']
        for q in qus:
          l+=1
          for q in q:
            if q in out:
             out=ans[l]   
             return render(request,'basic/ai.html',{'out':out}) 
        else:  
           out="Sorry I couldn't understand......." 
           return render(request,'basic/ai.html',{'out':out})  
    else:
        out="Hi,How can I help you......."
        return render(request,'basic/ai.html',{'out':out})    
    
def profile(request):
 if request.user.is_authenticated: 
  type_data=Labour_type.objects.get(user__username=request.user)   
  if type_data.reg_type=='labour': 
     if request.method=='POST':
        #username=User.objects.get(username=request.user)
        data=Labour_data.objects.get(user__username=request.user)
        form=labourform(request.POST,instance=data)
        #print('yes')
        if form.is_valid():
            form.save()
            return render(request,'basic/home.html')
        else:
            return redirect('labourform')
     else:
        data=Labour_data.objects.get(user__username=request.user)
        form=labourform(instance=data)
        return render(request,'basic/profile.html',{'form':form})    
  else: 
         userdata=User.objects.get(username=request.user)
         return render(request,'basic/profile.html',{"userdata":userdata })  
     
 else:
    messages.error(request, "you can see profile only after login")
    return render(request,'basic/profile.html')               
         
def showlabour(request):
    if request.method=='POST':
        name=request.POST.get('name')
        loc=request.POST.get('location')
        type=request.POST.get('worktype')
        
        
        if name!='' and loc!='' and type!='':
            if type=='All':
             data=Labour_data.objects.filter(Q(name__icontains=name)&Q(location__icontains=loc))
            else: 
             data=Labour_data.objects.filter(Q(name__icontains=name)&Q(location__icontains=loc)&Q(type__icontains=type))
            
        elif name!='' and loc!='': 
            data=Labour_data.objects.filter(Q(location__icontains=loc)&Q(name__icontains=name))
        elif  loc!='' and type!='': 
            if type=='All':
             data=Labour_data.objects.filter(Q(location__icontains=loc))
            else: 
             data=Labour_data.objects.filter(Q(location__icontains=loc)&Q(type__icontains=type))    
        elif name!='' and type!='': 
            if type=='All':
             data=Labour_data.objects.filter(Q(name__icontains=name))
            else:
             data=Labour_data.objects.filter(Q(type__icontains=type)&Q(name__icontains=name))    
        else:
            if name!='':
                data=Labour_data.objects.filter(name__icontains=name)
            elif loc!='':
                data=Labour_data.objects.filter(Q(location__icontains=loc))    
            elif type=='All':
                data=Labour_data.objects.all()
            elif type!='':
                 data=Labour_data.objects.filter(type__icontains=type)   
            else:    
                data=Labour_data.objects.filter(Q(name__icontains=name)|Q(location__icontains=loc)|Q(type__icontains=type))
                
        return render(request,'basic/labourpage.html',{'data':data})
    
def showprofile(request):
    if request.user.is_authenticated: 
      type_data=Labour_type.objects.get(user__username=request.user)   
      if type_data.reg_type=='labour': 
          data=Labour_data.objects.get(user__username=request.user)  
          print(data.other_type)  
          return render(request,'basic/dprofile.html',{'data':data})  
      else:
          userdata=User.objects.get(username=request.user)
          return render(request,'basic/dprofile.html',{"userdata":userdata }) 