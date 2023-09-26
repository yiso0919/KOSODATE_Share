# KOSODATE Share

KOSODATE share 匿名のコミュニケーションで子育ての悩みや課題を気楽に解決する場を提供。保護者同士の共有と保育士およびAIによる回答でサポートします。
とある会社の5日インターンで優勝した作品であり，開発メンバー初対面で，1から開発した作品になります．


# 作品概要

投稿一覧画面はこのようになっています．
モバイルでの操作に最適化されており，タイトルや相談内容の一部を見れるようになっています

<img width="314" alt="スクリーンショット 2023-09-01 170254" src="https://github.com/TogoTarogit/BIPROGY/assets/62383281/d2b3ec38-606a-483b-b92a-f5e5ef9e7123">

質問投稿画面はこのようになっています．

<img width="318" alt="スクリーンショット 2023-09-01 170430" src="https://github.com/TogoTarogit/BIPROGY/assets/62383281/1eccb7e8-9f49-439b-88f8-ae6b1ae7defc">

投稿に対してAIが自動で応答するようになっています

<img width="312" alt="スクリーンショット 2023-09-01 170541" src="https://github.com/TogoTarogit/BIPROGY/assets/62383281/18404af9-24ff-4e94-8d03-86c0abb6dd90">

また，投稿に対して他の人が返信することも可能であり，投稿者の保育士かどうかのタグや個人を識別する機能を実装しています

<img width="293" alt="スクリーンショット 2023-09-01 175324" src="https://github.com/TogoTarogit/BIPROGY/assets/62383281/7d818961-0dee-444f-af66-28a392ed972a">

また，保育に対して最適化されたAI相手に相談することも可能です

<img width="326" alt="スクリーンショット 2023-09-01 170626" src="https://github.com/TogoTarogit/BIPROGY/assets/62383281/059751ce-a564-4578-ba63-16aad326d6c2">


## 環境構築

### 1. 仮想環境の設定
**特別必要な物**: OPENAI_API_KEY

```bash
python3 -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

python3 setup_db.py

flask run
```

### 2. エラーの解決方法

- `no such column: question.timestamp` エラーが出る場合：
  このエラーは，データベースの `question` テーブルに `timestamp` カラムが存在しない場合に発生します．`setup_db.py` を実行してデータベーススキーマを更新するか，SQLクエリを修正してください．また，このディレクトリを削除することで解決するかもしれません： `instance/`

必要なライブラリをインストールするには以下のコマンドを実行してください：

```bash
pip install -r requirements.txt
```

`config.py` ファイルで必要な変数を設定してください．

## 使用技術

- HTML
- CSS
- Bootstrap
- Python
- Flask
- SQLite3
- OpenAI API
- その他...

以上の手順に従って，KOSODATE Shareの環境を設定し，お悩み相談サービスを提供できるようになります．

##　ディレクトリ構成
- Name                     Description                               Mode
- ----                     -----------                               ----
- readme.md                Readmeファイル                            -a----
- instance                 データベースを保存します                    d-----
- static                   ジャバスクリプトの保存先                     d-----
- templates                html の保存先                              d-----
- venv                     仮想環境性ってい                            d-----
- .gitignore               Gitの無視ファイルリスト                       -a----
- app.py                   データベース通信                            -a----
- chat_ai.py               AIのモデル設定                             -a----
- config.py                設定ファイル                               -a----
- dummy_db.py              ダミーデータの作成ファイル                    -a----
- models.py                データベースのモデル                         -a----
- requirements.txt         必要なライブラリ                            -a----
- setup_db.py              データベース立ち上げ                         -a----

## Contribution 

# TOGO (https://github.com/TogoTarogit)
- ChatGPTと回答の連携や保育士として質問に寄り添うよう調整
- ユーザー登録機能
- Git の管理を担当

# 礒崎　(https://github.com/yiso0919)
- 画像ファイルを添付していない時のバグ修正
- 回答一覧のデザイン
- その他バグ調整、デザインの改良
  
# 片山　(https://github.com/RikutoKatayama)
- プロジェクトのマネジメント（役割の振り分け・管理，機能の取捨選択？など）
- スプリントバックログの詳細決定
- DB属性の設定

# 辻村 (https://github.com/Umadachi564)
- ChatGPT APIの導入
- 各画面のプロトタイプデザインの実装
- Bootstrap5の導入支援

# 若崎　(https://github.com/keiwakasaki)
- デザインを考えて共有する
- Flaskでバックエンドの大枠作成
- 検索機能や画像投稿機能の実装

# 根津	(https://github.com/Nezu4280)
- 画面遷移の機能の実装およびデザインの改良
- 相談内容の短縮表記
- 回答者の識別

