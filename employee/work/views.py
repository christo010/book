from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import Empform,bookform,persform,studentform
from work.models import emp,bookdb,personal,studentdb


class Emp(View):
    def get(self,request):
        form=Empform()
        return render(request,"empl.html",{"form":form})
    def post(self,request):
        form=Empform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            emp.objects.create(**form.cleaned_data)
            return render(request,"empl.html",{"form":form})
        else:
            return render(request,"empl.html",{"form":form})
        
class book(View):
    def get(self,request):
        form=bookform()
        return render(request,"books.html",{"form":form})
    def post(self,request):
        form=bookform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            #bookdb.objects.create(**form.cleaned_data)#==orm query3
             #or use 
            form.save()#:method to add the data into database without using orm query.we ccan use this for only model form
            return render(request,"books.html",{"form":form})
        else:
            return render(request,"books.html",{"form":form})

class booklist(View):
    def get(self,request):
        qs=bookdb.objects.all()
        return render(request,"booklist.html",{"qs":qs})
class book_one(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=bookdb.objects.get(id=id)
        return render(request,"bookone.html",{"qs":qs})
class book_del(View):
    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=bookdb.objects.get(id=id).delete()
        return redirect('book-det')
    
class pdetail(View):
    def get(self,request):
        form=persform()
        return render(request,"person.html",{"form":form})
    def post(self,request):
        form=persform(request.POST)
        if form.is_valid():
            form.save()

            return render(request,"person.html",{"form":form})
        
class pdetailall(View):
    def get(self,reuest):
        lo=personal.objects.all()
        return render(reuest,"person.html",{"lo":lo})
    
class student(View):
    def get(self,request):
        form=studentform()
        return render(request,"student.html",{'form':form})
    def post(self,request):
        form=studentform(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return render(request,"student.html",{"form":form})
class studename(View):
    def get(self,request,**k):
        print(k)
        id=k.get('pk')
        da=studentdb.objects.get(id=id)
        return render(request,"studna.html",{'data':da})
        







        
