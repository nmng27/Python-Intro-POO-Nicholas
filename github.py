# A gente vai simular um cadastro de informações 
from datetime import datetime, date, timedelta
class Login:
    
    def __init__(self,nome,sobrenome,email,user,rua,bairro,cidade,estado,senha,dia,mes,ano) -> None:
        self.__nome = nome 
        self.__sobrenome = sobrenome
        self.__email = email 
        self.__user = user
        self.__rua = rua
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__dia = dia 
        self.__mes = mes 
        self.__ano = ano 
        self.__senha = senha
    
    # Agora vamos trabalhar com as funções get e set para trazer o nome do usuario e caso ele queira alterar o nome 
    
    # Obtendo o nome completo do usuario
    def get_nome_completo(self):
        return self.__nome + " " + self.__sobrenome
    
    #  Trabalhando com email 
    def get_email(self):
        return self.__email
    def set_email(self,novo_email):
        self.__email = novo_email

    # Trabalhando com endereços 
    def get_endereco(self):
        return self.__rua + ", " + self.__bairro + ", " + self.__cidade + ", " + self.__estado
    def set_endereco(self,nova_rua,novo_bairro,nova_cidade,novo_estado):
        self.__rua = nova_rua
        self.__bairro = novo_bairro
        self.__cidade = nova_cidade
        self.__estado = novo_estado
    
    # Trazendo a data 
    def get_dt_nasc(self):
        from datetime import datetime, date, timedelta
        dt_nasc = date(self.__ano,self.__mes,self.__dia)
        return dt_nasc
    
    # Pegando a senha 

    def get_senha(self):
        return self.__senha
    
    
    # trazendo o usuário
    def get_user(self):
        return self.__user 
    
    #  Alterando o user
    def set_user(self,novo_user):
        self.__user = novo_user
    
    # Alterando a senha 
    def set_senha(self,nova_senha):
        tamanho = len(nova_senha)
        check_senha = nova_senha.capitalize()
        if (tamanho > 8 and tamanho < 16) and (nova_senha == check_senha):
            print("Senha cadastrada")
            self.__senha = nova_senha
        else:
            print(f"Senha não cadastrada")