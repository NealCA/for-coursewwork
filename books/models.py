from django.db import models

# Create your models here.


class Author (models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=70, default='null')
    password = models.CharField(max_length=50, default='123')

    def __str__(self):
        return self.username


class News (models.Model):
    unique_key = unique_key = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    headline = models.CharField(max_length=64, unique=True)
    category = [('pol', 'ForPolitics'), ('art', 'ForArt'), ('tech', 'ForTechnologyNew'), ('trivia', 'ForTriviaNews')]
    category = models.CharField(max_length=50)
    region = [('uk', 'ForUKNews'), ('eu', 'ForEuropeanNews'), ('w', 'ForWorldNews')]
    region = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    details = models.CharField(max_length=512,)

