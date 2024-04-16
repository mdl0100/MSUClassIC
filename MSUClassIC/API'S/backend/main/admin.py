from django.contrib import admin

from . import models

admin.site.register(models.DepartmentModel)
admin.site.register(models.AxisModel)
admin.site.register(models.ScheduleModel)
