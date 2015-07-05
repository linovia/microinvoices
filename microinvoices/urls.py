from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
import microinvoices.invoices.views


router = DefaultRouter()
router.register(r'invoices', microinvoices.invoices.views.Invoice)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
] + router.urls
