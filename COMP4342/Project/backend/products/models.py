from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.conf import settings

def validate_image_size(value):
    # Limit the image size to 5 MB
    max_size = 5 * 1024 * 1024  # 5 MB in bytes

    if value.size > max_size:
        raise ValidationError(f"Image size should be no more than {max_size / (1024 * 1024)} MB.")

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.ImageField(
        upload_to="media/",
        blank=True,
        null=True,
        validators=[validate_image_size, FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])]
    )
    category = models.CharField(max_length=100, null=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
