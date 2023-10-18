# 测试用例模型
# model/testcase_model.py

from sqlalchemy import Column, Integer, String
from server import Base


class TestcaseModel(Base):
    """
        测试用例的数据模型
    """

    __tablename__ = 'testcase'

    # 用例id，主键，唯一
    id = Column(Integer, primary_key=True)
    # 用例标题，不为空，并且唯一
    name = Column(String(80), nullable=False, unique=True)
    # 用例步骤
    step = Column(String(260))
    # 用例的自动化方法或手工执行方法
    method = Column(String(120))
    # 备注
    remark = Column(String(120))

    def __repr__(self):
        # 数据库的 魔法方法 直观展示数据
        '''[<User "xxxx">,<User "yyyy">]'''
        return '<Testcase %r>' % self.name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "step": self.step,
            "method": self.method,
            "remark": self.remark,
        }
