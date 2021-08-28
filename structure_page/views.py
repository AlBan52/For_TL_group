from django.shortcuts import render

def show_structure(request):
	return render(request, 'structure_page.html')
