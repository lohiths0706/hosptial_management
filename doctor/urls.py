from django.contrib import admin
from django.urls import path
from doctor.views import about, home, contact,Login,Logout_admin,index,View_Docter,Delete_Docter,Add_doctor,Delete_Patient,View_Patient,Add_patient,View_Appointment,Add_Appointment,Delete_Appointment,doctor
urlpatterns = [
    path('' , home, name='home'),
    path('about/' ,about,  name='about'),
    path('contact/',contact, name='contact'),
    path('admin_login/',Login, name='Login'),
    path('logout/',Logout_admin, name='Logout_admin'),
    path('i2/',index,name='index'),
    path('view_doctor/',View_Docter,name='view_Doctor'),
    path('add_docter/',Add_doctor,name='add_doctor'),
    path('delete_doctor(?P<int:pid>)/',Delete_Docter,name='delete_doctor'),
    path('view_patient/',View_Patient,name='view_patient'),
    path('add_patient/',Add_patient,name='add_patient'),
    path('delete_patient(?P<int:pid>)/',Delete_Patient,name='delete_patient'),
    path('view_appointment/',View_Appointment,name='view_appointment'),
    path('add_appointment/',Add_Appointment,name='add_appointment'),
    path('delete_appointment/<int:pid>/',Delete_Appointment,name='delete_appointment'),
    #path('delete_doctor/<int:pid>/', views.delete_doctor, name='delete_doctor'),
    path('doctor/',doctor,name='kanna')
    
]