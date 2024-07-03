from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1> Manimaran SDE </h1>")



def index1(request):
    return HttpResponse("<h1>Working at Freshworks as SDE II</h1>")


def name(request , name):
    return HttpResponse(f"""
             <h1>
        {name}           
             </h1> 
             <h2>Working as SDE II at Freshworks</h2>                                
                        
                        
                        """)