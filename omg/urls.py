from django.conf.urls import url, include
from django.contrib import admin
from omg import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index$', views.index),
    url(r'^show_topic$',views.show_topic),
    url(r'^add_topic1$',views.add_topic1),
    url(r'^edit_topic$',views.edit_topic),

    url(r'^testform',views.testform),
    url(r'^testfile',views.testfile),
]