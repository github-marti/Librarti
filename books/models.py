from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True, null=True)
    read_date = models.CharField(max_length=255, blank=True, null=True)
    add_date = models.DateTimeField('date added')

    def __str__(self):
        return self.title

class Review(models.Model):
    NO_STARS = '☆☆☆☆☆'
    ONE_STAR = '★☆☆☆☆'
    TWO_STARS = '★★☆☆☆'
    THREE_STARS = '★★★☆☆'
    FOUR_STARS = '★★★★☆'
    FIVE_STARS = '★★★★★'
    REVIEW_CHOICES = [
        (NO_STARS, 'No stars'),
        (ONE_STAR, 'One star'),
        (TWO_STARS, 'Two stars'),
        (THREE_STARS, 'Three stars'),
        (FOUR_STARS, 'Four stars'),
        (FIVE_STARS, 'Five stars')
    ]
    book = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    stars = models.CharField(max_length=255, choices=REVIEW_CHOICES, default=NO_STARS)
    thoughts = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.stars