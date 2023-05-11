<<<<<<< HEAD
=======
from django.urls import include, path
>>>>>>> 65b8e1507a42d26c734ea6f696bb4dd670fbf374
from rest_framework.routers import DefaultRouter

from api.views import (
    CategoryViewSet,
<<<<<<< HEAD
    GenreViewSet,
    TitleViewSet,
)

router = DefaultRouter()
router.register("categories", CategoryViewSet)
router.register("genres", GenreViewSet)
router.register("titles", TitleViewSet)
=======
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
    UserViewSet
)

router_v1 = DefaultRouter()
router_v1.register("categories", CategoryViewSet)
router_v1.register("genres", GenreViewSet)
router_v1.register("titles", TitleViewSet)
router_v1.register('users', UserViewSet)
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews",
    ReviewViewSet, basename="reviews"
)
router_v1.register(
    r"titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments",
    CommentViewSet, basename="comments"
)

urlpatterns = [
    path("v1/", include(router_v1.urls)),
    path("v1/auth/", include("users.urls")),
]
>>>>>>> 65b8e1507a42d26c734ea6f696bb4dd670fbf374
