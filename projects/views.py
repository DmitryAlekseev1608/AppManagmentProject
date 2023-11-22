from django.shortcuts import render
from projects.models import *
from projects.form import *
from django_tables2 import RequestConfig

# Create your views here.
def ChooseProject(request):
    return render(request, 'projects/ChooseProject.html')

def TablesReport(request):
    queryset = Projects.objects.all()
    table = SimpleTable(queryset)
    RequestConfig(request).configure(table)
    return render(request, 'projects/TablesReport.html', {'table': table})
