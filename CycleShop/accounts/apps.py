from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "CycleShop.accounts"

    def ready(self):
        import CycleShop.accounts.signals
