from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm

#Don't Repeat Yourself = DRY


def home_page(request):
    context = {"title": "Home page", "list": [1,3, 4,6,7]}
    return render(request, 'home.html', context)


def about_page(request):
    return render(request, "about_page.html", {"title":"About Us page"})


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form = ContactForm()
    context = {"title": "Contact page",
               "form": form
               }
    return render(request, "form.html", context)

def example_page(request):
    context     = {"title": "example"}
    templat_name = "about_page.xls"
    template_obj = get_template(templat_name)
    return HttpResponse(template_obj.render(context))