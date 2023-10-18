from flask import Flask
from flask_bootstrap import Bootstrap
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

# 实例化 app
app = Flask(__name__)
# 把 app 实例传入 Bootstrap 类中
Bootstrap(app)


# SQLAlchemy 设置
Base = declarative_base()
# 定义数据库
db_host = "127.0.0.1"  # MySQL主机名
db_port = "3306"  # MySQL端口号，默认3306
db_name = "testplatform"  # 数据库名称
db_user = "root"  # 数据库用户名
db_pass = "mysql123456789"  # 数据库密码
# 数据库类型+数据库引擎（ pip install pymysql）
db_url = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
# 创建引擎，连接到数据库
# engine = create_engine('sqlite:///data.db', echo=True)
engine = create_engine(db_url, echo=True)
# 创建session对象
DBSession = sessionmaker(bind=engine)
db_session: Session = DBSession()

# 定义路由与视图函数
@app.route("/")
def index():
    # return "霍格沃兹测试管理平台"
    # 跳转到测试用例列表展示接口
    return redirect(url_for("user.login"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)