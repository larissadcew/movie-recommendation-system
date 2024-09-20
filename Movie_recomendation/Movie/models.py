from django.db import models


#class User():
    #pass

class Movie(models.Model):
    pass

# Create your models here.
class MovieReview(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)  # Relaciona com o filme
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.movie.title}'