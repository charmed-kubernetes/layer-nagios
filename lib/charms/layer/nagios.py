import os
import stat

NAGIOS_PLUGINS_DIR = '/usr/lib/nagios/plugins'


def install_nagios_plugin(source_path, plugin_name, data=None):
    """ Install a nagios plugin.

    Args:
        source_path: Source file path to install
        plugin_name: Name of the plugin in nagios

    Returns: Full path to installed plugin
    """
    if data is None:
        with open(source_path, "r") as f:
            data = f.read()
    dest_path = os.path.join(NAGIOS_PLUGINS_DIR, plugin_name)
    if os.path.exists(dest_path):
        # we could complain here, test the files are the same contents, or
        # just bail. Idempotency is a big deal in Juju, so I'd like to be
        # ok with being called with the same file multiple times, but we
        # certainly want to catch the case where multiple layers are using
        # the same filename for their nagios checks.
        with open(dest_path, "r") as f:
            dest = f.read()
        if dest == data:
            # same file
            return dest_path
        # else:
            # different file contents!
            # maybe someone changed options or something...

    with open(dest_path, "w") as f:
        f.write(data)

    os.chmod(dest_path, stat.S_IRWXU | stat.S_IRGRP |
             stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
    return dest_path


def remove_nagios_plugin(plugin_name):
    """ Remove a nagios plugin.

    Args:
        plugin_name: Plugin name that was passed to install_plugin

    Returns: None
    """
    dest_path = os.path.join(NAGIOS_PLUGINS_DIR, plugin_name)
    if os.path.exists(dest_path):
        os.remove(dest_path)
