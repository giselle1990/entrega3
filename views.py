from django.shortcuts import redirect, render
from . import models
from . import forms 

def index(request):
    return render(request, "coder/index.html")

def deudor_list(request):
    consulta = models.Deudor.objects.all()
    contexto = {"deudor" : consulta}
    return render(request, "Coder/deudor_list.html, contexto")

def deudor_form(request):
    if request.method == "POST":
        form = forms.deudorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("deudor_list")
    else:
        form = forms.deudorform()
        return render(request, "coder/deudor_form.html", {"form":form}) 
    
    
    
    
    
    
    

