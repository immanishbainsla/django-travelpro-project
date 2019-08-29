from django.views import generic
from django.contrib import messages
from django.shortcuts import render
from accounts.forms import UserContactForm

# Create your views here.

# Index View
class IndexView(generic.TemplateView):
    template_name = 'index.html'


# About View
class AboutView(generic.TemplateView):
    template_name = 'about.html'


# USER CONTACT VIEW
def ContactView(request):
    form = UserContactForm()
    if request.method == 'POST':
        form = UserContactForm(data = request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'We have recieved your Query. We will contact you soon. Thanks.')

        else:
            messages.error(request, 'Form in Invalid.')

    else:
        form = UserContactForm()

    return render(request, 'contact.html', context={'form':form})
