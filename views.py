from django.http import HttpResponse
import datetime


def hello(request):
	return HttpResponse("Hello World")


def show_Time(request):
	now = datetime.datetime.now()
	html = "<html><body> 现在的时间是: %s.</body></html>" % now
	return HttpResponse(html)
