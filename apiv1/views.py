from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apiv1.serializers import BookSerializer
from shop.models import Book


# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    """
    本モデルの CRUD のための APIView (ModelViewSet クラス。
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # 登録・更新用のメソッドはログイン必須に設定する。
    permission_classes = [IsAuthenticatedOrReadOnly]
