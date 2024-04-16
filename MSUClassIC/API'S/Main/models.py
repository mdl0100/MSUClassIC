from django.db import models


class DepartmentModel(models.Model):
    """
    For registration purpose
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AxisModel(models.Model):
    """
    For axis labels,
    x-axis: Professor names
    y-axis: Time slots
    """

    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    name = models.CharField(max_length=50)
    static = models.BooleanField(default=True)
    moved = models.BooleanField(default=False)

    def __str__(self):
        return self.department.name + " - " + self.name


class ScheduleModel(models.Model):
    """
    For schedule data
    """

    department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    name = models.CharField(max_length=50)
    static = models.BooleanField(default=False)
    moved = models.BooleanField(default=False)

    def __str__(self):
        return self.department.name + " - " + self.name
