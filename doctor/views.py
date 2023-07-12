from telnetlib import LOGOUT
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import Doctor,Patient,Appointment
def about(request):
    return render(request, "index.html")
def home(request):
    return render(request, "home.html")
def contact(request):
    return render(request, "contact.html")
def doctor(request):
    return render(request,"doctors.html")
def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctor=Doctor.objects.all()
    patient=Patient.objects.all()
    appointment=Appointment.objects.all()
    d=0
    p=0
    a=0
    for i in doctor:
        d=d+1
    for i in patient:
        p=p+1
    for i in appointment:
        a=a+1
    d1={'d':d,'p':p,'a':a}
    return render(request,"i2.html",d1)

# def Login(request):
#     error = ""
#     if request.method =="POST":
#         u=request.post['uname']
#         p=request.post['password']
#         user = authenticate(username=u ,password=p)
#         try:
#             if user.is_staff:
#                 Login(request,user)
#                 error ="NO"
#             else:
#                 error = "yes"
#         except:
#             error ="yes"
#     d={'error':error}
#    return render(request,'login.html',d)
#if user is not None:
# if user.is_staff:
   #             return redirect('home')  # Redirect to the home page after successful login
  #          else:
  #              error = "Invalid login credentials."
#        else:
 #           error = "Invalid username or password."
def Login(request,):
    error =""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error ="no"
            else:
                error = "yes"
        except:
            error ="yes"
    d={'error':error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('Login')
def View_Docter(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request, "view_doctor.html",d)
def Delete_Docter(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_Doctor')

def Add_doctor(request):
    error =""
    d = {'error': error}
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n= request.POST.get('name')
        m= request.POST.get('mobile')
        sp=request.POST.get('special')
        if m is not None:
            try:
                Doctor.objects.create(name=n,mobile=m,special=sp)
                error='no'
            except:
                error='yes'
        else:
            error = 'Missing mobile field'
        d={'error': error}
    return render(request, 'adddoctor.html', d)

def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat=Patient.objects.all()
    d={'pat':pat}
    return render(request, "view_patient.html",d)
    
def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient=Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def Add_patient(request):
    error =" "
    d = {'error': error}
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n= request.POST['name']
        g= request.POST['gender']
        m= request.POST['mobile']
        ad=request.POST['address']
        if m is not None:
            try:
                Patient.objects.create(name=n,gender=g,mobile=m,address=ad)
                error='no'
            except:
                error='yes'
        else:
            error = 'Missing mobile field'
        d={'error': error}
    return render(request, 'add_patient.html', d)

# def Add_Appointment(request,pk):
#     if request.method == 'POST':
#         doctor = get_object_or_404(Doctor,pk=pk)
#         patient_name = request.POST.get('patient')
#         date = request.POST.get('date')
#         time = request.POST.get('time')
        
#         # doctor = Doctor.objects.get(id=doctor_id)
        
#         appointment = Appointment.objects.create(doctor=doctor, patient=patient_name, date=date, time=time)
        
#         return redirect('view_appointment')
#     else:
#         doctors = Doctor.objects.all()
#         patinets=Patient.objects.all()
#         d={'doctor':doctors,'Patient':patinets}
#         return render(request,"add_appointment.html",d)


# def Add_Appointment(request):
#     error = ""
#     doctors = Doctor.objects.all()
#     patients = Patient.objects.all()
    
#     if not request.user.is_staff:
#         return redirect('login')
    
#     if request.method == "POST":
#         n = request.POST['doctor']
#         p = request.POST['patient']
#         da = request.POST['date']
#         t = request.POST['time']

#         doctor = Doctor.objects.filter(name=n).first()
#         patient = Patient.objects.filter(name=p).first()

#         if doctor and patient:
#             try:
#                 Appointment.objects.create(doctor=doctor, patient=patient, date=da, time=t)
#                 error = 'no'
#             except:
#                 error = 'An error occurred while creating the appointment.'
#         else:
#             error = 'Invalid doctor or patient.'

#     d = {'doctors': doctors, 'patients': patients, 'error': error}
#     return render(request, 'add_appointment.html', d)



def Add_Appointment(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()

    if request.method == 'POST':
        doctor_name = request.POST['doctor']
        patient_name = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']

        doctor = Doctor.objects.filter(name=doctor_name).first()
        patient = Patient.objects.filter(name=patient_name).first()

        if doctor and patient:
            appointment = Appointment.objects.create(doctor=doctor, date=date, time=time)
            appointment.patient.add(patient)
            return redirect('view_appointment')
        else:
            error = 'Invalid doctor or patient.'
            return render(request, 'add_appointment.html', {'doctors': doctors, 'patients': patients, 'error': error})

    return render(request, 'add_appointment.html', {'doctors': doctors, 'patients': patients})


# def View_Appointment(request):
#     if not request.user.is_staff:
#         return redirect('login')
#     at=Appointment.objects.all()
#     d={'at':at}
#     return render(request, "view_appointment.html",d)

def View_Appointment(request):
    appointments = Appointment.objects.all()
    return render(request, 'view_appointment.html', {'appointments': appointments})


def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment=Appointment.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')