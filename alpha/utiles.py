from .config.base_config import DEBUG


def get_used_config() -> str:
    current_config = (
        "alpha.config.local_config" if DEBUG else "alpha.config.production_config"
    )
    return current_config
