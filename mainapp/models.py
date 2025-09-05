# mainapp/models.py
from django.db import models

class HomePage(models.Model):
    banner = models.ImageField(upload_to="home/")
    sub_banner = models.ImageField(upload_to="home/")

    def __str__(self):
        return "Homepage Images"



# mainapp/models.py
from django.db import models

class HowItWorksImage(models.Model):
    image = models.ImageField(upload_to="home/")

    class Meta:
        verbose_name = "How It Works Image"
        verbose_name_plural = "How It Works Images"

    def __str__(self):
        return "How It Works Image"


class DashboardImage(models.Model):
    image = models.ImageField(upload_to="home/")

    class Meta:
        verbose_name = "Dashboard Image"
        verbose_name_plural = "Dashboard Images"

    def __str__(self):
        return "Dashboard Image"



class CommunityImage(models.Model):
    image = models.ImageField(upload_to="community/")
    order = models.PositiveIntegerField(default=0)  # to control placement

    class Meta:
        verbose_name = "Community Image"
        verbose_name_plural = "Community Images"
        ordering = ["order"]

    def __str__(self):
        return f"Community Image {self.order}"


from django.db import models

class AboutUsBanner(models.Model):
    image = models.ImageField(upload_to="aboutus/banner/")
    alt_text = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return "About Us Banner"


class MissionSection(models.Model):
    image = models.ImageField(upload_to="aboutus/mission/")
    title = models.CharField(max_length=100, default="Our Mission")
    description = models.TextField()

    def __str__(self):
        return "Mission Section"


class VisionSection(models.Model):
    image = models.ImageField(upload_to="aboutus/vision/")
    title = models.CharField(max_length=100, default="Our Vision")
    description = models.TextField()

    def __str__(self):
        return "Vision Section"



from django.db import models

# Section 1 Banner
class BlogBanner(models.Model):
    heading_white = models.CharField(max_length=200, help_text="First heading line in white")
    heading_green = models.CharField(max_length=200, help_text="Second heading line in green")
    description = models.TextField(help_text="3 lines description. Use <br> for line breaks where needed.")
    image = models.ImageField(upload_to="blog/banner/")

    def __str__(self):
        return f"Blog Banner - {self.heading_white} {self.heading_green}"


# Categories for tabs
class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# Posts for each category
class BlogPost(models.Model):
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name="posts")
    title = models.TextField(help_text="Main title. Use <br> for line breaks if needed.")
    reading_time = models.CharField(max_length=50, help_text="Example: 5 Mins Read . 20 May 2025")
    image = models.ImageField(upload_to="blog/posts/")

    def __str__(self):
        return f"{self.category.name} - {self.title[:30]}"


from django.db import models
from django.contrib.auth.models import User

class LoginImage(models.Model):
    name = models.CharField(max_length=100, default="Auth Image")
    image = models.ImageField(upload_to="auth_images/")

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    mobile = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"profile: {self.user.email}"
