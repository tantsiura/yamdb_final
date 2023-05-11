from rest_framework import serializers
<<<<<<< HEAD

from api.models import Category, Genre, Title
=======
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User
>>>>>>> 65b8e1507a42d26c734ea6f696bb4dd670fbf374


class CategorySerializer(serializers.ModelSerializer):
    """Класс для преобразования данных категории."""

    class Meta:
        model = Category
        fields = (
            "name",
            "slug",
        )


class GenreSerializer(serializers.ModelSerializer):
    """Класс для преобразования данных жанра."""

    class Meta:
        model = Genre
        fields = (
            "name",
            "slug",
        )


class TitleSerializerGet(serializers.ModelSerializer):
    """Класс для преобразования данных произведения при методе GET."""

    category = CategorySerializer(many=False, read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Title
        fields = "__all__"


class TitleSerializerCreateAndUpdate(serializers.ModelSerializer):
    """
    Класс для преобразования данных произведения при методах CREATE и UPDATE.
    """

    category = serializers.SlugRelatedField(
        slug_field="slug", queryset=Category.objects.all()
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field="slug", many=True
    )

    class Meta:
        model = Title
<<<<<<< HEAD
        fields = "__all__"
=======
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for Review instances.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Review
        fields = (
            "id",
            "text",
            "author",
            "score",
            "pub_date",
            "title"
        )
        read_only_fields = ("title",)
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['author', 'title'],
                message=('На одно произведение '
                         'пользователь может оставить только один отзыв.')
            )
        ]


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment instances.
    """
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Comment
        fields = (
            "id",
            "text",
            "author",
            "pub_date",
            "review"
        )
        read_only_fields = ("review",)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "bio",
            "role",
        )
        model = User


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    
    class Meta:
        model = User
        fields = ('email', 'username')

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                '"me" не может быть использован в качестве Username!'
            )
        return value


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')
>>>>>>> 65b8e1507a42d26c734ea6f696bb4dd670fbf374
