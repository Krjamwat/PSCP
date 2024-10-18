
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def creative(request):
    return render(request,"creative.html")
