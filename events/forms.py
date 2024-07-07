from django import forms

from events.models import Idea


class CreateIdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = (
            "title",
            "overview",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Idea Title'
        })
        self.fields['overview'].widget = forms.Textarea(attrs={
           'class': 'form-control',
           'placeholder': 'Idea Overview'
        })
