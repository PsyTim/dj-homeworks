from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter("created_at")

    class Meta:
        model = Advertisement
        fields = ["created_at", "creator"]
