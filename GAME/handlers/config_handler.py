import configparser
import os


class ConfigHandler:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.path.join("") + "config.ini")

    def get_value(self, section, key):
        # Checking to see if the section is actually a section in the config file.
        if section not in self.config.sections():
            print("Error: section not found")
            raise KeyError
        # Checking to see if the key exists in the given section.
        elif key not in self.config[section].keys():
            print("Error: key not found in section")
            raise KeyError
        return self.config[section][key]

    def set_value(self, section, key, value):
        if section not in self.config.sections():
            print("Error: section not found")
            raise KeyError
        elif key not in self.config[section].keys():
            print("Error: key not found in section")
            raise KeyError

        self.config[section][key] = value

        # Actually writing to the config file
        with open("config.ini", "w") as configfile:
            self.config.write(configfile)
