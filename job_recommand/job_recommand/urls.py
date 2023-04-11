from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('job_recommand_app.urls'))
    # path("", views.test),
]
