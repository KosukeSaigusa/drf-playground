import uuid

from django.db import models


class Author(models.Model):
    """
    著者モデル。
    Book: N - Author: N の関係である。
    """

    class Meta:
        db_table = "author"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="著者名", max_length=120)


class Book(models.Model):
    """
    本モデル。
    """

    # モデル内部の Meta クラスには、対応するテーブル名、デフォルトのソート順、
    # 複数カラムへのユニーク制約やインデックス、モデルオブジェクトの名称（管理サイトなどで使用）、
    # モデルクラス全体に対する付加情報（オプション）などを記述する。
    class Meta:
        db_table = "book"

    # Field クラスに指定できるフィールドオプションの例
    #
    # - verbose_name: フィールドの名前。
    # - unique: データベースのユニーク制約。
    # - db_index: データベースのインデックスを設定するかどうか。
    # - primary_key: フィールドを主キーにするかどうか。
    # - default: レコード登録時に値が指定されなかった場合のデフォルト値。
    # - max_length: 文字列の最大文字数。CharField では指定必須（Field クラスの
    # check() メソッドで呼ばれる _check_max_length_attribute() メソッドが
    # 担当している）。
    # - choices: 登録・更新時の入力値の取りうる値を制限する。
    # - blank: CharField や TextField において ModelSerializer でのバリデーション時に
    # 空白文字列を許可するかどうか規定する（デフォルト: False）。
    # - validators: 文字種チェックなどのバリデーションを指定する。
    # - on_delete: OneToOneField および ForeignKey で指定必須。関連先のモデルオブジェクトが
    # 削除された際の挙動を規定する。
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name="タイトル", max_length=120)
    price = models.IntegerField(verbose_name="価格", null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    # Book と N 対 N の関係にある Author モデルを ManyToManyField で表現している。
    authors = models.ManyToManyField(Author, verbose_name="著者", blank=True)

    # BookSerializer に price_with_tax の SerializerMethodField を
    # 定義するのもよいが、Book モデルに @property で属性を追加しても良い。
    # @property
    # def price_with_tax(self) -> Optional[int]:
    #     if not self.price:
    #         return None
    #     return int(Decimal(self.price) * Decimal(1 + TAX_RATE))

    def __str__(self):
        return self.title
