## How to launch

Execute `docker compose up -d` and that's all, after that service can be accessed on http://localhost:8080

## run siege:
run --rm -t --network="siege_test_default" -v /Path/to/project/siege_test/urls:/etc/urls yokogawa/siege -d1 -t5M -c25 -i -f /etc/urls/urls.txt
