from django.shortcuts import render, redirect
from .forms import CreateNewList
from .models import ExpirationList


# Create your views here.
def index(request):
    context = {}
    return render(request, 'expiration_list/index.html', context)


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        print(form.errors)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ExpirationList(name=n)
            t.save()
            return redirect("/")
    else:
        form = CreateNewList()

    return render(response, "expiration_list/create.html", {"form": form})
