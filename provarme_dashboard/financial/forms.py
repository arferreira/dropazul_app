from django import forms

from provarme_dashboard.financial.models import Category, Expense


class ExpenseForm(forms.ModelForm):

    total = forms.DecimalField(label='Valor', localize=True, max_digits=10, decimal_places=2,
                               widget=forms.TextInput(attrs={'class': 'money form-control'}))

    class Meta:
        model = Expense
        fields = ['name', 'account', 'category', 'maturity', 'total', 'emission_date', 'settle']

    def __init__(self, *args, **kwargs):
        category_type = kwargs.pop('category_type', None)
        super(ExpenseForm, self).__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.filter(type_categories__in=[category_type, Category.ALL])
