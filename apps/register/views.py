from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def register_user(request):
	
	if request.method == "POST"

		create_register_user = UserCreateForm(request.POST)

		if create_register_user.is_valid(): 
		#Si es validando

			create_register_user.save()

			return httpResponseRedirect('/')

		else:
		#No es valido los datos

			create_register_user = UserCreateForm();

			return render_to_response('register.html',{'register_form' : create_register_user  } ,context_instance = RequestContext(request))


