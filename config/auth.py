import os
import stat
import getpass
import ConfigParser

config_folder = os.path.expanduser(os.path.join('~', '.hsrtools'))
config_file = os.path.join(config_folder, 'config')
config = ConfigParser.ConfigParser()


def _parse_config():
    """Parse config file and return stored username/password."""

    # Create folder if necessary
    if not os.path.isdir(config_folder):
        os.mkdir(config_folder)

    # Read config, write default config file if it doesn't exist yet.
    if not len(config.read(config_file)):
        print 'Could not find configuration file. Creating %s.' % config_file

        # Login data
        username = raw_input('\nHSR Username: ').strip()
        print 'Enter your password, in case you want to store it in the ' \
              'config file. Otherwise you will be asked for it each time.\n' \
              'Warning: Password will be saved in plaintext.'
        password = getpass.getpass('HSR Password (ENTER to skip): ').strip()

        # Write config
        config.add_section('auth')
        config.set('auth', 'username', username)
        config.set('auth', 'password', password)
        config.write(open(config_file, 'w'))
        os.chmod(config_file, stat.S_IREAD | stat.S_IWRITE)

        print 'Initial configuration is finished. you may edit your ' + \
              'configuration file at %s.\n' % config_file
    else:
        try:
            config.add_section('auth')
        except ConfigParser.DuplicateSectionError:
            pass
        
        # Get user data
        username = config.get('auth', 'username')
        password = config.get('auth', 'password')

    return username, password


def userinfo():
    """Try to get auth info from config file. Prompt for password if it wasn't
    stored in the config file."""

    # Try to get user info from config
    username, password = _parse_config()

    # If passwort hasn't been stored, prompt for it
    if not password:
        password = getpass.getpass('HSR Password: ').strip()

    # Return info
    return username, password
