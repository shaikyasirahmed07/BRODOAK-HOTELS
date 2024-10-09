from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('check_booking/' , check_booking),
    path('', home , name='home'),
    path('login.html/', login_page , name='home'),
    path('Contact.html/', contact , name='home'),
    path('About.html/', about , name='home'),
    path('login.html/signup.html/', signup , name='home'),
    path('login.html/signup.html/login.html/', login_page , name=''),
    path('login.html/signup.html/login.html/signup.html', signup , name='home'),
    path('hotel-detail/<uid>/', hotel_detail, name="hotel_detail"),
    path('login/', login_page, name='login_page'),
    path('home.html', home, name='register_page'),
    path('register/', register_page , name='register_page'),
    path('register/home.html', home, name='register_page'),
    path('register/About.html', about, name='register_page'),
    path('register/Contact.html', contact, name='register_page'),
    path('register/login.html', login_page , name='home'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()