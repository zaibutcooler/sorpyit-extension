from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FreelanceOffer(models.Model):
    CHOICES = (
        ("day", 'day'),
        ("month", 'month'),
        ("year", 'year'),
    )

    CURRENCY_CHOICES = (
        ("Dollar", 'Dollar'),
        ("Yenn", 'Yenn'),
        ("Euro", 'Euro'),
        ("Yuan", 'Yuan'),
        ("Kyats", 'Kyats'),
    )

    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES)
    title = models.CharField(max_length=100)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    amount = models.IntegerField()
    requirements = models.TextField()
    deadline = models.CharField(max_length=100)
    deadline_type = models.CharField(max_length=20, choices=CHOICES)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_as_freelancer')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects_as_client')
    project_offer = models.ForeignKey(FreelanceOffer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField()


class FreelanceApply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(FreelanceOffer, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class ProjectReviews(models.Model):
    STAR_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=STAR_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
