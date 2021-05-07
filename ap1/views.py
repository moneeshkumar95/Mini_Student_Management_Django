from django.shortcuts import render, redirect
from .forms import *
from . models import *
from .serializers import *
from rest_framework.decorators import api_view

#to redirect
def home(request):
    return redirect("list")

#show list of students
@api_view(['GET','POST'])
def liststudent(request):
    queryset = Student.objects.all()
    serializer = StudentSerializers(queryset, many=True)
    if request.POST:
        form = Create_Student(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            return render(request,'api_list.html',{"items":serializer.data, "form":form})
    else:
        form = Create_Student()
        return render(request,'api_list.html',{"items":serializer.data, "form":form})

#update the student details
@api_view(['GET','POST'])
def updatestud(request, rn):
    rol_no = Student.objects.get(roll_no=rn)
    form = Create_Student(instance=rol_no)

    if request.method == "POST":
        form = Create_Student(request.POST, instance=rol_no)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            return redirect("apiupdate_student")
    else:
        return render(request, 'api_update_student.html',{'form':form})

#create marks
@api_view(['GET','POST'])
def marks(request):
    items = Add_Mark.objects.all()
    if request.method == "POST":
        form = Add_m(request.POST)
        if form.is_valid():
            form.save()
            return redirect("apiadd_mark")
        else:
            return render(request, "api_add_mark.html", {"items": items, 'form': form})
    else:
        form = Add_m()
        return render(request, "api_add_mark.html", {"items": items, 'form': form})

#update student marks
@api_view(['GET','POST'])
def updatemarks(request, pk):
    idt = Add_Mark.objects.get(id=pk)
    form = Add_m(instance=idt)

    if request.method == "POST":
        form = Add_m(request.POST, instance=idt)
        if form.is_valid():
            form.save()
            return redirect("apiadd_mark")
        else:
            return render(request, "api_update_mark.html", {'form': form})
    else:
        return render(request, "api_update_mark.html", {'form': form})