from django.shortcuts import render
from . models import stud
from django.db.models import Count
# Create your views here.

def student(request):
    if request.method=="POST":
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        age=request.POST.get('age')
        grade=request.POST.get('grade')
        address=request.POST.get('address')
        parent_occupation=request.POST.get('parent_occupation')
        student=stud(firstname=fname,lastname=lname,age=age,grade=grade,address=address,parent_occupation=parent_occupation)
        student.save()
        
    return render(request,'form.html')

def count(request):
    result = (stud.objects.values('grade').annotate(dcount=Count('grade')) .order_by())
    return render(request,'count.html',{'result':result})