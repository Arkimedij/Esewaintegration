from django.shortcuts import render
from .models import Card
# Create your views here.
def landingpage(request):
    cards = Card.objects.all()
    return render(request, 'base.html',{'cards':cards})