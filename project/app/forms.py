# from django import forms
#
# from .models import Product
#
#
# class BaseForm(forms.Form):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field_name, field in self.fields.items():
#             field.widget.attrs['class'] = 'form-control'
#
#
# class OrderCreateForm(BaseForm, forms.ModelForm):
#     date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#
#     class Meta:
#         model = Product
#         fields = ['date', 'title' ]
#
#
# # class OrderEditForm(BaseForm, forms.ModelForm):
# #
# #     class Meta:
# #         model = Order
# #         fields = ['date', 'title', 'discount', 'is_paid']