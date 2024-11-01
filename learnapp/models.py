from django.db import models
import uuid

class SampleModel(models.Model):
    # Character and Text Fields
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Numeric Fields
    quantity = models.IntegerField()
    price = models.FloatField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.PositiveIntegerField()
    rating = models.PositiveSmallIntegerField()

    # Boolean Field
    is_active = models.BooleanField(default=True)

    # Date and Time Fields
    start_date = models.DateField()
    start_datetime = models.DateTimeField()
    alert_time = models.TimeField()

    # Email and URL Fields
    email = models.EmailField(unique=True)
    website = models.URLField()

    # Slug Field
    slug = models.SlugField(unique=True)

    # File and Image Fields
    file = models.FileField(upload_to='files/')
    image = models.ImageField(upload_to='images/')

    # Relational Fields
    foreign_key_field = models.ForeignKey('self', on_delete=models.CASCADE, related_name="related_foreign_key")
    one_to_one_field = models.OneToOneField('self', on_delete=models.CASCADE, related_name="related_one_to_one")
    many_to_many_field = models.ManyToManyField('self', related_name="related_many_to_many")

    # UUID and JSON Fields
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    json_field = models.JSONField(default=dict)

    def __str__(self):
        return self.name
