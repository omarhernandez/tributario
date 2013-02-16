from apps.register.forms import create_form_register
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse


def  registro_view(request):


	create_register_user =  create_form_register()


	ctx = {

			'form_register' : create_register_user ,

		  }
	
	return render_to_response('register.html',ctx,  context_instance = RequestContext(request)  )



# ----------------------------------------------------------------------------------------------------------


def validate_register_form(request):
	
	if request.method == "POST":

		create_register_user = create_form_register(request.POST)

		if create_register_user.is_valid(): 
			
		#Si es validando
			create_register_user.save()

			return httpResponseRedirect('/')

		else:
		#No es valido los datos

			create_register_user = create_form_register();

			return render_to_response('register.html',{'register_form' : create_register_user  } ,context_instance = RequestContext(request))


