import os.path
from uuid import uuid4
from django.db import models
from django.utils import timezone


def upload_func(instance, filename):
    prefix = timezone.now().strftime("%m/%d")
    file_name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()  # 확장자 추출
    return "/".join([
        prefix, file_name + extension,
    ])


# Create your models here.
class Letter(models.Model):
    sender = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    content = models.TextField(null=True, max_length=1500)
    image = models.ImageField(null=True, blank=True, upload_to=upload_func)
    timestamp = models.DateTimeField(default=timezone.now)
    sent = models.BooleanField(default=False)
    send_attempt_over = models.BooleanField(default=False)

    def __str__(self):
        fail_str = '[FAIL] ' if not self.sent else ''
        return fail_str + self.get_header()

    def get_header(self):
        return self.sender + ': ' + self.subject

    @classmethod
    def create(cls, sender, subject, content, image):
        return cls(sender=sender, subject=subject, content=content, image=image)