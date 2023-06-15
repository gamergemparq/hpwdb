# pyright: reportMissingModuleSource=false
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Gitlog3
from .forms import CreateNewCommit
# Create your views here.


def index(response, id=None):
    if id:
        commit = Gitlog3.objects.get(id=id)
        form = CreateNewCommit(data=commit)
        print(form)
        return render(response, "hpwapp/commit-edit.html", {"form": form})
    else:
        commits = Gitlog3.objects.all()
        return render(response, "hpwapp/commits.html", {"commits": commits})


def home(response):
    return render(response, "hpwapp/home.html", {"name": "test"})


def create(response):
    if response.method == "POST":
        form = CreateNewCommit(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            dy = form.cleaned_data["day"]
            dt = form.cleaned_data["date"]
            t = form.cleaned_data["time"]
            m = form.cleaned_data["message"]
            g = Gitlog3(name=n, day=dy, date=dt, time=t, message=m)
            g.save()

        return HttpResponseRedirect("/%i" % g.id)
    else:
        form = CreateNewCommit()
    
    return render(response, "hpwapp/create.html", {"form": form})
