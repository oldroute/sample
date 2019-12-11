from django.db import models


class Planet(models.Model):

    class Meta:
        verbose_name = 'планета'
        verbose_name_plural = 'планеты'
        ordering = ['order']

    order = models.PositiveIntegerField(verbose_name='порядок', default=0)
    name = models.CharField(verbose_name='название', max_length=255)
    description = models.TextField(verbose_name='название', null=True, blank=True)
    code = models.CharField(verbose_name='код', max_length=255)

    def __str__(self):
        return self.name
