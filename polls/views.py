from django.shortcuts import redirect, render
from polls.models import db_models

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        query = request.POST['query']
        db_models(name = name, email = email, query = query).save()
        return redirect("/")
    return render(request, "index.html")

def show(request):
    form = db_models.objects.all()
    return render(request, 'show.html', {'form':form})