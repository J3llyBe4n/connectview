from django.shortcuts import render
from .models import Country

def pp_v(request):
	posts = Country.objects.all()
	print(posts)
	return render(request, 'index.html',{"posts": posts})