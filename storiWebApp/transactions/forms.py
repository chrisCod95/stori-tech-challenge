from django import forms


class SummaryEmailForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField()
    csv_file = forms.FileField()
