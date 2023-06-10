from django.db import models
from django.contrib.auth.models import User


# class Admin(models.Model):
#     name = models.CharField(max_length=80)
#
#     class Meta:
#         verbose_name = 'Администратор'
#         verbose_name_plural = 'Администраторы'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# class UserAnswer(models.Model):
#     user_id = models.ForeignKey('User', on_delete=models.CASCADE)
#     test_id = models.ForeignKey('Test', on_delete=models.CASCADE)
#     question_id = models.ForeignKey('Question', on_delete=models.CASCADE)
#     answer_id = models.ForeignKey('Answer', on_delete=models.PROTECT)
#
#     class Meta:
#         verbose_name = 'Ответ пользователя'
#         verbose_name_plural = 'Ответы пользователей'

class UserResult(models.Model):
    user = models.ForeignKey('Profile', on_delete=models.CASCADE)
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    result = models.IntegerField()

    def __str__(self):
        return str(f"{self.user}-{self.test}")

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'


class Answer(models.Model):
    answer_text = models.CharField(max_length=300)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    score = models.IntegerField()
    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Test(models.Model):
    test_name = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.test_name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

