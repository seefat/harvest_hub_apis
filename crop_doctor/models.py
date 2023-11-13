from django.db import models
from django.contrib.auth import get_user_model

from core.utils import BaseModelWithUID

User = get_user_model()

class CropDoctorQuestion(BaseModelWithUID, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='crop_doctor/questions/', blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Question by {self.user.username}: {self.title}"

class CropDoctorReply(BaseModelWithUID, models.Model):
    question = models.ForeignKey(CropDoctorQuestion, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_text = models.TextField()
    reply_image = models.ImageField(upload_to='crop_doctor/replies/', blank=True, null=True)

    def __str__(self):
        return f"Reply to {self.question.title} by {self.doctor.username}"
