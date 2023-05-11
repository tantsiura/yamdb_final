<<<<<<< HEAD
from rest_framework import (filters, mixins, viewsets)

from api.filters import TitleFilter
from api.models import Category, Genre, Title

from api.serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializerCreateAndUpdate,
    TitleSerializerGet,
)

=======
import uuid

# from django.shortcuts import get_object_or_404
from rest_framework import (filters, mixins, views, viewsets)
from rest_framework import status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from django.core.mail import send_mail
from django.db import IntegrityError

from api_yamdb.settings import DEFAULT_EMAIL
from api.filters import TitleFilter
from reviews.models import Category, Genre, Review, Title
from users.models import User

from api.serializers import (
    CategorySerializer,
    CommentSerializer,
    GenreSerializer,
    ReviewSerializer,
    SignUpSerializer,
    TitleSerializerCreateAndUpdate,
    TitleSerializerGet,
    TokenSerializer,
    UserSerializer
)


>>>>>>> 65b8e1507a42d26c734ea6f696bb4dd670fbf374
class CategoryAndGenreMixin(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Класс для категорий и жанров."""

    filter_backends = [filters.SearchFilter]
    search_fields = ["=name"]
    lookup_field = "slug"


class CategoryViewSet(CategoryAndGenreMixin):
    """Класс для работы с категориями."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(CategoryAndGenreMixin):
    """Класс для работы с жанрами."""

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class TitleViewSet(viewsets.ModelViewSet):
    """Класс для работы с произведениями."""

    queryset = Title.objects.all()
    http_method_names = ["get", "post", "delete", "patch"]
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ["create", "partial_update", "destroy"]:
            return TitleSerializerCreateAndUpdate
        return TitleSerializerGet
<<<<<<< HEAD
=======


class ReviewViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing reviews.
    The viewset provides re-defined `perform_create()` and `get_queryset()`
    actions.
    """
    serializer_class = ReviewSerializer

    def get_queryset(self):
        """Re-define method to return only comments belonging to the post."""
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))

        return title.reviews.select_related('author')

    def perform_create(self, serializer):
        """Re-define method to set comment's author and post automatically."""
        title = get_object_or_404(Title, id=self.kwargs.get("title_id"))
        serializer.save(
            author=self.request.user,
            title=title
        )


class CommentViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for managing comments.
    The viewset provides re-defined `perform_create()` and `get_queryset()`
    actions.
    """
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Re-define method to return only comments belonging to the post."""
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))

        return review.reviews.select_related('author')

    def perform_create(self, serializer):
        """Re-define method to set comment's author and post automatically."""
        review = get_object_or_404(Review, id=self.kwargs.get("review_id"))
        serializer.save(
            author=self.request.user,
            review=review
        )


class SignUpViewSet(CreateAPIView):

    def create(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user, create = User.objects.get_or_create(
                **serializer.validated_data)
        except IntegrityError:
            return Response(
                'Ошибка данных. Проверьте поле login или email!',
                status=status.HTTP_400_BAD_REQUEST
            )
        user.save()
        confirmation_code = str(uuid.uuid4())
        user.confirmation_code = confirmation_code
        send_mail(
            subject='Ваш код подтверждения',
            message=f'Код подтверждения:{confirmation_code}',
            from_email=DEFAULT_EMAIL,
            recipient_list=[user.email],
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateTokenViewSet(views.APIView):

    def get_token(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        confirmation_code = serializer.validated_data['confirmation_code']
        user = get_object_or_404(User, username=username)
        if user.confirmation_code == confirmation_code:
            token = RefreshToken.for_user(user)
            token_data = {'token': str(token.access_token)}
            return Response(token_data, status=status.HTTP_200_OK)
        return Response(
            'Некорректный код подтверждения!',
            status=status.HTTP_400_BAD_REQUEST
        )


class UserViewSet(viewsets.ModelViewSet):
    """Viewset для модели  User."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ('username',)
    lookup_field = ('username')

    @action(
        methods=['get', 'patch'],
        detail=False,
        url_path='me',
    )

    def edit_own_profile(self, request):
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                request.user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            serializer = self.get_serializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
>>>>>>> 65b8e1507a42d26c734ea6f696bb4dd670fbf374
