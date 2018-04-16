# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import time

def index(request):
	date_time = time.localtime(time.time()),
	month = {
		'1' : 'January',
		'2' : 'February',
		'3' : 'March',
		'4' : 'April',
		'5' : 'May',
		'6' : 'June',
		'7' : 'July',
		'8' : 'August',
		'9' : 'September',
		'10' : 'October',
		'11' : 'November',
		'12' : 'December'
	}
	context = {
		"time" : str(date_time[0][3]) +":"+str(date_time[0][4]),
		"date" : month[str(date_time[0][1])]+ " " + str(date_time[0][2]) + ", " + str(date_time[0][0])
	}
	return render(request, "time_app/index.html", context)
# Create your views here.
