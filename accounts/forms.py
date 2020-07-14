from django.forms import ModelForm
from .models import AddProductModel, PlaceOrderModel
# from .models import PlaceOrderModel


class AddProductForm(ModelForm):
    class Meta:
        model = AddProductModel
        fields = '__all__'



class updateStatusForm(ModelForm):
    class Meta:
        model = PlaceOrderModel
        fields = ('product_status',)

