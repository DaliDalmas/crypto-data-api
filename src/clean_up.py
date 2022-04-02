import sys
import json
my_settings = open('my_settings.json')
settings = json.load(my_settings)
sys.path.append(settings["BASE_PATH"])

import os
class CleanUp:
    def __init__(self, path:str) -> None:
        self.path:str = path

    def run(self):
        os.remove(self.path)

if __name__=='__main__':
    clean = CleanUp(
        path=settings['BINARY_SERVER_DATA_PATH']
    )
    clean.run()

    clean = CleanUp(
        path=settings['CSV_SERVER_DATA_PATH']
    )
    clean.run()