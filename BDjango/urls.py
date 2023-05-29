from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Registration.urls')),
    path('blog/', include('Blog.urls')),
]