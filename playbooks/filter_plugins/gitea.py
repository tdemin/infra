from __future__ import absolute_import, division, print_function
__metaclass__ = type

ENV_PREFIX = "GITEA__"

# transforms dictionary featuring Gitea config sections as keys and K/V
# vars in those sections as subdicts to dictionary of Gitea-supported
# environment variables, see [1]
#
# [1]: https://docs.gitea.com/installation/install-with-docker (see
#     "Managing Deployments With Environment Variables)
def dict_to_env(dictionary):
    result = {}
    for section, values in dictionary.items():
        for key, value in values.items():
            env_var = f"{ENV_PREFIX}{section}__{key}"
            result[env_var] = value

    return result

class FilterModule(object):
    def filters(self):
        return {
            'gitea_dict_to_env_dict': dict_to_env
        }
