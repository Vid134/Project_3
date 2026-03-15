# import configparser to read config.ini files
import configparser

# create ConfigParser object
config = configparser.ConfigParser()

# read config.ini file
config.read("config.ini")


class ConfigReader:
    """
    Utility class to read values from config.ini
    """

    @staticmethod
    def get_base_url():
        # return base URL from config file
        return config.get("environment", "base_url")

    @staticmethod
    def get_browser():
        # return browser name from config file
        return config.get("environment", "browser")

    @staticmethod
    def get_timeout():
        # return timeout value
        return config.getint("environment", "timeout")

    @staticmethod
    def get_username():
        # return default username
        return config.get("credentials", "username")

    @staticmethod
    def get_password():
        # return default password
        return config.get("credentials", "password")