from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import NameForm
from django.views.decorators.csrf import ensure_csrf_cookie
import logging
from django.core.files.storage import FileSystemStorage
from .models import Member
from .forms import NameForm
from . import id_management 
import os

logger = logging.getLogger('logger')

def homepage(request):
    items = Member.objects.all()
    logger.info(items[12].image_path)
    return render(request, '1.html', {'items': items})

def additem(request):
    template = loader.get_template('2.html')
    return HttpResponse(template.render()) 


def update_db(request):

    # if this is a POST request we need to process the form data
    if request.method == "POST":

        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST, request.FILES)

        
        
        if form.is_valid():

            BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #get base path
            Media_DIR = os.path.join(BASE_DIR, "media") #get media directory path

            logger.info(Media_DIR)
            item_name = form.cleaned_data["item_name"]
            link  = form.cleaned_data["link"]
            price = form.cleaned_data["price"]
            image_path = form.cleaned_data["image"]
            item_id = id_management.give_smallest_free_id() #get free id from id_management.py

            
            image = request.FILES.get('image')
            media_path = os.path.join(Media_DIR, str(item_id)) #craft path for id directory
            image_path = os.path.join(Media_DIR, str(image_path)) #craft path for saved picture
            image_path = image_path.replace(" ", "")
            logger.info(image_path)
            logger.info(media_path)
            os.mkdir(media_path)
            
            if image:
                image_name = image.name
                image_name = image_name.replace(" ","")
                fs = FileSystemStorage(location=media_path)
                fs.save(image_name, image)  # Save image to the media folder

            Member.objects.create(item_name=item_name, link=link, price=price, image_path=image_path, item_id=item_id)
            return HttpResponseRedirect("/additem?success=true") #redirect back to orginal page but keep flag set to create popup
    else:
        logger.info(form.errors)
    return render(request, '1.html', {'form': form}) 