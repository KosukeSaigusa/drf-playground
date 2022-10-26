from decimal import Decimal
from typing import Optional

from rest_framework import serializers

from config.constants import TAX_RATE
from shop.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author

    fields = [
        "id",
        "name",
    ]


# class AuthorListSerializer(serializers.ListSerializer):
#     def update(self, instance, validated_data):
#         pass
#
#     child = AuthorSerializer()


# ModelSerializer を継承することで、モデルのフィールド定義を再利用することができ、
# モデルの定義に基づいた型変換やバリデーションが行われるので、シリアライザの
# 記述量を大幅に減らすことができる。
class BookSerializer(serializers.ModelSerializer):
    # 税込価格（Book モデルには存在しないが、レスポンスに追加したいフィールド）
    price_with_tax = serializers.SerializerMethodField()

    # Book を取得する API で、Book モデルに（一対一で）関連している
    # 出版社（Publisher モデル）のフィールドも一緒に取得したい場合には、
    # このように ReadOnlyField と source オプションを利用することで
    # それを実現することができる。
    publisher_name = serializers.ReadOnlyField(source="publisher.name")

    # Book モデルの ManyToManyField である Author を、Book を取得する API で
    # 一緒に取得したい場合には、このような ListSerializer を使用するか、
    # many=True な Serializer を記述する。
    # authors = AuthorListSerializer()
    authors = AuthorSerializer(many=True)

    class Meta:
        # Meta クラスの model に対象のモデルクラスを定義する。
        model = Book

        # Meta クラスの fields には利用するフィールド名を list or tuple 形式で定義する。
        # すべてのフィールドを利用する場合は "__all__" という文字列を指定しても良い。
        # 利用しないフィールドを指定する場合は、fields の代わりにに exclude を使用する。
        fields = [
            "id",
            "title",
            "price",
            # Book モデルには存在しないが、レスポンスに追加したいフィールド
            "price_with_tax",
            # Book を取得する API で一緒に取得したい Book モデルの関連モデルのフィールド
            "publisher_name",
            # Book モデルの ManyToManyField である Author がネストされて取得できる。
            "authors",
        ]

        # extra_kwargs を使用することでフィールドオプション定義を上書きすることもできる。
        #
        # 例：
        # extra_kwargs = {
        #    "title": {
        #        "write_only": True,
        #        "max_length": 10,
        #    }
        # }

    # シリアライザの Field クラスには、それぞれの Field クラスに
    # 対応した「フィールドオプション」と呼ばれる属性が設定されており、それによってフィールドの
    # 特性が規定される。主な例は下記の通り。
    #
    # - write_only: 登録・更新・一部更新時の入力フィールドには含めるが、出力用フィールドには
    # 含めない場合に True を指定する、。
    # - read_only: 出力用フィールドには含めるが、登録・更新・一分更新時の入力用フィールドには
    # 含めない場合に True を指定する。
    # - required: 入力データにフィールドが指定されなかった場合にバリデーション結果を NG にするかどうか。
    # default オプションが設定されている場合や read_only=True の場合は required=False となる。
    # デフォルト値は True（フィールド必須）である。
    # - default: 登録・更新時にフィールドが指定されなかったときに使われるデフォルト値。
    # ただし、一部更新のときには使用されない。
    # - allow_null: 入力時に null を許容するかどうか。デフォルト値は False。
    # - allow_blank: 入力値に空文字を許容するかどうか。CharField などで使用可能。
    # - source: 値を出力する際の参照先をデフォルトから変更したい場合に使用する。
    # 関連モデルの属性をドット区切りで指定することもできる。
    # - max_length: CharField などのバリデーションで指定される最大長さ。
    # - min_length: CharField などのバリデーションで指定される最小長さ。
    # - max_value: IntegerField や FloatField のバリデーションで使用される最大値。
    # - min_value: IntegerField や FloatField のバリデーションで使用される最小値。
    # - validators: 文字種チェックなどのバリデーション。list や tuple で指定する。
    # - error_messages: バリデーション結果が NG である場合のエラーメッセージ。dict で指定する。
    #
    # 例：
    # price = serializers.CharField(read_only=True)

    # SerializerMethodField を用いて出力専用の戻り値を出力する。
    def get_price_with_tax(self, instance) -> Optional[int]:
        if not instance.price:
            return None
        return int(Decimal(instance.price) * Decimal(1 + TAX_RATE))
