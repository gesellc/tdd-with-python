# Test-Driven Development with Python

In this repository I will work through Harry J.W. Percival's book "Test-Driven Development with Python".

Go and visit the book's home planet: http://www.obeythetestinggoat.com/

## Check Status

[![Build Status](https://travis-ci.org/gesellc/tdd-with-python.svg?branch=master)](https://travis-ci.org/gesellc/tdd-with-python) [![Coverage Status](https://coveralls.io/repos/github/gesellc/tdd-with-python/badge.svg?branch=master)](https://coveralls.io/github/gesellc/tdd-with-python?branch=master) [![Code Health](https://landscape.io/github/gesellc/tdd-with-python/master/landscape.svg?style=flat)](https://landscape.io/github/gesellc/tdd-with-python/master)


## Play with the app locally

* Check prerequisites (you might only need Django for now)

  http://www.obeythetestinggoat.com/book/pre-requisite-installations.html#_required_software_installations

* Start Server

        python3 manage.py runserver

* Point your favourite browser to home

  http://127.0.0.1:8000/

## Run Tests

* Run the functional tests

        python3 manage.py test functional_tests

* Run the unit tests

        python3 manage.py test lists
