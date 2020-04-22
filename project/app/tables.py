# import django_tables2 as tables
#
# from .models import Product
# # from .models import OrderItem, Order
# class ProductTable(tables.Table):
#     #tag_final_value = tables.Column(orderable=False, verbose_name='Price')
#     action = tables.TemplateColumn(
#         '<button class="btn btn-info add_button" data-href="{% url "ajax_add" %}">Add!</a>'
#     )
#
#     class Meta:
#         model = Product
#         template_name = 'django_tables2/bootstrap.html'
#         fields = ['title', 'category','country','city', 'url']