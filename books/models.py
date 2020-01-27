from django.db import models

# Create your models here.
class Book(models.Model):
    class Review(models.IntegerChoices):
        NONE = 0
        ONE_STAR = 1
        TWO_STARS = 2
        THREE_STARS = 3
        FOUR_STARS = 4
        FIVE_STARS = 5    
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    synopsis = models.CharField(max_length=10000, blank=True, null=True)
    review = models.IntegerField(choices=Review.choices, default=Review.NONE)
    thoughts = models.CharField(max_length=10000, blank=True, null=True)
    read_date = models.CharField(max_length=255, blank=True, null=True)
    add_date = models.DateTimeField('date added')
    def __str__(self):
        return self.title