from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    MIN_AVAILABLE_ENERGY: int = 100
    SLEEP_BY_MIN_ENERGY: list[int] = [1800, 2400]

    AUTO_UPGRADE: bool = True
    MAX_LEVEL: int = 20
    MAX_PRICE: int = 50000000

    BALANCE_TO_SAVE: int = 1000000
    UPGRADES_COUNT: int = 10

    MAX_COMBO_PRICE: int = 10000000

    APPLY_DAILY_ENERGY: bool = True
    APPLY_DAILY_TURBO: bool = True

    USE_TAPS: bool = True
    RANDOM_TAPS_COUNT: list[int] = [10, 50]
    SLEEP_BETWEEN_TAP: list[int] = [10, 25]

    USE_RANDOM_DELAY_IN_RUN: bool = False
    RANDOM_DELAY_IN_RUN: list[int] = [0, 15]

    USE_RANDOM_USERAGENT: bool = False


settings = Settings()
