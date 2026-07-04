from django.db import models
from django.utils.text import slugify


class Interest(models.Model):
    """
    User interests used for partner matching.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
        db_index=True,
    )

    slug = models.SlugField(
        max_length=120,
        unique=True,
        editable=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "interests"
        ordering = ("name",)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name