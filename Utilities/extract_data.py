import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def get_url():
        url = config.get('common data', 'base_url')
        return url

    @staticmethod
    def get_username1():
        username=config.get('common data', 'username1')
        return username

    @staticmethod
    def get_password1():
        password=config.get('common data', 'password1')
        return password

    @staticmethod
    def get_username2():
        username = config.get('common data', 'username2')
        return username

    @staticmethod
    def get_password2():
        password = config.get('common data', 'password2')
        return password
