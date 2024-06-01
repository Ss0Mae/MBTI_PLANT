from django.db import models

# Create your models here.

class Question(models.Model):
    CATEGORY_CHOICES = [
        ('EI', '외향형 (E) vs. 내향형 (I)'),
        ('SN', '감각형 (S) vs. 직관형 (N)'),
        ('TF', '사고형 (T) vs. 감정형 (F)'),
        ('JP', '판단형 (J) vs. 인식형 (P)'),
    ]

    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

