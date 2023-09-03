from __future__ import absolute_import, division, print_function
__metaclass__ = type

# merges all dictionaries passed into it with dict.update(), later
# dictionaries taking precedence
def dict_merge(*args):
    merged = dict()
    for dictionary in args:
        merged.update(dictionary)

    return merged

class FilterModule(object):
    def filters(self):
        return {
            'dict_merge': dict_merge
        }
