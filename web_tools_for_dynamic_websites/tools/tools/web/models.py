from django.db import models


class Profile(models.Model):
    email = models.EmailField()

    name = models.CharField(
        max_length=25,
    )

    is_deleted = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'{self.pk}: {self.name} with {self.email}'

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        return self.save()
