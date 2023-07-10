class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # metodos normais que recebe self
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password
        # metodos setters (que setam algo)

    @classmethod
    # classmethod não usa self e recebe cls = class
    def creat_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    # metodo que não tem acesso as informações das classes
    # meio inutil...
    def log(msg):
        print('LOG', msg)


c1 = Connection.creat_with_auth('luiz', '12345')


# c1.set_user('luiz')
# c1.set_password('132578')
# print(c1.user)
