from django.shortcuts import render

from apps.models import Project


# Create your views here.
def index_1(request):
    Contacts = Project.objects.all()
    context = {
        'Contacts': Contacts
    }
    return render(request, 'apps/index.html', context)