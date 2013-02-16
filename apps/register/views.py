from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse


def  registro_view(request):


	create_register_user =  UserCreationForm(request.POST)


	ctx = {

			'form_register' : create_register_user ,

		  }
	
	return render_to_response('inicio/inicio.html',ctx,  context_instance = RequestContext(request)  )



# ----------------------------------------------------------------------------------------------------------


def validate_register_form(request):
	
	if request.method == "POST":

		create_register_user = UserCreationForm(request.POST)

		if create_register_user.is_valid(): 
		#Si es validando

			create_register_user.save()

			return httpResponseRedirect('/')

		else:
		#No es valido los datos

			create_register_user = UserCreationForm();

			return render_to_response('register.html',{'register_form' : create_register_user  } ,context_instance = RequestContext(request))


