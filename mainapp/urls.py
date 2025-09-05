from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about_us, name="about_us"),
    path("blogs/", views.blog_page, name="blog_page"),
    path("become-a-partner/", views.partner, name="partner"),
    # footer pages / extras (placeholders)
    path("trade-investor/", views.trade_investor, name="trade_investor"),
    path("market-explore/", views.market_explore, name="market_explore"),
    path("ready-token/", views.ready_token, name="ready_token"),
    path("main-option/", views.main_option, name="main_option"),
    path("file-checking/", views.file_checking, name="file_checking"),
    path("faqs/", views.faqs, name="faqs"),
    path("docs/", views.docs, name="docs"),
    path("press-kit/", views.press_kit, name="press_kit"),
    
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),

]
