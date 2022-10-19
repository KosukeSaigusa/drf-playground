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
poetry add <package-name>
poetry add <package-name> --dev
poetry remove <package-name>
```
