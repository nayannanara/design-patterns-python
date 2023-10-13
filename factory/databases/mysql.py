from factory.interface.database import DatabaseInterface


class MysqlRepository(DatabaseInterface):
    def select_one(self) -> dict:
        return {
            'success': True,
            'data': 'olá mundo'
        }