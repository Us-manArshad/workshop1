from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="parent_category", null=True, blank=True)

    def __str__(self):
        if self.parent:
            return f"{self.parent} > {self.title}"
        return self.title
