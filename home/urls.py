from django.contrib import admin 
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
           path("forms.html",views.forms,name="forms"),
    path("uploadCoin",views.uploadCoin,name="uploadCoin"),
    path("displayall",views.displayall,name="displayall"),
    path("searching",views.searching,name="searching"),
   path('',views.displayall,name="displayall"
        ),
 path('admin/', admin.site.urls),

]