from django.db import models


class Poll(models.Model):
    question = models.CharField(max_length=2500, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.question} - {self.created_at}'

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Choice(models.Model):
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='choices', verbose_name='Опрос')

    def __str__(self):
        return f'{self.text}'
