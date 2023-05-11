from django_filters import rest_framework as filters

<<<<<<< HEAD
from api.models import Title
=======
from reviews.models import Title
>>>>>>> 65b8e1507a42d26c734ea6f696bb4dd670fbf374


class TitleFilter(filters.FilterSet):
    """Отбор произведения по наименованию."""

    genre = filters.CharFilter(field_name="genre__slug", lookup_expr="iexact")
    category = filters.CharFilter(field_name="category__slug",
                                  lookup_expr="iexact")
    year = filters.NumberFilter(field_name="year", lookup_expr="iexact")
    name = filters.CharFilter(field_name="name", lookup_expr="contains")

    class Meta:
        model = Title
<<<<<<< HEAD
        fields = "__all__"
=======
        fields = "__all__"
>>>>>>> 65b8e1507a42d26c734ea6f696bb4dd670fbf374
