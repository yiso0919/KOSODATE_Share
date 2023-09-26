from app import app, db
import shutil

# 削除するディレクトリのパス
# dir_path = "./instance"
# インスタンスディレクトリを削除
# shutil.rmtree(dir_path)


with app.app_context():
    db.create_all()

print("Database and tables created!")
