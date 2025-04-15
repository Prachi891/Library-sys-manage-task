from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'bio']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('.com'):
            raise forms.ValidationError("Only .com emails are allowed.")
        return email
