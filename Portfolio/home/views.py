from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpRequest

# Create your views here.

def home(request):
    return render(request, 'home/index.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message']
            }
            message = "\n".join(body.values())

        try:
            send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
        except BadHeaderError:
            return HttpRequest('Invalid header found.')
        return redirect('home/index.html')
    form = ContactForm()
    return render(request, 'home/contact.html', {'form':form})