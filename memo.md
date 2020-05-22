# Docker Command

docker-compose build
docker-compose up -d

docker exec -it backend bash
docker exec -it frontend sh

npx create-nuxt-app nuxtproject



delete mode 100644 frontend/src/nuxtproject/.babelrc
delete mode 100644 frontend/src/nuxtproject/jest.config.js
delete mode 100644 frontend/src/nuxtproject/package-lock.json
delete mode 100644 frontend/src/nuxtproject/test/Logo.spec.js

# Required documentation

画面遷移図
要件定義書
テーブル定義書
ユースケース図
シーケンス図
テスト項目書
関数仕様書

# Use case

会員
    ログインする
    投稿する
    閲覧する
    編集する
    削除する
    フォローする
    コメントする

非会員
    登録する

## Use case senario

非会員は登録する。
登録の際にメールアドレスとパスワードを設定する。

会員はログイン後に
プロフィールの更新ができる。

記事の
閲覧、
投稿、
編集、
削除
ができる。

他ユーザーをフォローできる。
他ユーザーの記事にコメントができる。

## 名詞

ユーザー、非会員、登録、メールアドレス、パスワード、設定、会員、ログイン、プロフィール、更新、記事、閲覧、投稿、編集、削除、他ユーザー、フォロー、コメント

---

とい合わせ

何を持って

かんたんな

1.thanks
2.thanks + DB
3.パソコン + SP のDB 同じ条件

---

ユーザーシナリオ：
# のび太は新しいto-doアプリがあると聞いてそのホームページにアクセスした。
# のび太はページのタイトルがとヘッダーがto-doアプリであることを示唆していることを確認した。
# のび太はto-doアイテムを記入するように促され、
# のび太は「どら焼きを買うこと」とテキストボックスに記入した(彼の親友はどら焼きが大好き)
# のび太がエンターを押すと、ページは更新され、
# "1: どら焼きを買うこと"がto-doリストにアイテムとして追加されていることがわかった
# テキストボックスは引続きアイテムを記入することができるので、
# 「どら焼きのお金を請求すること」を記入した(彼はお金に関してはきっちりしている)
# ページは再び更新され、新しいアイテムが追加されていることが確認できた
# のび太はこのto-doアプリが自分のアイテムをきちんと記録されているのかどうかが気になり、
# URLを確認すると、URLはのび太のために特定のURLであるらしいことがわかった
# のび太は一度確認した特定のURLにアクセスしてみたところ、
# アイテムが保存されていたので満足して眠りについた。


テストケース：
# <html>で始まっているか？
# <html>で終わっているか？
# <title>が正しいか？
# <keyword>が正しいか？
# <description>が正しいか？
# <h1>が入っているか？
# <h2>が入っているか？
# 正しいtemplateが使われているか？
# status codeが正しいか？（200, 302）
# 遷移先が正しいか？（200, 302）
# POSTでデータが保存されているか？
# Modelにデータが保存されているか？
# Modelからデータが取り出せているか？
# 
# 
# 
# 
# 
# 
# 
# 
# 


