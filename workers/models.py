from django.db import models


class Group(models.Model):
    """
    Модель бригады.
    """
    name = models.CharField(max_length=100, verbose_name="Название бригады")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бригада"
        verbose_name_plural = "Бригады"


class Speciality(models.Model):
    """
    Модель специальностей.
    """
    name = models.CharField(max_length=255, verbose_name="Специальность")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class Worker(models.Model):
    """
    Модель работника.
    """
    name = models.CharField(max_length=255, verbose_name="ФИО")
    group = models.ForeignKey(Group, default=None, on_delete=models.SET_NULL, blank=True, null=True,
                              verbose_name="Бригада")
    payment = models.PositiveIntegerField(verbose_name="Зарплата")
    speciality = models.ForeignKey(Speciality, default=None, on_delete=models.SET_NULL, blank=True, null=True,
                                   verbose_name="Специальность")

    def __str__(self):
        return f"{self.name} - {self.group} - {self.payment} - {self.speciality}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
