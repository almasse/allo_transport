from django.shortcuts import render
from models import *

def get_menu(request):
	return render(request,"menu.html")