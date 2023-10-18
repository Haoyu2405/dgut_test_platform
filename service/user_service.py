from dao.user_dao import UserDao
from model.user_model import UserModel

user_dao = UserDao()


class UserService:

    def get(self, user_id) -> UserModel:
        '''
        通过 ID 查询用户
        '''
        return user_dao.get(user_id)

    def get_by_name(self, user_name):
        '''
        通过姓名查询用户
        '''
        return user_dao.get_by_name(user_name)

    def create(self, user_model: UserModel) -> int:
        '''
        创建用户
        '''
        # 新增前先查询用户是否存在
        user = user_dao.get_by_name(user_model.username)
        if not user:
            # 没有重名，创建用户
            user_dao.create(user_model)
            return user_model.id