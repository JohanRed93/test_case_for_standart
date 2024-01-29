from django.contrib import admin

from .models import PaymentRequests, CompanyDetails


admin.site.register(PaymentRequests)
admin.site.register(CompanyDetails)

