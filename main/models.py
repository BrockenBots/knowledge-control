from django.db import models


class Admin(models.Model):
    admin_id = models.IntegerField(primary_key=True, auto_created=True)
    login = models.CharField(max_length=50)
    name = models.CharField(max_length=80)
    password = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'


class User(models.Model):
    user_id = models.IntegerField(primary_key=True, auto_created=True)
    login = models.CharField(max_length=50)
    name = models.CharField(max_length=80)
    password = models.CharField(max_length=30)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True, auto_created=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class UserAnswer(models.Model):
    user_answer_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)
    test_id = models.ForeignKey('Test', on_delete=models.CASCADE)
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)
    answer_id = models.ForeignKey('Answer', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователей'


class Answer(models.Model):
    answer_id = models.IntegerField(primary_key=True, auto_created=True)
    answer_text = models.CharField()
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Question(models.Model):
    question_id = models.IntegerField(primary_key=True, auto_created=True)
    question_text = models.CharField(max_length=200)
    test_id = models.ForeignKey('Test', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Test(models.Model):
    test_id = models.IntegerField(primary_key=True, auto_created=True)
    test_name = models.CharField(max_length=40)
    description = models.TextField(max_length=1000)
    category_id = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

