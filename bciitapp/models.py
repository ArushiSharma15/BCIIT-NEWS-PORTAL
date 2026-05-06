from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.name


class ClubImage(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='clubs/')


# FACULTY
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.name


class FacultyImage(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='faculty/')


# EVENT
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.title


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='events/')


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField()
    message = models.TextField()
