from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    place = models.CharField(max_length=500)
    teacher = models.ForeignKey(
        'Teacher',
        on_delete=models.CASCADE,
        related_name='courses',
    )
    startTime = models.FloatField()
    endTime = models.FloatField()
    weekDay = models.IntegerField()
    appointment_id = models.SlugField()
    service_id = models.SlugField()
    pay = models.BooleanField(default=False)
    appointment = models.BooleanField()
    color = models.CharField(max_length=10)
    availability = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    short_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    position = models.TextField()
    imageUrl = models.SlugField(max_length=400, blank=True)

    def __str__(self):
        return self.name