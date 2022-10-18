from django.contrib import admin

from shop.models import Book


class BookModelAdmin(admin.ModelAdmin):

    list_display = ("title", "price", "created_at")
    ordering = ("-created_at",)
    readonly_fields = ("id", "created_at")


# 参考
# https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#modeladmin-objects
# https://docs.djangoproject.com/ja/4.1/intro/tutorial07/
# ModelAdmin はカスタマイズして定義しなければ、
# admin.site.register(Book) とするだけでデフォルトの Admin インターフェースが
# 提供される。
#
# ```python
# @admin.register(Book)
# class BookModelAdmin(admin.ModelAdmin):
#     pass
# ```
#
# というように register デコレータを使用して記述することもできる。
admin.site.register(Book, BookModelAdmin)
