from handlers import config_handler


class LogHelper:
    def __init__(self):
        self.allowed_log_levels = ["DEBUG", "INFO", "WARN"]
        self.conf_handler = config_handler.ConfigHandler()

    def write_log(self, log_level, log_message):
        if self.conf_handler.get_value("development", "debug") != "True" and log_level.lower() == "debug":
            return False

        log_level = log_level.upper()
        if log_level in self.allowed_log_levels:
            print(log_level + ": " + log_message)
