# from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings 
from articles import views as article_views

urlpatterns = [
    # url(r'^about/$',views.about),
    # url(r'^$', views.homepage)
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('articles/', include('articles.urls')),
    path('about', views.about),
    path('',  article_views.article_list, name="home"),
    path('home/', article_views.article_list, name="home")

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
