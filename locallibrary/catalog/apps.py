from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CatalogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "locallibrary.catalog"
    verbose_name = _("Catalog")

    def ready(self):
        try:
            import locallibrary.catalog.signals  # noqa: F401
        except ImportError:
            pass
