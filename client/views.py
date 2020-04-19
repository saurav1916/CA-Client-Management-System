from django.shortcuts import render,redirect
from client.forms import addform
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from client.models import Clientinfo
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    pending=Clientinfo.objects.filter(income_taxreturn=False)
    return render(request,'home.html',{'pending':pending})



def add_Client(request):
        form=addform()
        if request.method == "POST":
            form=addform(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/home/')
    
        return render(request,'addclient.html',{'acd':form})


def view_client(request):
    name=Clientinfo.objects.all()
    return render(request,'viewclients.html',{'list':name})   

def client_detail(request):
    name1=Clientinfo.objects.filter(id=request.GET['id']).all().values()
    return render(request,'list.html',{'list1':name1})


def update_itr(request):
        file=request.FILES["myfile"]
        FileSystemStorage().save(file.name,file)
        file_update=Clientinfo.objects.filter(name=request.GET['name']).update(Return=request.FILES['myfile'])
        itr_update=Clientinfo.objects.filter(name=request.GET['name']).update(income_taxreturn=True)    
        return HttpResponseRedirect("/home/")
        

def delete_client(request):
    Clientinfo.objects.filter(name=request.GET['name']).delete()  
    return HttpResponseRedirect("/viewclient")


def edit_client(request):
    detail=Clientinfo.objects.get(id=request.GET['id'])
    id=request.GET['id']
    form= addform(instance=detail)
    if request.method == "POST":
        form=addform(request.POST,request.FILES,instance=detail)
        if form.is_valid():
            form.save()
            return redirect("/clientdetail/?id=" +str(id))
    return render(request,'addclient.html',{"acd":form})
        
