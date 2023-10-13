from factory.usecase.usecase import Usecase
from factory.databases.mysql import MysqlRepository

class MysqlFactory:
    
    @staticmethod
    def create() -> Usecase:
        return Usecase(MysqlRepository())