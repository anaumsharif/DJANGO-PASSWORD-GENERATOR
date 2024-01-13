from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import random



# Create your views here.
# Login required for backend and front end is coded here
# for password generation or login we need a function we need and then we will be calling that function in the urls.py in the  mainproject 

def home(request): # whenever someone requests for the homepage.So they will be provided with this page or this function will be called.
    # return HttpResponse("<h1>Hello world!!</h1><br> <h2>My first Django Project</h2>") # saving the file and adding the url
    return render(request, 'home.html')

def passgen(request):
    char =list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('digits'):
        char.extend(list('0123456789'))
    if request.GET.get('symbol'):
        char.extend(list('+-*/%!@$%^&~`'))
        
    length = int(request.GET.get('length',10))
    
        
        
        
        
    password =""
    for x in range (length): # 8 didgit password so from 0 to 7 
        password += random.choice(char)
    # pas = {'password':password} #json object 
    return render(request ,'password.html',{'password':password})
    # return JsonResponse(pas)
    
    '''we are passing this password, which is which we have generated
in the form of dictionary, and it is coming going to the front end in the form of.
string and we are just passing this variable.'''









