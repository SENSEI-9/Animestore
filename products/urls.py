from django.urls import path
from products import views

urlpatterns =[
    path('view',views.view,name='view'),
    path('add',views.add,name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete')
]