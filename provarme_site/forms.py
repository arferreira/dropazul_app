from django import forms

from provarme_dashboard.products.models import Devolution

class DevolutionForm(forms.ModelForm):

    class Meta:
        model = Devolution
        fields = '__all__'