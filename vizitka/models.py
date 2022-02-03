from django.db import models


class Viz(models.Model):
    title = models.CharField('Название', max_length=60)
    text = models.TextField('Описание')
    date = models.DateTimeField()
    photo = models.ImageField(upload_to='vizitka/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
