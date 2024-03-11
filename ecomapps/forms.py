from django import forms
from .models import Product,Address
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__' 

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city', 'street', 'nearest_landmark']

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'city',
            'street',
            'nearest_landmark',
            Submit('submit', 'Submit', css_class='btn-success')
        )
class MyForm(forms.Form):
    name = forms.CharField(label='Name')
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', widget=forms.Textarea)