from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator


class BaseUserModel(models.Model):
    """
    BaseUserModel represents the common fields and functionalities for users in the system.

    This abstract model provides the following fields:
    - first_name: The user's first name (required).
    - last_name: The user's last name (required).
    - address: The user's address (required).
    - national_id: A unique national identification number (required, must be 14 characters).
    - email: A unique email address for the user (required, must be from the '@gmail.com' domain).
    - phone_number1: The user's primary phone number (required, unique).
    - phone_number2: An optional secondary phone number (unique if provided).
    - graduation_date: The date the user graduated (required, includes year, month, and day).
    - qualification: The user's qualification level (required).
    - gender: The user's gender, with options for 'male' and 'female' (default is 'male').
    - year_of_birth: The user's year of birth (required).
    - marital_status: The user's marital status, with options such as 'single', 'married', 'divorced', and 'widowed' (default is 'single').
    - employment_date: The date the user was added to the system (auto-generated when the user is created).

    The `clean` method ensures that the email must belong to the Gmail domain, raising a ValidationError otherwise.

    This model is abstract and should be inherited by other models that require these common fields.
    """

    MARITAL_STATUS_CHOICES = [
        ("single", "single"),
        ("married", "married"),
        ("divorced", "divorced"),
        ("widowed", "widowed"),
    ]

    GENDER_CHOICES = [
        ("male", "male"),
        ("female", "female"),
    ]

    QUALIFICATION_CHOICES = [
        ("high_school", "High School"),
        ("bachelor", "Bachelor"),
        ("master", "Master"),
        ("doctorate", "Doctorate"),
    ]

    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=150, null=False, blank=False)
    national_id = models.CharField(
        max_length=14,
        unique=True,
        null=False,
        blank=False,
        validators=[MinLengthValidator(14)],
    )
    email = models.EmailField(max_length=245, null=False, blank=False, unique=True)
    phone_number1 = models.CharField(
        max_length=13, null=False, blank=False, unique=True
    )
    phone_number2 = models.CharField(max_length=13, null=True, blank=True)
    graduation_date = models.DateField(null=False, blank=False)
    qualification = models.CharField(
        max_length=20,
        choices=QUALIFICATION_CHOICES,
        default="high_school",
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default="male",
    )
    year_of_birth = models.DateField(null=False, blank=False)
    marital_status = models.CharField(
        max_length=10,
        choices=MARITAL_STATUS_CHOICES,
        default="single",
    )
    employment_date = models.DateField(auto_now_add=True)

    def clean(self):
        super().clean()
        if not self.email.endswith("@gmail.com"):
            raise ValidationError("Email must be from @gmail.com domain.")

    def __str__(self):
        return f"name is {self.first_name} and email is {self.email}"

    class Meta:
        abstract = True
