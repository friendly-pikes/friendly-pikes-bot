import json
import os

from utils.semifunc import *
from utils.custom.context import Context
# So we don't copy code 24/7 for diffrent files


def open_file(dir, filename, fileext):
    file = None
    filepath = os.path.abspath(f"{dir}/{filename}.{fileext}")

    with open(filepath) as raw:
        file = json.loads(raw.read())

    return file

def get_filepath(filename, fileext):
    filepath = os.path.abspath(f"misc/{filename}.{fileext}")
    return filepath

def get_config_entry(entry: str):
    return _config()[entry]


def _config():
    return open_file("misc", "config", "json")

def _banished():
    return open_file("misc", "banished", "json")

def _radar_ignore_force():
    return open_file("misc", "radar_forced_ignore", "json")


def get_random_topic():
    topics = get_config_entry("topics")
    rand = random.choice(topics)
    
    return rand

def get_emoji_ids(ctx):
    main_test = main_or_test(ctx)
    return _config()['emoji_ids'][main_test]

def get_afk():
    afk = open_file("misc", "afk", "json")
    return afk['users']

def get_server_name():
    return _config()['server_name']

def get_command_ignores():
    return _config()['command_ignores']

def get_channel_ids(ctx):
    main_test = main_or_test(ctx)
    return _config()['channel_ids'][main_test]

def get_role_ids(ctx):
    main_test = main_or_test(ctx)
    return _config()['role_ids'][main_test]

def get_owner_id():
    return _config()['owner_id']


def get_server_id(name: str):
    return _config()["server_ids"][name]

def get_channel_id(ctx, name: str):
    main_test = main_or_test(ctx)
    return get_channel_ids(ctx)[name]