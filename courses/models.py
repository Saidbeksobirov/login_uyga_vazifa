from django.db import models


class CoursesModel(models.Model):
    full_name = models.CharField(max_length=123)
    phone_number = models.CharField(max_length=13)
    age = models.IntegerField()

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'courses'
        verbose_name_plural = 'coursess'