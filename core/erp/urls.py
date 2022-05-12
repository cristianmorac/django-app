from django.urls import path
#from core.erp.views import category_list
#funcion
#from core.erp.Views.Category.views import category_list
#clase
from core.erp.Views.Category.views import * 

app_name = 'erp'

urlpatterns = [
    #path('category/list/', category_list, name='category_list') funcion,
    #clase
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/list2/', category_list, name='category_list2'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
]