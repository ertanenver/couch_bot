from environs import Env
from dataclasses import dataclass

@dataclass
class Bots:
    bot_token: str
    admin_id: int
    super_user_password: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path:str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.int("ADMIN_ID"),
            super_user_password=env.str("SUPER_USER_PASSWORD")

        )
    )

settings = get_settings('./input')