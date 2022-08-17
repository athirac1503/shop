from django.urls import path
from. import views

urlpatterns=[
        path('user_login',views.user_login,name='user_login'),
        path('sign_up',views.sign_up,name='sign_up'),
        path('add_product',views.add_product,name='add_product'),
        path('billing',views.billing,name='billing'),
        path('bill/<int:id>',views.bill,name='bill'),



       
]