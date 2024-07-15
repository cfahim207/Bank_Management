
from django.contrib import admin
from django.urls import path,include
from core.views import homeview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview.as_view(),name='home'),
    path('account/', include("accounts.urls")),
    path('transactions/', include("transactions.urls")),
]
