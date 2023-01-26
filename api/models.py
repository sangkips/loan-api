from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from django.core.validators import RegexValidator


BUSINESS_SECTOR = (
    ("Retail", "Retail"),
    ("Professional Services", "Professional Services"),
    ("Food & Drink", "Food & Drink"),
    ("Entertainment", "Entertainment"),
)


class CustomUser(AbstractUser):
    """
    AbstractUser allows us to use email and not username as the identifier
    """

    # name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name", "phone_number"]

    def __str__(self):

        return f"{self.first_name} {self.last_name}"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=200)
    address = models.CharField(max_length=50)
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
        max_digits=19,
        decimal_places=2,
        validators=[MinMoneyValidator(10000), MaxMoneyValidator(100000)],
    )
    loan_duration = models.IntegerField(help_text="Duration in days")
    reason_for_borrowing = models.TextField(help_text="Reasons for requesting a loan")

    def __str__(self):
        return self.business_name
