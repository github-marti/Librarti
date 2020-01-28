from django.db import models

# Create your models here.
class Book(models.Model):
    NONE = '☆☆☆☆☆'
    ONE_STAR = '★☆☆☆☆'
    TWO_STARS = '★★☆☆☆'
    THREE_STARS = '★★★☆☆'
    FOUR_STARS = '★★★★☆'
    FIVE_STARS = '★★★★★'
    REVIEW_CHOICES = [
        (NONE, 'None'),
        (ONE_STAR, 'One star'),
        (TWO_STARS, 'Two stars'),
        (THREE_STARS, 'Three stars'),
        (FOUR_STARS, 'Four stars'),
        (FIVE_STARS, 'Five stars')
    ]  
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=10000, blank=True, null=True)
    review = models.CharField(max_length=255, choices=REVIEW_CHOICES, default=NONE)
    thoughts = models.CharField(max_length=10000, blank=True, null=True)
    read_date = models.CharField(max_length=255, blank=True, null=True)
    add_date = models.DateTimeField('date added')
    def __str__(self):
        return self.title