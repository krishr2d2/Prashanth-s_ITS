from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .models import *
from .forms import *


# Create your views here.
def index(request):

	template = 'website/index.html'
	points = set(data.objects.all())
	return render(request, template, {'points': points})


def news(request):
	return render(request, 'website/news.html', {})


def contact(request):
	return render(request, 'website/contact.html', {})



def redirect(request, lat, lng):
	
	Data = data.objects.filter(latitude=lat).filter(longitude=lng)
	return render(request, 'website/show_data.html', {'data': Data, 'lat': lat, 'lng': lng})
	

def show_data(request):
	return render(request, 'website/show_data.html', {})



class insert(FormView):

	template_name = 'website/insert.html'
	form_class = insert_form
	

	def get(self, request, *args, **kwargs):
		form = self.form_class(None)
		context = {
			'form' : form
		}

		return render(request, self.template_name, context)


	def post(self, request, **kwargs):

		form = insert_form(request.POST)
		context = {'form' : self.form_class(None)}

		if form.is_valid():

			if request.POST['latitude'] < 0:
				context["error_message"] = "Invalid latitude"
			if request.POST['longitude'] < 0:
				context["error_message"] = "Invalid longitude"
			if request.POST['temperature'] < 0:
				context["error_message"] = "Invalid temperature"
			if request.POST['humidity'] < 0:
				context["error_message"] = "Invalid humidity"
			if request.POST['co2'] < 0:
				context["error_message"] = "Invalid Co2"
			if request.POST['smoke'] < 0:
				context["error_message"] = "Invalid smoke"

			D = data()
			D.latitude = float(request.POST['latitude'])
			D.longitude = float(request.POST['longitude'])
			D.temperature = request.POST['temperature']
			D.humidity = request.POST['humidity']
			D.co2 = request.POST['co2']
			D.smoke = request.POST['smoke']
			D.save()

			context["message"] = "Data Inserted !!"

			return render(request, self.template_name, context)

		return render(request, self.template_name, {'form' : self.form_class(None)})



def current_data(request, lat, lng, temp, humid, carbon, smo):

	current = data(
			latitude = lat,
			longitude = lng,
			temperature = temp,
			humidity = humid,
			co2 = carbon,
			smoke = smo,
		)
	current.save()
	return HttpResponse("insertd")