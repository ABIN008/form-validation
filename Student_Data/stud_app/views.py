from django.shortcuts import redirect, render
from django.views import View
from stud_app.models import Student
from django.views.generic import View, ListView

from stud_app.forms import DetailForm


# Create your views here.

class StudentView(View):
    
    def get(self, request):
        form = DetailForm() 
        return render(request, "studform.html", {"form": form})
    
    def post(self, request):
        form = DetailForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return render(request, "list.html", {"data": instance})
        else:
            return render(request, "studform.html", {"form": form})

class StudentListView(ListView):
    template_name = "studentlist.html"
    context_object_name = "datas"
    queryset = Student.objects.all()

class StudentUpdateView(View):

    def get(self, request, id):
        form = DetailForm(instance=Student.objects.get(id=id))
        return render(request, "studform.html", {"form": form})
    
    def post(self, request, id):
        form = DetailForm(request.POST, instance=Student.objects.get(id=id))
        if form.is_valid():
            instance = form.save()
            return redirect("details_list")
        else:
            return render(request, "studform.html", {"form": form})
