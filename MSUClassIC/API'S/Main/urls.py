from django.urls import path

from . import views


urlpatterns = [
    path("department/", views.DepartmentView.as_view(), name="department"),
    path(
        "department/<int:department_id>/",
        views.DepartmentScheduleView.as_view(),
        name="department_schedule",
    ),
    path("axis/", views.AxisView.as_view(), name="axis"),
    path("schedule/", views.ScheduleView.as_view(), name="schedule"),
    path("schedule/delete/<int:schedule_id>/", views.ScheduleDeleteView.as_view(), name="schedule_delete"),
]
