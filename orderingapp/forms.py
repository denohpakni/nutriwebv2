from django.forms import ModelForm, formset_factory
from .models import AddProduct, PlaceOrder
# from .models import PlaceOrderModel


class AddProductForm(ModelForm):
    class Meta:
        model = AddProduct
        fields = '__all__'


class updateStatusForm(ModelForm):
    class Meta:
        model = PlaceOrder
        fields = ('product_status',)

class OrderForm(ModelForm):
    class Meta:
        model = PlaceOrder
        fields = ('product_name','product_quantity')


OrdersFormSet = formset_factory(OrderForm, extra=3, can_delete=True)
