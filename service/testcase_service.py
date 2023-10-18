from typing import List
from dao.testcase_dao import TestcaseDao
from model.testcase_model import TestcaseModel

# 实例化测试用例实体类
testcase_dao = TestcaseDao()


class TestcaseService:
    def create(self, testcase_model: TestcaseModel) -> int:
        """
        创建用例
        """
        result = testcase_dao.get_by_name(testcase_model.name)
        if not result:
            return testcase_dao.create(testcase_model)

    def update(self, testcase_model: TestcaseModel) -> int:
        """
        更新用例
        """
        if testcase_dao.get(testcase_model.id):
            testcase_dao.update(testcase_model)
        return testcase_model.id

    def delete(self, testcase_id: int) -> int:
        """
        删除用例
        """
        if self.get(testcase_id):
            return testcase_dao.delete(testcase_id)

    def list(self) -> List[TestcaseModel]:
        """
        获取全部用例
        """
        return testcase_dao.list()

    def get(self, testcase_id: int) -> TestcaseModel:
        """
        获取某个测试用例
        """
        return testcase_dao.get(testcase_id)