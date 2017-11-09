class LogHelper:
    def __init__(self):
        self.allowed_log_levels = ["DEBUG", "INFO", "WARN"]

    def write_log(self, log_level, log_message):
        log_level = log_level.upper()
        if log_level in self.allowed_log_levels:
            print(log_level + ": " + log_message)
