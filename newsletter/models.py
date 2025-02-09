from django.db import models
from django import forms


class Recipient(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    comment = models.TextField()

    def __str__(self):
        return self.name


class Message(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.subject

class Sending(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=15, choices=(
        ('Завершена', 'Завершена'),
        ('Создана', 'Создана'),
        ('Запущена', 'Запущена')
    ))
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    recipients = models.ManyToManyField(Recipient)

    def __str__(self):
        return self.status
