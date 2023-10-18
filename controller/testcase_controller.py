# # 导入 Flask 的模块
from flask import Blueprint, request, render_template, redirect, url_for


from utils.log_utils import logger

case_bp = Blueprint("case", __name__, url_prefix="/testcase")


# 查询用例
@case_bp.route("")
def get_case():
    from service.testcase_service import TestcaseService
    testcase_service = TestcaseService()
    cases = testcase_service.list()
    # return cases
    return render_template("testcase.html", testcase_list=cases)


@case_bp.route("/add", methods=["POST"])
def add_case():
    # 接收表单格式请求体中的数据
    case_info = request.form
    logger.info(f"接收到的请求体为 {case_info}")
    from model.testcase_model import TestcaseModel
    testcase = TestcaseModel(**case_info)
    from service.testcase_service import TestcaseService
    testcase_service = TestcaseService()
    # 把测试用例数据写入数据库
    testcase_service.create(testcase)
    logger.info("测试用例添加成功")
    # 跳转到测试用例列表展示接口
    return redirect(url_for("case.get_case"))


@case_bp.route("/delete/<case_id>")
def delete_case(case_id):
    logger.info(f'要删除的测试用例 ID 为 {case_id}')
    # 解决循环导入的问题
    from service.testcase_service import TestcaseService
    testcase_service = TestcaseService()
    # 调用 service 中的删除方法
    testcase_service.delete(case_id)
    # 跳转到测试用例列表展示接口
    return redirect(url_for("case.get_case"))


@case_bp.route("/update/<case_id>", methods=["GET", "POST"])
def update_case(case_id):
    logger.info(f"要更新的测试用例 ID 为 {case_id}")
    from service.testcase_service import TestcaseService
    testcase_service = TestcaseService()
    logger.info(f"当前请求方法为 {request.method}")

    if request.method == "POST":
        case_info = request.form
        logger.info(f"获取到的请求体为 {case_info}")
        # 获取表单格式请求体，生成测试用例对象
        # 构造测试用例对象
        from model.testcase_model import TestcaseModel
        testcase = TestcaseModel(**case_info)
        logger.info(f"构造出来的测试用例对象为 {testcase}")
        # 调用更新方法，写入更新后的数据
        testcase_service.update(testcase)
        # 跳转到测试用例列表展示接口
        return redirect(url_for("case.get_case"))
    # 如果不是 post 请求，则完成页面展示
    # 通过用例 ID 查询用例
    case = testcase_service.get(case_id)
    return render_template("update_testcase.html", testcase=case)