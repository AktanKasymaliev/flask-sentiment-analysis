from configparser import ConfigParser, NoOptionError, NoSectionError
import os

def load_conf(config: ConfigParser, section: str, name: str, default=None) -> str:
    try:
        output = config.get(section, name)
    except (NoOptionError, NoSectionError) as e:
        output = default
    return output

def config() -> None:
    config_parse = ConfigParser()
    config_parse.read("settings.ini")
    SYSTEM = "SYSTEM"

    #SYSTEM
    os.environ.setdefault("FLASK_DEBUG", load_conf(config_parse, SYSTEM, "FLASK_DEBUG", "False"))
    os.environ.setdefault("FLASK_KEY", load_conf(config_parse, SYSTEM, "FLASK_KEY", "super_secret_key"))
    os.environ.setdefault("FLASK_HOST", load_conf(config_parse, SYSTEM, "FLASK_HOST", "super_secret_key"))