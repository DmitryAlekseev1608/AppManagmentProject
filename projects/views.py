from django.shortcuts import render

# Create your views here.
def ChooseProject(request):
    return render(request, 'projects/ChooseProject.html')

def TablesReport(request):
    return render(request, 'projects/TablesReport.html')

