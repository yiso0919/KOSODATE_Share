from flask import Flask, render_template, redirect, url_for, request
from models import db, Question, Answer  # モデル関連
from datetime import datetime  # 日時を扱うためのモジュール
from sqlalchemy import or_
import pytz
import base64
from chat_ai import chat_answer

# Flaskのアプリケーションインスタンスの作成
app = Flask(__name__)

# データベースの設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qa.db'

# データベースの初期化
db.init_app(app)

japan_timezone = pytz.timezone('Asia/Tokyo')

# トップページのルート設定
@app.route('/')
def index():
    # クエリパラメータ 'search' の値を取得
    search_text = request.args.get('search')
    
    # 検索テキストが指定されている場合、該当する質問を検索
    if search_text:
        questions = Question.query.filter(or_(Question.title.contains(search_text), Question.content.contains(search_text))).order_by(Question.timestamp.desc()).all()
    else:
        questions = Question.query.order_by(Question.timestamp.desc()).all()
    
    return render_template('index.html', questions=questions)

# 質問投稿ページのルート設定
@app.route('/question', methods=['GET', 'POST'])
def post_question():
    ####
    #質問投稿処理
    ####
    if request.method == 'POST':
        # 質問のデータベースと回答のデータベース両方に追加する
    
        # フォームからタイトルと内容を取得
        title = request.form['title']
        content = request.form['content']
        
        # 質問用データベース
        # 現在の日時を取得
        current_time = datetime.now(japan_timezone)
        file = request.files['uploaded_image']
        image_binary_data = file.read()
        image_encoded = base64.b64encode(image_binary_data).decode('utf-8')
        # Questionインスタンスの作成
        question = Question(title=title, content=content, timestamp=current_time, image_data=image_encoded)
        # データベースセッションに質問を追加し、コミット
        db.session.add(question)
        db.session.commit()
        
        
        # 回答データベース
        print("チャットGPTに入力します")
        response_text = chat_answer(content)
        print("質問投稿処理回答",response_text)
        
        #chatgpt
        answer = Answer(content=response_text, question_id=question.id)
        # question = Question.query.get(id)
        db.session.add(answer)
        # データベースセッションに回答を追加し、コミット
        db.session.commit()
        return redirect(url_for('index'))

    
    return render_template('post_question.html')

# 質問詳細ページのルート設定
@app.route('/question/<int:id>')
def question_detail(id):
    # 指定されたIDの質問をデータベースから取得（存在しない場合は404エラーを返す）
    question = Question.query.get_or_404(id)
    # 質問の詳細をHTMLで表示
    return render_template('question_detail.html', question=question)

# 質問詳細ページのルート設定
@app.route('/question_and_answer/<int:id>')
def question_and_answer(id):
    # 指定されたIDの質問をデータベースから取得（存在しない場合は404エラーを返す）
    question = Question.query.get_or_404(id)
    return render_template('question_and_answer.html', question=question)

# 回答投稿のルート設定
@app.route('/answer/<int:id>', methods=['POST'])
def post_answer(id):
    # フォームから回答内容を取得
    content = request.form['content']
    # Answerインスタンスの作成
    answer = Answer(content=content, question_id=id)
    #
    selected = request.form.getlist('option')
    print(selected)
    if len(selected) == 1:
        ex_answer_content = "保育士" + content
        ex_answer = Answer(content=ex_answer_content, question_id=id)
        db.session.add(ex_answer)
    else:
        ex_answer_content = "一般" + content
        ex_answer = Answer(content=ex_answer_content, question_id=id)
        db.session.add(ex_answer)  

    current_time = datetime.now(japan_timezone)
    question = Question.query.get(id)
    question.timestamp = current_time
    # データベースセッションに回答を追加し、コミット
    db.session.commit()
    # 質問詳細ページへリダイレクト
    return redirect(url_for('question_and_answer', id=id))

# AIお悩み相談ページのルート設定
@app.route('/aianswer',methods=['GET','POST'])
def ai_process():
    result = None
    flag = False
    if request.method == "POST":
        input_text = request.form['input_text']
        flag = True
        result = chat_answer(input_text)
        flag = False
    return render_template('ai_answer.html',result=result, flag=flag)

# スクリプトとして実行された場合の処理
if __name__ == '__main__':
    app.run(debug=True)
