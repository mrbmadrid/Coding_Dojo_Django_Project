# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random

# Create your views here.

def index(request):
	if not 'words' in request.session:
		request.session['words'] = 1
	else:
		request.session['words'] +=1

	request.session['word'] = ""
	for i in range (0,14):
		request.session['word'] += str(unichr(int(random.random()*26+65)))

	return render(request, "random_word/index.html")
def reset(request):
	request.session['words'] = 0

	return redirect(index)