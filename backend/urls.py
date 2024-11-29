from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('api.urls')),
    path('api/user-student/', include('user_student.urls')),
    path('user-admin/', include('user_admin.urls')),
    path('user-teacher/', include('user_teacher.urls')),
    path('special-education/', include('special_education.urls')),
    path('api/user-parent/', include('user_parent.urls')), 

    # # Serve media files in both development and production
    # path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),

    #     # Serve static files
    # path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
    
    # # Serve React app - this should be last
    # re_path(r'^.*', TemplateView.as_view(template_name='index.html'), name='index'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path('static/<path:path>', serve, {'document_root': settings.STATIC_ROOT}),
        path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    ]

# This should always be last
urlpatterns += [
    re_path(r'^.*', TemplateView.as_view(template_name='index.html'), name='index'),
]