from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import NameForm
from django.views.decorators.csrf import ensure_csrf_cookie
import logging
from .models import Member
from .forms import NameForm

logger = logging.getLogger(__name__)

def homepage(request):
    template = loader.get_template('1.html')
    return HttpResponse(template.render())

def additem(request):
    template = loader.get_template('2.html')
    logger.info("test")
    return HttpResponse(template.render()) 


def update_db(request):
    logger.info("test2")
    # if this is a POST request we need to process the form data
    form = NameForm(request.POST)
    if request.method == "POST":
        logger.info("test2")
        # create a form instance and populate it with data from the request:
        logger.info(form)
        
        if form.is_valid():
            logger.info("test3")
            item_name = form.cleaned_data["item_name"]
            link  = form.cleaned_data["link"]
            price = form.cleaned_data["price"]
            Member.objects.create(item_name=item_name, link=link, price=price)
            return HttpResponseRedirect("additem")
    else:
        print(form.errors)
    return render(request, '1.html', {'form': form})