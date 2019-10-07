from django import forms


class ContactForm(forms.Form):
    full_name_ContactForm = forms.CharField()
    email_ContactForm = forms.EmailField()
    content_ContactForm = forms.CharField(widget=forms.Textarea)