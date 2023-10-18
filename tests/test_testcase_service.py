from model.testcase_model import TestcaseModel
from service.testcase_service import TestcaseService


class TestTestcaseService:

    def setup_class(self):
        self.testcase_service = TestcaseService()

    def create(self):
        testcase = TestcaseModel(
            name="测试用例99",
            step="打开浏览器,\n 输入百度网址\n",
            method="手工",
            remark="进行百度网站打开测试"
        )
        self.case_id = self.testcase_service.create(testcase)

    def delete_case(self):
        if self.testcase_service.get(self.case_id):
            self.testcase_service.delete(self.case_id)

    def setup(self):
        self.create()

    def teardown(self):
        self.delete_case()

    def test_create(self):
        case_id = self.case_id
        print(case_id)
        assert case_id

    def test_update(self):
        testcase = TestcaseModel(
            id=self.case_id,
            name="测试用例99_update",
            step="打开浏览器,\n 输入百度网址\n",
            method="手工",
            remark="进行百度网站打开测试"
        )
        case_id = self.testcase_service.update(testcase)
        print(case_id)
        assert case_id

    def test_delete(self):
        case_id = self.case_id
        after_case_id = self.testcase_service.delete(case_id)
        print(after_case_id)
        assert after_case_id

    def test_list(self):
        case_list = self.testcase_service.list()
        print(case_list)
        assert len(case_list)

    def test_get(self):
        case = self.testcase_service.get(self.case_id)
        print(case)
        assert case.id
