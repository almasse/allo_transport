from django.conf.urls import url
from . import views


urlpatterns = [
	#url(r'activite-feed/$', ActiviteFeed()),
	#url(r'event-feed/$', EventFeed()),
    #url(r'ajouter/$', views.ajouter_activite, name='ajouter_activite'),

    url(r'menu/$', views.get_menu, name='get_menu'),


]
