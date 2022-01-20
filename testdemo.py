import json

import requests

r = requests.get("http://admin:123456@101.200.243.163:9000/job/Prey9/40/allure/widgets/suites.json")
print(json.dumps(r.json(), indent=2, ensure_ascii=False))