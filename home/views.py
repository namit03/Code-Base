from django.shortcuts import render,redirect
from django.contrib import messages
from home.forms import StudentEditModelForm
from home.forms import StudentCreateForm

# Create your views here.
from home.forms import StudentSearchForm
from home.models import Student

def home_view(request):
       # del request.session['id']
        if request.method =="POST":
                        search=StudentSearchForm(request.POST)
                        if search.is_valid():
                                value = search.cleaned_data.get('q')
                                result = Student.objects.filter(student_name__contains=value)
                                return render(request,'delete.html',
                                {'result':result})
        else:
                form=StudentSearchForm()
                result=Student.objects.all()
                return render(request,'delete.html',{'form':form})

def deletestudent(request,id):
    result=Student.objects.get(id=id)
    result.delete()
    messages.success(request,'Deleted Successfully!!')
    return redirect('/') 

def editstudent(request,id):
        student=Student.objects.get(id=id)
        if request.method=='POST':
                request.session['id']=id
                print("request.session['id']",request.session['id'])
                modelform=StudentEditModelForm(request.POST,instance=student)
                if modelform.is_valid():
                        modelform.save()
                        return redirect('/')
        else:
                modelform =StudentEditModelForm(instance=student)
                return render(request,'edit.html',{'form':modelform})

def createstudent(request):
        if request.method=="POST":
                form=StudentCreateForm(request.POST)
                if form.is_valid():
                        student=Student.objects.create(student_name=form.cleaned_data.get('student_name'),department=form.cleaned_data.get('department'))
                        student.save()
                        messages.success(request,'Created Successfully!!')
                        return redirect('/')
        else:
                form=StudentCreateForm()
                return render(request,'create.html',{'form':form})                                       



    # form=StudentSearchForm()
    # msg="hello form from django"
    # context={'form':form,'msg':msg}
    # return render(request,'home.html',context)

def about(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'home.html')