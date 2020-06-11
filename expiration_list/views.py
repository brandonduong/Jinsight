from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, 'expiration_list/index.html', context)

