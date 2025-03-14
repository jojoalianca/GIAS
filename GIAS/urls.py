from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from GIAS import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('publicApp.urls')),
    path('', include('main.urls')),
    path('utilizador/', include('users.urls')),
    path('Report/', include('report.urls')),
    path('ArquivoR/', include('ArquivoRelatoriu.urls')),
    path('login/', views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('dadus-custom/', include('custom.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)