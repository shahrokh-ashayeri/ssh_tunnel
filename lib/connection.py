import os
import subprocess
import codecs


class Connection:

    def __init__(self) -> None:
        pass

    def is_alive(self):
        proc = subprocess.Popen(
            ["nc -z localhost 8080 || echo 'No tunnel open'"],
            stdout=subprocess.PIPE,
            shell=True,
        )
        (out, err) = proc.communicate()

        if err:
            raise Exception("An error occured in SSH Connection")

        return codecs.decode(out, "unicode_escape")

    def close(self):
        pass
