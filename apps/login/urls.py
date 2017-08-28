from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', (views.index)),
    url(r'^register$', (views.register)),
    url(r'^logout$', (views.logout)),
    url(r'^login$', (views.login)),
    url(r'^dashboard$', (views.dashboard)),
    url(r'^add/$', (views.add)),
    url(r'^add_item$', (views.add_item)),
    url(r'^add_wishlist/(?P<item_id>\d+)$', (views.add_wishlist)),   
    url(r'^delete/(?P<item_id>\d+)$', (views.delete)),
    url(r'^remove/(?P<item_id>\d+)$', (views.remove)),
    url(r'^description/(?P<item_id>\d+)$', (views.description)),
]