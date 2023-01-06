from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'First Name', 'class':'input_text'}),max_length=50, label='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'Last Name', 'class':'input_text'}),max_length=50, label='')
    email_address = forms.EmailField(widget=forms.TextInput(attrs={ 'placeholder':'Email', 'class':'input_text'}), max_length = 150, label='')
    message = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder':'Send me a message', 'class':'message_text'}), max_length=2500, label='')