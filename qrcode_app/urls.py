
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

urlpatterns = [path('make_invite', views.make_invite, name='make_invite'),
               path('get_invite/<str:pk>/', views.get_invite, name='get_invite')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)