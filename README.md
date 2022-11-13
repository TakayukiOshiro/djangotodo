参考
https://tech-diary.net/django-todo-tutorial/

# 1.環境構築(python)

powerShellで　`python -V` を行い、バージョンが帰ってきたらインストール済み<br>
そうでなければ、[公式の](https://www.python.jp/python_vscode/windows/index.html)手順で行けると思う
<br>
<br>

# 2.環境構築(django)
https://tech-diary.net/django-todo-tutorial/<br>


# 3.プロジェクト作成
powerShell で `$ django-admin startproject [プロジェクト名] .`を入力<br>
<br>
実行したディレクトリにプロジェクトフォルダが作成される<br>
このディレクトで`$ python manage.py runserver`でサーバー起動後、`http://localhost:8000`にアクセスするとロケットが発射されるページが出る<br>
<br>

# 4.アプリ作成
powershell で`$ python manage.py startapp [アプリディレクトリ名]`入力でアプリのフォルダが作成される<br>
プロジェクトは、webサイトの構成とアプリのコレクション<br>
アプリは何かを行うアプリケーション<br>
例) YouTube<br>
    プロジェクト：YouTube<br>
    アプリケーション：動画投稿、動画視聴、動画配信、etc (=具体的なサービス機能のニュアンス？)<br>
<br>

# 4.初期設定
アプリの登録を行う<br>
/[アプリディレクトリ名]/setting.pyの`INSTALLED_APPS`に`[アプリディレクトリ名].apps.[アプリディレクトリ名]config`を追加<br>

言語とタイムゾーンの変更<br>
`LANGUAGE_CODE` と `TIME_ZONE` を変更する<br>


# 5.Hello World する
`config/urls.py`<br>
を以下のようにする<br>

<pre>

from django.contrib import admin
from django.urls import path, include # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("[アプリ名].urls")) # 追加
]

</pre>

変更後、アプリディレクトリに新しくviews.pyを作る<br>
ソースは以下<br>
<pre>

from django.shortcuts import render # 最初これだけ
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("＜h1＞Hello World＜/h1＞")// 表示上の関係で<と>を全角にしてる

</pre>

その後、同ディレクトリにurls.pyを作る<br>
<pre>

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),// トップページにアクセスしたら、views.pyのindex()がコールされる
]

</pre>

# 6.モデル作成とマイグレーション
djangoではModelを定義すると、SQLを書かずにデータベースで使うテーブルを作成できる<br>

## models.pyでモデルを定義する
こんな感じ<br>

<pre>

from django.db import models # 最初はこれだけ

# Create your models here.
class Todo(models.Model):
    title = models.CharField("タスク名", max_length=30)
    description = models.TextField("詳細", blank=True)
    deadline = models.DateField("締切")

    def __str__(self):
        return self.title

</pre>

## マイグレーションファイル作成
powershellで`$ python manage.py makemigrations`を入力<br>

## テーブル作成
powershellで`$ python manage.py migrate`を入力<br>

# 7.管理画面設定とタスク登録

## 管理者ユーザーを作る
powershellで`$ python manage.py createsuperuser`を入力<br>
ユーザー名、パスワードは必須入力<br>

サーバーを立ち上げて、http://localhost:8000/admin にアクセスすると、データベースにアクセスできる(django独自らしい?)<br>

管理画面で確認したいテーブルを追加する<br>
/アプリ名/admin.pyに追加<br>
<pre>
from django.contrib import admin
from .models import Todo

# Register your models here.
admin.site.register(Todo)

</pre>

# 機能開発の流れ
1. アプリ名/view.pyでロジック作成
2. アプリ名/urls.pyでURL設定(ルーティング)
3. HTML編集

# 8. Todoタスクを表示させる
view.py<br>
<pre>
from django.shortcuts import render
from django.views.generic import ListView

from .models import Todo


class TodoList(ListView):
    model = Todo // model.pyで作成したTodoクラス
    context_object_name = "tasks" // htmlに表示するときに使う変数名
</pre>

urls.py<br>
<pre>
from django.urls import path
from .views import TodoList

urlpatterns = [
    path("", TodoList.as_view(), name="list"),
]

</pre>

htmlを保存するフォルダは/アプリ名/templates/アプリ名/.htmlになる<br>
今回はtodo_list.htmlになる（どうしてかは勉強中<br>

```

<h1>Todo List</h1>

<table>
    <thead>
        <tr>
        <th scope="col">title</th>
        <th scope="col">deadline</th>
        </tr>
    </thead>
    <tbody>
    {% for task in tasks %}
    <tr>
        <td>{{ task.title }}</td>
        <td>{{ task.deadline }}</td>
    </tr>
    {% endfor %}
    </tbody>
</table>

```