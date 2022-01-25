from django.db import models
from django.utils import timezone

from core.models import User


class DatesModelMixin(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(verbose_name="Дата создания")
    updated = models.DateTimeField(verbose_name="Дата последнего обновления")

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super().save(*args, **kwargs)


class GoalCategory(DatesModelMixin):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ('title', 'user')

    title = models.CharField(verbose_name="Заголовок", max_length=255)
    user = models.ForeignKey(User, verbose_name="Автор", null=True, default=None, blank=True,
                             help_text="В случае пустого значения категория будет общей", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Goal(DatesModelMixin):
    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"

    class Status(models.IntegerChoices):
        to_do = 1, "To do"
        in_progress = 2, "In progress"
        done = 3, "Done"
        archived = 4, "Archived"
        overdue = 5, "Overdue"

    class Priority(models.IntegerChoices):
        low = 1
        medium = 2
        high = 3
        critical = 4

    user = models.ForeignKey(User, verbose_name="Пользователь", related_name="goals", on_delete=models.PROTECT)
    category = models.ForeignKey(GoalCategory, verbose_name="Категория", on_delete=models.PROTECT)
    title = models.CharField(verbose_name="Заголовок", max_length=255)
    description = models.TextField(verbose_name="Описание")
    due_date = models.DateField(verbose_name="Дата выполнения")
    status = models.PositiveSmallIntegerField(verbose_name="Статус", choices=Status.choices)
    priority = models.PositiveSmallIntegerField(verbose_name="Приоритет", choices=Priority.choices)

    def __str__(self):
        return self.title


# TODO changes history?

