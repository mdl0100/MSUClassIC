from django.urls import path

from . import views


urlpatterns = [
    # GET - Get all departments
    # POST - Create a new department
    path("department/", views.DepartmentView.as_view(), name="department"),
    #
    # GET - Get department schedule data (by department_id)
    path(
        "department/<int:department_id>/",
        views.DepartmentScheduleView.as_view(),
        name="department_schedule",
    ),
    #
    # POST - Create a new axis label (professor name or time slot)
    path("axis/", views.AxisView.as_view(), name="axis"),
    #
    # POST - Create a new schedule data
    path("schedule/", views.ScheduleView.as_view(), name="schedule"),
    #
    # DELETE - Delete a schedule data
    path(
        "schedule/delete/<int:schedule_id>/",
        views.ScheduleDeleteView.as_view(),
        name="schedule_delete",
    ),
]
