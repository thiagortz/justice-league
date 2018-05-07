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
[Postman link](https://www.getpostman.com/collections/f12769c5bfdd48dceb41)


### LICENSE

```
MIT License

Copyright (c) 2017 Stone Payments

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

