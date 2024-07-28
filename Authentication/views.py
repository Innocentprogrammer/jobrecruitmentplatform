from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from NextGen_Teche import settings
# from django.core.mail import send_mail, EmailMessage
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes,force_text
# from .tokens import generate_token


# Create your views here.
def home(request):
    return render(request,"Authentication/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username):
            messages.error(request,"Username is already exist! Please try some other username")
            return redirect('/')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email is already registered!")
            return redirect('/')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')
        
        if password1 != password2:
            messages.error(request, "Password didn't match")
            return redirect('/')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!")
            return redirect('/')

        myuser = User.objects.create_user(username,email,password1)
        myuser.first_name=fname
        myuser.last_name=lname

        # myuser.is_active=False

        myuser.save()

        messages.success(request,"Your Account has been Successfull Created.")

        # welcome Email

        # subject = "Welcome to NextGen Teche"
        # message = "Hello "+ myuser.first_name + "!! \n "+ "Welcome to NextGen Teche \n Thank you for visiting our website. \n We have also send you a confirmation email, Please your email address in order to activate you account. \n\n Thanking You \n Mratyunjay Saxena \n (Founder)"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email

        # current_site=get_current_site(request)
        # email_subject="Confirm Your Email NextGen Teche"
        # message2= render_to_string('email_confirmation.html',{ 
        #     'name' :myuser.first_name,
        #     'domain':current_site.domain,
        #     'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token':generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()


        return redirect('signin')

    return render(request, "Authentication/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username,password=password1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,"index.html",{'fname':fname})

        else:
            messages.error(request,"Bad Credentials")
            return redirect('/')


    return render(request, "Authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect('/')

# def activate(request, uidb64, token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except(TypeError,ValueError,OverflowError,User.DoesNotExist):
#         myuser=None
#     if myuser is not None and generate_token.check_token(myuser, token):
#         myuser.is_active = True
#         myuser.save()
#         login(request, myuser)
#         return redirect('home')
#     else:
#         return render(request, 'activation_failed.html')