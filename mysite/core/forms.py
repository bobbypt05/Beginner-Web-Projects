from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.Form):
			
			Fusername = forms.CharField(max_length=50,
			widget = forms.TextInput(attrs={
				'placeholder':'Username',
			}))
	    	
			Ffirst_name = forms.CharField(max_length=30,
				widget = forms.TextInput(attrs={
					'placeholder':'First Name'
			}))

			Flast_name = forms.CharField(max_length=30,
				widget = forms.TextInput(attrs={
						'placeholder':'Last Name'
			}))

			Femail = forms.EmailField(max_length=30,
				widget = forms.TextInput(attrs={
						'placeholder':'Email'
			}))

			Fpassword1 = forms.CharField(max_length=30,
				widget = forms.TextInput(attrs={
						'placeholder':'Password'
			}))

			Fpassword2 = forms.CharField(max_length=30,
				widget = forms.TextInput(attrs={
						'placeholder':'Confirm Password'
					})
				)
	    