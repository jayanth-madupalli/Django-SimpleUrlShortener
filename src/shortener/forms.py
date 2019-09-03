from django import forms
from .validators import validate_url

class SubUrlForm(forms.Form):
    url = forms.CharField(
        label = 'Submit URL',
        validators = [validate_url],
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Your Long URL here",
                "style": "height:70px",
            }
        )
    )