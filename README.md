# Justice League


### Installation

```sh
pip install -r requirements.txt
```

### Start Application

```shell
python src/main.py
```

### Running Tests

First, you need to install the test runner (nosetests)

```shell
pip install -r requirements-dev.txt
```

To run all tests, use the test runner at the root of the project:
To run all the tests, you can use nosetests from the root of project

```shell
nosetests
```

Also, you can run only unit tests:

```shell
nosetests tests/unit
```

Or integration tests:

```shell
nosetests tests/integration --nologcapture
```

To measure test coverage, run the command bellow

```shell
nosetests --with-coverage --cover-package=src  --cover-inclusive --cover-html
```


#### Postman
[Collection](https://www.getpostman.com/collections/260d600d62527c96374e) <br/>
[Docs](https://documenter.getpostman.com/view/1939702/justice-league/RW1gEHAp#73460193-cb09-47a8-ad14-aa206ed3e30a)




