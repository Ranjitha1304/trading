from django.shortcuts import render

from .models import HomePage
from .models import CommunityImage, HowItWorksImage, DashboardImage


def index(request):
    homepage = HomePage.objects.first()  # get the latest entry
    how_it_works = HowItWorksImage.objects.first()
    dashboard = DashboardImage.objects.first()
    community_images = CommunityImage.objects.all()

    return render(
        request, "index.html", 
        {
            "homepage": homepage,
            "how_it_works": how_it_works, 
            "dashboard": dashboard,
            "community_images": community_images,
            }
        )

from django.shortcuts import render
from .models import AboutUsBanner, MissionSection, VisionSection

def about_us(request):
    banner = AboutUsBanner.objects.first()
    mission = MissionSection.objects.first()
    vision = VisionSection.objects.first()
    return render(request, "about_us.html", {
        "banner": banner,
        "mission": mission,
        "vision": vision,
    })

from .models import BlogBanner, BlogCategory, BlogPost

def blog_page(request):
    banner = BlogBanner.objects.first()
    categories = BlogCategory.objects.all()

    # Attach posts to each category
    for category in categories:
        category.posts_list = category.posts.all()

    return render(request, "blog.html", {
        "banner": banner,
        "categories": categories,
    })

# mainapp/views.py
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from .forms import PartnerForm

def partner(request):
    success_message = ""
    form = PartnerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            # Prepare email content to admin
            subject = "New Partner Request from website"
            message = (
                f"New partner form submitted:\n\n"
                f"Name: {data['name']}\n"
                f"Phone: {data['phone']}\n"
                f"Email: {data['email']}\n"
                f"City: {dict(form.fields['city'].choices).get(data['city'], data['city'])}\n"
                f"Pincode: {data['pincode']}\n\n"
                "Please contact the applicant."
            )
            admin_email = getattr(settings, "PARTNER_NOTIFICATION_EMAIL", None) or getattr(settings, "DEFAULT_FROM_EMAIL", None)
            try:
                if admin_email:
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        [admin_email],
                        fail_silently=False,
                    )
                # success feedback
                success_message = "Thanks for reaching us. We will contact you soon."
                # keep the form displayed (do not clear) — if you prefer to clear form add: form = PartnerForm()
            except BadHeaderError:
                form.add_error(None, "Invalid header found. Email not sent.")
            except Exception as e:
                # don't leak internal details
                form.add_error(None, "An error occurred sending email. Try again later.")
        # invalid -> errors available in form
    return render(request, "partner.html", {"form": form, "success_message": success_message})



# footer placeholder views
def trade_investor(request):
    return render(request, "placeholder.html", {"title": "Trade Investor"})

def market_explore(request):
    return render(request, "placeholder.html", {"title": "Market Explore"})

def ready_token(request):
    return render(request, "placeholder.html", {"title": "Ready Token"})

def main_option(request):
    return render(request, "placeholder.html", {"title": "Main Option"})

def file_checking(request):
    return render(request, "placeholder.html", {"title": "File Checking"})

def faqs(request):
    return render(request, "placeholder.html", {"title": "FAQ's"})

def docs(request):
    return render(request, "placeholder.html", {"title": "Docs"})

def press_kit(request):
    return render(request, "placeholder.html", {"title": "Press Kit"})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, LoginForm
from .models import LoginImage, UserProfile

def login_view(request):
    image = LoginImage.objects.first()
    error = ""
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data["email"].strip().lower()
            pwd = form.cleaned_data["password"]
            # find user by email
            try:
                user_obj = User.objects.get(email__iexact=email)
            except User.DoesNotExist:
                user_obj = None

            if user_obj:
                user = authenticate(request, username=user_obj.username, password=pwd)
                if user:
                    login(request, user)
                    return redirect("home")
            error = "Check your email and password."
    return render(request, "login.html", {"form": form, "image": image, "error": error})


def register_view(request):
    image = LoginImage.objects.first()
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"].strip()
            mobile = form.cleaned_data["mobile"].strip()
            email = form.cleaned_data["email"].strip().lower()
            password = form.cleaned_data["password1"]

            if User.objects.filter(email__iexact=email).exists():
                form.add_error("email", "Email already registered. Please login.")
            else:
                # use email as username
                username = email
                user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
                # create profile with mobile
                UserProfile.objects.create(user=user, mobile=mobile)
                messages.success(request, "Registered successfully. Please login.")
                return redirect("login")

    return render(request, "register.html", {"form": form, "image": image})
