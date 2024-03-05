
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

urlpatterns = [path('make_invite', views.make_invite, name='make_invite'),
               path('make_special_invite', views.make_special_invite, name='make_special_invite'),
               path('get_info', views.festival_detail, name='festival_detail'),
               path('get_invite', views.get_invite, name='get_invite'),
                path('students/<int:id>/', views.student_detail, name='student_detail'),
                path('guest1/<int:id>/', views.guest1_detail, name='guest1_detail'),
                path('guest2/<int:id>/', views.guest2_detail, name='guest2_detail'),
                 path('guests/<int:id>/', views.guests, name='guest_detail'),
                 path('upload', views.upload, name='upload'),
                path('save_dict_to_excel/', views.save_dict_to_excel, name='save_dict_to_excel'),
                path('query_about_0/', views.query_about_0, name='query_about_0')






]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)