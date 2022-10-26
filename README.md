# DRF playground

## Setup

[poetry](https://python-poetry.org/docs/) のインストール

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

[pyenv](https://github.com/pyenv/pyenv) のインストール

```shell
brew update
brew install pyenv
```

リポジトリのクローン

```shell
cd workspace
gh repo clone KosukeSaigusa/drf-playground
```

仮想環境 (.venv) の作成、依存パッケージのインストール

```shell
cd drf-playground
poetry install
```

依存パッケージの追加・削除

```shell
# パッケージの追加
poetry add <package-name>

# パッケージの追加 (dev dependencies)
poetry add <package-name> --dev

# パッケージの削除
poetry remove <package-name>
```

マイグレーション

```shell
# マイグレーションの適用状況の確認
.venv/bin/python3 manage.py showmigrations --database=<データベース名>

# マイグレーションファイルの生成
.venv/bin/python3 manage.py makemigrations <アプリケーション名>

# マイグレーションの実行
.venv/bin/python3 manage.py migrate <アプリケーション名> --database=<データベース名>

# 指定したマイグレーション状態にロールバック
.venv/bin/python3 manage.py migrate <アプリケーション名> <マイグレーションファイルの ID>

# マイグレーションで実行される SQL を事前に確認
.venv/bin/python3 manage.py sqlmigrate <アプリケーション名> <マイグレーションファイルの ID>
```
