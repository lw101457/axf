from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^base/$',views.base,name='base'),
    url(r'^home/$',views.home,name='home'),
    url(r'^market/$',views.market,name='market'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^mine/$',views.mine,name='mine')
]