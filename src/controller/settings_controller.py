import os
import configparser
from shutil import copyfile
from ttkbootstrap.dialogs.dialogs import Messagebox
# Custom libraries
from config.definitions import APP_USER_DATA_FILE, CONFIG_FILE_VERSION, APP_DEFAULT_USER_DATA_FILE


class SettingsController:
    @staticmethod
    def load_or_create_config_file():
        """Loads and returns user settings. If the file
        APP_USER_DATA_DIR do not exist, creates the necessary directory
        structure and copies a template file with the default settings
        to the location.
        """
        settings = configparser.ConfigParser()

        print(f'Loading config file at: {APP_USER_DATA_FILE}')
        if not os.path.isfile(APP_USER_DATA_FILE):
            os.makedirs(APP_USER_DATA_FILE)
            print(f'Config file not found. Copying {APP_DEFAULT_USER_DATA_FILE}...')
            copyfile(APP_DEFAULT_USER_DATA_FILE, APP_USER_DATA_FILE)

        settings.read(APP_USER_DATA_FILE)
        SettingsController.compare_config_file_versions(settings)
        return settings
    
    @staticmethod
    def compare_config_file_versions(settings):
        """Compares the config file version of the config file on the
        executing machine and the config file template

        Parameters
        ----------
        settings
            A config file dictionary, generated by configparser.read()
            method.
        """
        v_curr = settings['DEFAULT'].getint('version')
        v_new = CONFIG_FILE_VERSION

        if v_curr != v_new:
            # Backup the old config file
            backup = f'{APP_USER_DATA_FILE}-{v_curr}'
            copyfile(APP_USER_DATA_FILE, backup)
            # Copy the new config file
            copyfile(APP_DEFAULT_USER_DATA_FILE, APP_USER_DATA_FILE)
            # Notify the user
            play_sound = settings['notifications.sound'].getboolean('info_messages')
            Messagebox.show_info(
                message=f'The user settings have been updated. To ensure a working program, the new configuration file will be loaded. Your old configuration file has been backuped in {backup}',
                title='Config File Update',
                alert=play_sound
            )
            settings.read(APP_USER_DATA_FILE)