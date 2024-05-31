import json
import os
import shutil
import subprocess
from typing import List, Tuple

x = open("meta-data.json", "w")

projects: List[Tuple[str, int]] = [
    ("cakephp--cakephp", 33),
    ("briannesbitt--Carbon", 11),
    ("composer--composer", 18),
    ("doctrine--dbal", 9),
    ("w7corp--easywechat", 9),
    ("laravel--framework", 94),
    ("googleapis--google-api-php-client", 3),
    ("spatie--laravel-permission", 6),
    ("magento--magento2", 23),
    ("Seldaek--monolog", 7),
    ("doctrine--orm", 15),
    ("PHP-CS-Fixer--PHP-CS-Fixer", 82),
    ("nikic--PHP-Parser", 3),
    ("PHPOffice--PhpSpreadsheet", 12),
    ("symfony--symfony", 188)
]


result = []
id = 0
for name, bug_count in projects:
    os.makedirs(name, exist_ok=True)
    for bug in range(1, bug_count):
        os.makedirs(os.path.join(name, f"{name}-{bug}"),exist_ok=True)
        for script in ["build_subject","config_subject","setup_subject","test_subject"]:
            shutil.copy(script,os.path.join(name, f"{name}-{bug}",script))
        id += 1
        '''
        proc = subprocess.Popen(
            ["python3 main.py -p {} -b {} -t info -v buggy".format(name, bug)],
            stdout=subprocess.PIPE,
            shell=True,
        )
        (out, err) = proc.communicate()
        data = out.decode("utf-8")
        lines = data.split("\n")
        '''
        result.append(
            {
                "id": id,
                "subject": name,
                "bug_id": f"{name}-{bug}",
                "test_timeout": 5,
                "language": "js",
                "build_script": "build_subject",
                "config_script": "config_subject",
                "clean_script": "clean_subject",
                "test_script": "test_subject",
                "passing_test_identifiers": [],
                "count_pos": 0,
                "failing_test_identifiers": [],
                "count_neg": 0,
                "line_numbers": [],
                "dependencies": [],
            }
        )
        # input()

x.write(json.dumps(result, indent=4))
x.close()
