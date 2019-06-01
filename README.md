## Project description

Amount of records during test: ~100000

Endpoints:

- `/` - index form and list (only ten items)
- `/deposit POST` - insert single record
- `/stats` - displays the result of a query with group by numeric index field  

## How to launch

Execute `docker compose up -d` and that's all, after that service can be accessed on http://localhost:8080

## Run siege:
```
run --rm -t --network="siege_test_default" -v /Path/to/project/siege_test/urls:/etc/urls yokogawa/siege -d1 -t1M -c25 -i -f /etc/urls/urls.txt
```

Urls for test:

```
http://app
http://app/stats
http://app/deposit POST name=test&type=Cat&weight=10&age=5
http://app/deposit POST name=test&type=Mouse&weight=2&age=2
http://app/deposit POST name=test&type=Dog&weight=10&age=5
http://app/deposit POST name=test&type=Turtle&weight=10&age=5
```

## Results

![Siege test](https://github.com/dariakharlan/siege_test/blob/master/report/chart_100k.png)
