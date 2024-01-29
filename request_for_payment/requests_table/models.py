from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from request_for_payment.settings import PAYMENT_TYPE, PAYMENT_STATUS

User = get_user_model()


class CompanyDetails(models.Model):
    payment_type = models.CharField(
        max_length=2,
        choices=PAYMENT_TYPE,
        default='CR',
        verbose_name='Тип платежа',
    )
    account_type = models.CharField(
        max_length=100,
        verbose_name='Тип карты/счёта',
    )
    owner_surname = models.CharField(
        max_length=50,
        verbose_name='Фамилия',
    )
    owner_name = models.CharField(
        max_length=50,
        verbose_name='Имя',
    )
    owner_patronymic = models.CharField(
        max_length=50,
        verbose_name='Отчество',
    )
    phone = PhoneNumberField(verbose_name='Номер телефона')
    limit = models.DecimalField(
        max_digits=21,
        decimal_places=2,
        verbose_name='Лимит средств',
    )


class PaymentRequests(models.Model):
    id = models.BigAutoField(
        primary_key=True,
        verbose_name='ID',
    )
    total = models.DecimalField(
        max_digits=21,
        decimal_places=2,
        verbose_name='Сумма платежа',
    )
    companydetails = models.ForeignKey(
        CompanyDetails,
        related_name='details',
        on_delete=models.CASCADE,
        verbose_name='Реквизиты',
    )
    status = models.CharField(
        max_length=2,
        choices=PAYMENT_STATUS,
        default='WT',
        verbose_name='Статус платежа',
    )
