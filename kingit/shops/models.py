from django.db import models
from django.urls import reverse


class TC(models.Model):
    title = models.CharField(max_length=255, verbose_name='название ТЦ')
    status = models.CharField(max_length=255, verbose_name='статус')
    count_pavilions = models.SmallIntegerField()
    city = models.CharField(max_length=255, verbose_name='город')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='стоимость')
    add_value_rito = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='кооф. добавочной стоимотси')
    storeys = models.SmallIntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def get_absolute_url(self):
        return reverse('managerC_edit', kwargs={'pk': self.pk})

    def delete_tc(self):
        return reverse('delete_tc', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ТЦ'
        verbose_name_plural = 'ТЦы'
        ordering = ['title']

class Worker(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    email = models.EmailField(max_length=255, verbose_name='email')
    password = models.CharField(max_length=255, verbose_name='password')
    role = models.CharField(max_length=255, verbose_name='роль')
    phone = models.CharField(max_length=255, verbose_name='телефон')
    gender = models.CharField(max_length=255, verbose_name='пол')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def get_absolute_url(self):
        return reverse('administrator_edit', kwargs={'pk': self.pk})

    def delete_worker(self):
        return reverse('delete_worker', kwargs={'pk': self.pk})

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Pavilion(models.Model):
    title_TC = models.CharField(max_length=255)
    number_pavilion = models.CharField(max_length=3, verbose_name='номер павилиона')
    floor = models.SmallIntegerField(verbose_name='этаж')
    status = models.CharField(max_length=255, verbose_name='статус')
    area = models.SmallIntegerField( verbose_name='общая площадь')
    cost_sqm = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='стоимость за кв.м')
    add_value_rito = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='кооф. добавочной стоимотси')

    def __str__(self):
        return self.title_TC

    class Meta:
        verbose_name = 'Павильон'
        verbose_name_plural = 'Павильоны'


class Tenant(models.Model):
    title_phone = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, verbose_name='телефон')
    address = models.CharField(max_length=255, verbose_name='адрес')

    def __str__(self):
        return self.title_phone

    class Meta:
        verbose_name = 'Арендатор'
        verbose_name_plural = 'Арендаторы'


class Rent(models.Model):
    title_TC = models.CharField(max_length=255, verbose_name='название тц')
    number_pavilion = models.CharField(max_length=3, verbose_name='номер павилиона ')
    status = models.CharField(max_length=255, verbose_name='статус')
    start_rent = models.DateField(verbose_name='начало ренты')
    finish_rent = models.DateField(verbose_name='окончание ренты')
    ID_tenant = models.ForeignKey(Tenant, models.PROTECT)
    ID_Worker = models.ForeignKey(Worker, models.PROTECT)

    def __str__(self):
        return self.title_TC

    class Meta:
        verbose_name = 'Аренда'
        verbose_name_plural = 'Аренды'
