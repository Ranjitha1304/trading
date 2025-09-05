# mainapp/admin.py
from django.contrib import admin
from .models import HomePage
from .models import HowItWorksImage, DashboardImage
from .models import CommunityImage
from .models import AboutUsBanner, MissionSection, VisionSection
from .models import BlogBanner, BlogCategory, BlogPost, LoginImage


admin.site.register(HomePage)

admin.site.register(HowItWorksImage)
admin.site.register(DashboardImage)

admin.site.register(CommunityImage)


admin.site.register(AboutUsBanner)
admin.site.register(MissionSection)
admin.site.register(VisionSection)

admin.site.register(BlogBanner)
admin.site.register(BlogCategory)
admin.site.register(BlogPost)

admin.site.register(LoginImage)

