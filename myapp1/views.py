from django.shortcuts import render,redirect
from .models import music,mark,box
from .forms import mymusic,mymark

def read(request):
    who=music.objects.all()
    return render(request,'index.html',{'who':who})


def create(request):
    if request.method=='POST':
       form=mymusic(request.POST)
       if form.is_valid():
          form.save()
          return redirect('/create')
    else:
        who=music.objects.all()
        has=music.objects.count()
        form=mymusic()
        return render(request,'home.html',{'form':form,'who':who,'has':has})


def new(request):
    tap=box.objects.all()
    return render(request,'new.html',{'tap':tap})

