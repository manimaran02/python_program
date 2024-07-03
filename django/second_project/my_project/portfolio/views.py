from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

projects = [
    {
        "id":1,
        "name": "Youtube Clone",
        "Language" : ["React Js,Redux,JavaScript"],
        "url" : "github"
    },
    {
        "id":2,
        "name" : "Food Delivery App",
        "Language" : ["Javascript,React,Redux"],
        "url" : "github"
    }

    ]

def home(request):
    return render(request,"my_projects/home.html",context={
        "my_projects" : projects,
    })


def project(request,id):
    name = ''
    project_details = ''
    for pro in projects:
        if(pro['id'] == id):
            project_details = pro
            name = pro['name']
    return render(request,"my_projects/project.html",context = {
                                            "project_name" : name,
                                            "project_details" : project_details
                                                        })        

