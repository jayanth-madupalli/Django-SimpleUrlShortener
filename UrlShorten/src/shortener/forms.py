from django import forms
from .validators import validate_url

class SubUrlForm(forms.Form):
    url = forms.CharField(
        label='Submit Url',
        validators=[validate_url],
        widget = forms.TextInput(
            attrs={
                "placeholder":"Your Long Url",
                "class":"form-control",
            }
        )    
    )

    """ 
    def clean_url(self):
        url=self.cleaned_data['url']
        if not "com" in url:
            raise forms.ValidationError("This is not a valid url")
        return url 
    
    def clean(self):
        cleaned_data = super(SubUrlForm, self).clean()
        url = cleaned_data.get('url')
        print(url)
    """