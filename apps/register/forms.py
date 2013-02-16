#encoding:utf-8
from django import forms
 
class  create_form_register (forms.Form):

	City = [('',  'Ciudad')]

	States = [('',  'Estado')]
	
 	Nombre = forms.CharField(label="", max_length=100 ,widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
 	
 	RFC = forms.CharField(label="" , widget = forms.TextInput(attrs={'placeholder':'RFC'}))
	
	TIPO_REGIMEN = [('',  'Tipo de Régimen '), ]+[(1 , 'Opcion 1')] + [(2 , 'Opcion 2')]

 
	key_combo=  forms.ChoiceField(label="",choices=TIPO_REGIMEN, widget=forms.Select(attrs={  'class' : 'select_input'  }))

	Ciudad =  forms.ChoiceField(label="",choices=City, widget=forms.Select(attrs={  'class' : 'select_input'  }))

	Estado = forms.ChoiceField(label="",choices=States, widget=forms.Select(attrs={  'class' : 'select_input'  }))
 
	#Nombre =  forms.ChoiceField(label="",choices=KEY_REMOTE_, widget=forms.Select(attrs={  'class' : 'select_input off_data key_rc'  }))

 
	def clean(self):
		return self.cleaned_data
 