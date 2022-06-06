from django.shortcuts import render

# Create your views here.
def moves(request):
    return render(request,'index.html')