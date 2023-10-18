from flask import Blueprint, request, render_template, redirect, url_for



from utils.log_utils import logger

user_bp = Blueprint("user", __name__, url_prefix="/user")


@user_bp.route("/register", methods=["get", "post"])
def register():
    '''
    注册功能
    '''
    if request.method == "POST":
        # 接收表单格式的请求体
        user_info = request.form
        logger.info(f"注册接口获取到的请求体为 {user_info}")
        username = user_info.get("username")
        password = user_info.get("password")
        # 如果用户名或者密码为空
        if not username or not password:
            logger.info("用户名或者密码为空")
            return render_template("register.html")
        from service.user_service import UserService
        user_service = UserService()
        # 先查询当前用户名是否存在
        if user_service.get(username):
            logger.info("用户已经存在")
            return render_template("register.html")
        # 当用户不存在，生成用户对象
        from model.user_model import UserModel
        user = UserModel(username=username, password=password)
        # 写入数据库
        user_service.create(user)
        # 注册成功后，进入登录页面
        return render_template("login.html")

    return render_template("register.html")


@user_bp.route("/login", methods=["get", "post"])
def login():
    '''
    登录功能
    '''
    if request.method == "POST":
        # 获取请求体数据
        user_info = request.form
        username = user_info.get("username")
        password = user_info.get("password")
        if not username or not password:
            logger.info("用户名或密码为空")
            return render_template("login.html")
        # 通过用户名查询
        from service.user_service import UserService
        user_service = UserService()
        user_result = user_service.get_by_name(username)
        if not user_result:
            logger.info("用户不存在")
            return render_template("login.html")
        # 判断用户输入的密码和表中密码是否一致
        if not user_result.check_hash_password(password):
            logger.info("密码错误，登录失败")
            return render_template("login.html")
        # 密码一致，登录成功，跳转到测试用例页面
        return redirect(url_for("case.get_case"))
    return render_template("login.html")