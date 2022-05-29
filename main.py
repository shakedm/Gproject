# assume Database is "mysite"
# connection to DB is in manage
from django.db import models
from django.db import connections


class Skill(models.Model):
    name = models.CharField()


class Candidate(models.Model):
    name = models.CharField()
    title = models.CharField()
    skills = models.ManyToManyField("Skill")


class Job(models.Model):
    title = models.CharField()
    skills = models.ManyToManyField("Skill")


def takesecond(element):
    return element[1]


def matcher(job: Job):
    title = job.title
    # execute a DB query to get all matching candidates with same title

    # CHECK THE RETURN OBJECT DJANGO CAN'T DEAL WITH EMPTY RESULT
    can = Candidate.objects.raw(" SELECT *  FROM candidate WHERE title = %s", [title])

    BestMatch = []
    # for each candidate we scan through the skills to see how many skills does he have that fit the job
    for c in can:
        skillMatch = 0
        for Cskill in c.skills:
            if Cskill in job.skills:
                skillMatch += 1
        BestMatch.append((c, skillMatch))

    # sort the list so the best matching candidates appear first
    BestMatch.sort(key=takesecond)
    return BestMatch


def main():
    title = input('Enter a job title to search:')
    skills = input('Enter the skills for the job')
    matcher(job=Job(title, skills))


if __name__ == '__main__':
    main()
