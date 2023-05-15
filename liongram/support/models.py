from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Faq(models.Model):
    CATEGORY_ONE ='1'
    CATEGORY_CHOICES = [
        (CATEGORY_ONE,'일반'),
        ('2','계정'),
        ('3','기타'),
    ]
    title = models.CharField(verbose_name="질문 제목",max_length=80)
    content= models.TextField(verbose_name='질문 내용')
    category=models.CharField(verbose_name='카테고리',max_length=2,choices=CATEGORY_CHOICES)

    created_at: models.DateTimeField(verbose_name='생성일지',auto_now_add=True)
    updated_at : models.DateTimeField(verbose_name='최종 수정 일시',auto_now=True)
    created_by : models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='faq_created_by')
    updated_by : models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='faq_updated_by')
