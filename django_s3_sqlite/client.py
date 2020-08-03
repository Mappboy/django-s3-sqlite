import subprocess

from django.db.backends.base.client import BaseDatabaseClient


class DatabaseClient(BaseDatabaseClient):
    executable_name = "spatialite"

    def runshell(self):
        args = [self.executable_name, self.connection.settings_dict["NAME"]]

        subprocess.check_call(args)
