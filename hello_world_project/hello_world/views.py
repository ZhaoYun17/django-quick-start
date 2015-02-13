from django.template import Context, loader
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse

def index(request): # Take request from a user
	return HttpResponse('<html><body>Hello, World!</body></html>') # instantiate this response

def about(request):
	return HttpResponse(
    "Here is the About Page. Want to return home? <a href='/'>Back Home</a"
)

def better(request):
    t = loader.get_template('betterhello.html')
    c = Context({'current_time': datetime.now(), })
    return HttpResponse(t.render(c))