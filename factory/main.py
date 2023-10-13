from factory.factories.mysql_factory import MysqlFactory

usecase = MysqlFactory.create()
response = usecase.do_something()

print(response)