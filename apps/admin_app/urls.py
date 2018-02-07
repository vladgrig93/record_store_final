from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin_portal$', views.index),
    url(r'^logout$', views.logout),
    url(r'^edit_user/(?P<user_id>\d+)$', views.edit_user),
    url(r'^remove_user/(?P<user_id>\d+)$', views.remove_user),
    url(r'^remove_record/(?P<record_id>\d+)$', views.remove_record),
    url(r'^edit_record_page/(?P<record_id>\d+)$', views.edit_record_page),
    url(r'^edit_artist_page/(?P<artist_id>\d+)$', views.edit_artist_page),
    url(r'^order_page/(?P<order_id>\d+)$', views.order_page),
    url(r'^addrecord$', views.addrecord),
    url(r'^proccess_record$', views.proccess_record),
    url(r'^update_record/(?P<record_id>\d+)$', views.update_record),
    url(r'^update_user/(?P<user_id>\d+)$', views.update_user),
    url(r'^update_status/(?P<order_id>\d+)$', views.update_order),
    url(r'^update_artist/(?P<artist_id>\d+)$', views.update_artist),
    ]
    