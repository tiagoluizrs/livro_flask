from model.User import User

class UserController():
    def __init__(self):
        self.user_model = User()

    def login(self, email, password):
        self.user_model.email = email
        password = self.user_model.hash_password(password)
        
        result = self.user_model.get_user()
        if result is not None:
            res = self.user_model.verify_password(password, result.password) 
            if res:
                return result
            else:
                return []
        return []
        
    def recovery(email):
        """
        A recuperação de e-mail será criada no capítulo 12. Trabalhando com serviços de e-mail
        """
        return ''