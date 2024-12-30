
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from additem.models import Member   

members = Member.objects.all()
for member in members:
    print(member.item_name, member.link, member.price, member.image_path, member.item_id)