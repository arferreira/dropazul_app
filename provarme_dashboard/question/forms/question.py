from django import forms
from django.forms import inlineformset_factory
from mptt.forms import TreeNodeChoiceField

from provarme_dashboard.question.models import Question, Alternative, Category


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        #fields = '__all__'
        exclude = ('exam',)

        widgets = {
            'wording': forms.Textarea(
                attrs={
                    'class': 'form-control summernote',
                    'rows': '3'
                }
            ),
            'categories': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'tags': forms.SelectMultiple(
                attrs={
                    'class': 'form-control select2'
                }
            ),
            'hint': forms.Textarea(
                attrs={
                    'id': 'hint',
                    'class': 'form-control summernote',
                    'rows': '3'
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control summernote',
                    'rows': '3'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        try:
            self.fields['tags'].empty_label = None
            self.fields['category'].empty_label = None
        except:
            pass

QuestionAlternativesFormSet = inlineformset_factory(
    Question,
    Alternative,
    form=QuestionForm,
    extra=1,
    widgets={
        'text': forms.Textarea(
            attrs={'class': 'form-control autosize', 'rows': '1'})
    })
