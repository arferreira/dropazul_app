from django import forms

from provarme_dashboard.question.models import Tag


class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = '__all__'
		widgets = {
			'description': forms.TextInput(
				attrs= {
					'class': 'form-control',
					'maxlength': '200'
				}
			),
			'tag': forms.TextInput(
				attrs= {
					'class': 'form-control'
				}
			),
		}
