"""
初始化数据库表文件
"""
from server import Base, engine
from model.testcase_model import TestcaseModel
from model.user_model import UserModel



if __name__ == '__main__':
    # 删除所有数据
    # Base.metadata.drop_all(bind=engine)
    # 创建表，需要传入创建连接的对象
    Base.metadata.create_all(bind=engine)