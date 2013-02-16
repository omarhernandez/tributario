#encoding:utf-8
from django.conf.urls.defaults import patterns,url

#creamos nueva rama de urls

urlpatterns = patterns('apps.register.views',  #Init View
 

			url(r'registro/$' ,    'registro_view' ,  name = 'vista_registro') , 

			  

			)