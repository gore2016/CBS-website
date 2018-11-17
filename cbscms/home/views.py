from django.shortcuts import render

def contact(request):
	return render(request, 'home/contact.html')
