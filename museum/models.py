from django.db import models
from django.urls import reverse
import users
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Tour(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, verbose_name=_('Тур'))
    exhibitions = models.ManyToManyField('Exhibition', verbose_name=_('Виставки'))
    date = models.DateTimeField(verbose_name=_('Час виставки'))
    admission = models.BooleanField(verbose_name=_('За записом?'))
    price = models.FloatField(default=0, verbose_name=_('Ціна'))

    def get_absolute_url(self):
        return reverse('tour-manage', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']


class Ticket(models.Model):
    id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name=_('Тур'))
    visitor = models.ForeignKey(users.models.MuseumUser, on_delete=models.CASCADE, verbose_name=_('Відвідувач'))

    def get_absolute_url(self):
        return reverse('ticket-manage', args=[str(self.id)])

    def __str__(self):
        return self.tour + " - " + self.visitor


class Exhibition(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128, verbose_name=_('Виставка'))
    items = models.ManyToManyField('Item', verbose_name=_('Предмети'))
    tours = models.ManyToManyField(Tour, null=True, blank=True, default=None, verbose_name=_('Тури'))

    def get_absolute_url(self):
        return reverse('exhibition-manage', args=[str(self.id)])

    def __str__(self):
        return self.name


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, verbose_name=_('Предмет'))
    quantity = models.IntegerField(verbose_name=_('Кількість'))
    in_exhibition = models.ForeignKey(Exhibition, null=True, on_delete=models.SET_NULL, default=None, blank=True, verbose_name=_('Виставки'))

    def get_absolute_url(self):
        return reverse('storage-manage', args=[str(self.id)])

    def __str__(self):
        return self.name
