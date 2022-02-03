from django.db import models


class Blog(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Информация')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
