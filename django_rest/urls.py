
from django.contrib import admin
from django.urls import path, include
from drapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # path('student-info/<int:pk>', views.student_information),
    # path('student_list/',views.student_list),
    # path('student_create/',views.student_create),
    path('student_update/',views.student_update),
]
