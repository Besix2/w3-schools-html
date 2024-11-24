from mysite.additem.models import Member

members = Member.objects.all()
for member in members:
    print(member.titel, member.link, member.price)