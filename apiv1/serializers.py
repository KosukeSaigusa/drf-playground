from rest_framework import serializers

from shop.models import Book


# ModelSerializer を継承することで、モデルのフィールド定義を再利用することができ、
# モデルの定義に基づいた型変換やバリデーションが行われるので、シリアライザの
# 記述量を大幅に減らすことができる。
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # Meta クラスの model に対象のモデルクラスを定義する。
        model = Book

        # Meta クラスの fields には利用するフィールド名を list or tuple 形式で定義する。
        # すべてのフィールドを利用する場合は "__all__" という文字列を指定しても良い。
        # 利用しないフィールドを指定する場合は、fields の代わりにに exclude を使用する。
        fields = ["id", "title", "price"]

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
