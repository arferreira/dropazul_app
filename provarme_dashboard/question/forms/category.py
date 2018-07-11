from django import forms
from mptt.forms import TreeNodeChoiceField
from provarme_dashboard.question.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['description', 'parent']

        widgets = {
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
					'maxlength': '100'

                }
            ),
            'parent': forms.Select(
                attrs={
                    'class': 'form-control select2'
                }
            ),
        }
