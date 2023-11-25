from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class MusicalInstrument(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Students(models.Model):
    # choice = [
    #     ('Guitar', 'Guitar'),
    #     ('Piano', 'Piano'),
    #     ('Saxophone', 'Saxophone'),
    #     ('Drum', 'Drum'),
    # ]

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.PositiveIntegerField()
    musical_instrument = models.ForeignKey(MusicalInstrument, on_delete=models.SET_NULL, null=True)
    grade = models.PositiveIntegerField('Grade', validators=[MinValueValidator(1), MaxValueValidator(12)])
    payment = models.BooleanField('Payment', default=False)
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return f'{self.name} - {self.age} - {self.course}'

    def get_absolute_url(self):
        return reverse('students_page', kwargs={'student_slug': self.slug})

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.surname}-{self.course}')
        super().save(force_insert, force_update, using, update_fields)
        return f'{self.name} - {self.surname} - {self.course}'


