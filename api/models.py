from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


from django.db.models.signals import post_save
from django.dispatch import receiver


BUSINESS_SECTOR = (
    ("Retail", "Retail"),
    ("Professional Services", "Professional Services"),
    ("Food & Drink", "Food & Drink"),
    ("Entertainment", "Entertainment"),
)


class User(AbstractUser):
    """
    AbstractUser allows us to use email and not username as the identifier
    """

    email = models.EmailField(max_length=50, unique=True)
    phone_number = PhoneNumberField(
        unique=True, help_text="Start with your country code such as +254"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "phone_number"]

    def __str__(self):

        return f"{self.first_name} {self.last_name}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user}"


# signal to create user profile
@receiver(post_save, sender=User)
def create_user_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# signal to save created user profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class LoanBook(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="loans",
        on_delete=models.SET_NULL,
        null=True,
    )
    business_name = models.CharField(max_length=200)
    registered_company_number = models.CharField(
        unique=True,
        max_length=8,
        validators=[
            RegexValidator(
                regex="\d{8}", message="Please provide 8 digit number", code="nomatch"
            )
        ],
        help_text="Enter 8 digit number",
    )
    # moneyField here handles the country's currency and improve on validations
    business_sector = models.CharField(max_length=30, choices=BUSINESS_SECTOR)
    amount_borrowed = MoneyField(
        max_digits=10,
        decimal_places=2,
        default_currency="KES",
        validators=[MinMoneyValidator(10000), MaxMoneyValidator(100000)],
    )
    loan_duration = models.CharField(
        max_length=2,
        validators=[
            RegexValidator(
                regex="\d{2}", message="Please specify duration in days", code="nomatch"
            )
        ],
        help_text="Duration in days",
        default=30,
    )
    reason_for_borrowing = models.TextField(help_text="Reasons for requesting a loan")

    def __str__(self):
        return f"{self.owner}"
