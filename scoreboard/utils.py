import os

# Env
def get_env_var(env_var_name, default_value):
    env_var_value = os.getenv(env_var_name)
    return env_var_value if env_var_value is not None else default_value