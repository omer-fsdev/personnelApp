from django.urls import path, include
from .views import (
    DepartmentView,
    PersonnelView,
    PersonnelUpdateView,
    DepartmentPersonnelView,
    Custom,
)

urlpatterns = [
    path("department/", DepartmentView.as_view()),
    path("personnel/", PersonnelView.as_view()),
    path("personnel/<int:pk>", PersonnelUpdateView.as_view()),
    path("department_detail/", DepartmentPersonnelView.as_view()),
    path("department_detail/<str:name>", Custom.as_view()),
]
