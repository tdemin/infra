from __future__ import absolute_import, division, print_function
__metaclass__ = type

from os.path import join as pathjoin

# treats arg as module arg for ansible.builtin.copy; concatenates `dest`
# and `config_path` if `config_path` isn't already in there, then
# appends owner/mode/group standard to all known distributions shipping
# systemd-networkd if unset in arg
def networkd_populate_fprops(arg, config_path):
    dest = arg.get('dest')
    new_dest = dest if config_path in dest \
        else pathjoin(config_path, dest)
    return {
        'dest': new_dest,
        'content': arg.get('content', ''),
        'mode': arg.get('mode', '0644'),
        'owner': arg.get('owner', 'root'),
        'group': arg.get('group', 'root')
    }

class FilterModule(object):
    def filters(self):
        return {
            'networkd_populate_file_properties': networkd_populate_fprops
        }
