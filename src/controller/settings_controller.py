import os
from configparser import ConfigParser
from shutil import copyfile

from ttkbootstrap.dialogs.dialogs import Messagebox


class SettingsController:
    @staticmethod
    def load_or_create_config_file(
        app_root_dir, required_config_file_version
    ) -> ConfigParser:
        """Loads and returns user settings. If the file
        APP_USER_DATA_DIR do not exist, creates the necessary directory
        structure and copies a template file with the default settings
        to the location.
        """
        settings = ConfigParser()

        app_usr_data_file_default = os.path.join(app_root_dir, "assets", "default.ini")

        usr_home_dir = os.path.expanduser("~")
        app_usr_data_dir = os.path.join(usr_home_dir, ".config", "time-journal")
        app_usr_data_file = os.path.join(app_usr_data_dir, "config")

        print(f"Loading config file at: {app_usr_data_file}")
        if not os.path.isfile(app_usr_data_file):
            print(f"Config file not found. Copying {app_usr_data_file_default}...")
            try:
                os.makedirs(app_usr_data_dir, exist_ok=True)
                copyfile(app_usr_data_file_default, app_usr_data_file)
            except PermissionError:
                print("PermissionError - Loading default ini file without copying.")
                app_usr_data_file = app_usr_data_file_default

        settings.read(app_usr_data_file)
        SettingsController.compare_config_file_versions(
            settings=settings,
            required_config_file_version=required_config_file_version,
            app_usr_data_file=app_usr_data_file,
            app_usr_data_file_default=app_usr_data_file_default,
        )
        return settings

    @staticmethod
    def compare_config_file_versions(
        settings,
        required_config_file_version,
        app_usr_data_file,
        app_usr_data_file_default,
    ):
        """Compares the config file version of the config file on the
        executing machine and the config file template

        Parameters
        ----------
        settings
            A config file dictionary, generated by configparser.read()
            method.
        """
        v_loaded = settings["DEFAULT"].getint("version")

        if v_loaded != required_config_file_version:
            # Backup the old config file
            backup = f"{app_usr_data_file}-{v_loaded}"
            copyfile(app_usr_data_file, backup)
            # Copy the new config file
            copyfile(app_usr_data_file_default, app_usr_data_file)
            # Notify the user
            play_sound = settings["notifications.sound"].getboolean("info_messages")
            Messagebox.show_info(
                message=(
                    "The user settings have been updated. To ensure a working program,"
                    " the new configuration file will be loaded. Your old"
                    f" configuration file has been backuped in {backup}"
                ),
                title="Config File Update",
                alert=play_sound,
            )
            settings.read(app_usr_data_file)
