from model.user_model import UserModel
from service.user_service import UserService


class TestTestUserService:

    def setup_class(self):
        self.user_service = UserService()

    def create(self):
        user = UserModel(
            username="user_create_99",
            password="123456"
        )

    def test_get(self):
        assert False

    def test_get_by_name(self):
        assert False

    def test_create(self):
        assert False
