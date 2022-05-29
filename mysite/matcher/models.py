from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=50)


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    skills = models.ManyToManyField("matcher.Skill", blank=True)

    def __str__(self):
        return f'{self.name}'


class Job(models.Model):
    title = models.CharField(max_length=50)
    skills = models.ManyToManyField("matcher.Skill")