#!/usr/bin/env python

import os


def get_secrets(env_var_list):
    """ get os environmental variable secret1 """
    secrets = dict()

    for env_var in env_var_list:
        secrets[env_var] = os.getenv(env_var)

    return secrets


if __name__ == "__main__":
    env_vars = ["secret1", "some_other_secret", "secret2", "secret3"]
    result = get_secrets(env_vars)
    print(result)
