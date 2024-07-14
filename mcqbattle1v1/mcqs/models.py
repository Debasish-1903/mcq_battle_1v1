from django.db import models

import uuid

# Create your models here.


class MCQs(models.Model):
    id=models.UUIDField(primary_key=True,
                        default=uuid.uuid4,
                        editable=False)
    body=models.TextField()
    explanation=models.TextField()
    options=models.JSONField()

