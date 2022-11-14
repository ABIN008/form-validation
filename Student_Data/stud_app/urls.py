from django.urls import path

from stud_app import views

urlpatterns = [
    path('', views.StudentView.as_view(), name="add_details"),
    path('list/', views.StudentListView.as_view(), name="details_list"),
    path('update/<id>/', views.StudentUpdateView.as_view(), name="update_student"),
]