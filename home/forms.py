from django import forms
from .models import SubmitModel
from django.forms import widgets, FileInput



class MainForm(forms.ModelForm):


	class Meta:
		model = SubmitModel
		fields = '__all__'

		widgets = {
			'pic': FileInput(attrs={'image': 'image'})

		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for i in self.fields:

			self.fields[i].widget.attrs['class'] = 'form-control'
		
		self.fields['sire'].required = False
		self.fields['dam'].required = False
		self.fields['sex'].required = False
		
		


