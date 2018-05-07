# Justice League


### Installation

```sh
pip install -r requirements.txt
```

## Running Tests

First, you need to install the test runner (nosetests)

```shell
pip install -r requirements-dev.txt
```

To run all tests, use the test [runner](nosetests) at the root of the project:
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


#### Postman collection
[Postman link](https://www.getpostman.com/collections/260d600d62527c96374e)


