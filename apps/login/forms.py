from django import forms

class  login_view(forms.Form):
 
 	


	def clean(self):
		return self.cleaned_data