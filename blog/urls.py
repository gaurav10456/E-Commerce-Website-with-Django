from django.urls import path
from . import views 
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path('admin/', admin.site.urls),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("search", views.search, name="search"),
    path("signup", views.handleSignup, name="handleSignup"),
    path("login", views.handleLogin, name="handleLogin"),
    path("logout", views.handleLogout, name="handleLogout"),
    path("createblogpost", views.createblogpost, name="createblogpost"),
    path("blog", views.blog, name="blog"),
    path("add", views.add, name="add"),
    path("browse", views.browse, name="browse"),
    path("apply",views.apply,name="apply"),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





