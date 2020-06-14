from django.shortcuts import render, redirect
from .forms import CreateNewList
from .models import ExpirationList
from django.utils import timezone


# Create your views here.
def index(request):
    context = {}
    return render(request, 'expiration_list/index.html', context)


def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ExpirationList(name=n)
            t.save()
            request.user.expirationlist.add(t)
            return redirect("/")
    else:
        form = CreateNewList()

    return render(request, "expiration_list/create.html", {"form": form})


def lists(request, id):
    ls = ExpirationList.objects.get(id=id)
    if not request.user.is_authenticated or ls not in request.user.expirationlist.all():
        return redirect("/")

    if request.method == "POST":
        if request.POST.get("newItem"):
            txt = request.POST.get("new")

            if len(txt) > 0 and request.POST.get("date"):
                date = request.POST.get("date")

                ls.item_set.create(text=txt, good=True, date_bought=str(timezone.now().date()),
                                   date_expired=date, days_left=0)
            else:
                print("invalid")

            return redirect("/" + str(id) + "#list_view")

        elif request.POST.get("deleteList"):
            ls.delete()
            return redirect("/")

    # Update the condition of all items in current list
    for i in ls.item_set.all():
        if timezone.now() >= i.date_expired:
            i.good = False

        # Calculate how many days left before expired
        delta = i.date_expired - timezone.now()
        hours = (delta.total_seconds() - (delta.days * 24 * 60 * 60)) / 3600

        if delta.days > 0:
            i.days_left = ("%d day(s) and %d hours" % (delta.days, hours))

        elif delta.total_seconds() > 0:
            i.days_left = ("%d hours" % hours)

        else:
            i.days_left = "----------"

        # Save item changes
        i.save()

    context = {"ls": ls}
    return render(request, "expiration_list/lists.html", context)


def delete(request, id, itemId):
    ls = ExpirationList.objects.get(id=id)
    ls.item_set.get(id=itemId).delete()
    return redirect("/" + str(id) + "#list_view")
