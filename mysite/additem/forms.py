from django import forms


class NameForm(forms.Form):
    item_name = forms.CharField(label="item_name", max_length=100)
    link  = forms.CharField(label="link", max_length=50)
    price = forms.DecimalField(label="price", max_digits=5, decimal_places=2)