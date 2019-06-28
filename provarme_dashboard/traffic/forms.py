from django import forms

from provarme_dashboard.traffic.models import Traffic


class TrafficForm(forms.ModelForm):

    investment = forms.DecimalField(label='Investimento (R$)', localize=True, max_digits=10, decimal_places=2,
                                    widget=forms.TextInput(attrs={'class': 'money form-control'}))

    class Meta:
        model = Traffic
        fields = ['product', 'event_date', 'investment', 'order_quantity']
