from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
	return render(request, "first_app/index.html")

def new(request):
	response = "This will eventually display a new blog post"
	return HttpResponse(response)

def create(request):
	return redirect('/')

def show(request, number):
	response = "This will display blog " + number
	return HttpResponse(response)

def edit(request, number):
	response = "This will edit blog " + number
	return HttpResponse(response)

def delete(request, number):
	response = "This will delete blog " + number
	return HttpResponse(response)

