[![PyPI version](https://badge.fury.io/py/apikey.svg)](https://badge.fury.io/py/apikey)
[![apikey](https://snyk.io/advisor/python/apikey/badge.svg)](https://snyk.io/advisor/python/apikey)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/ulf1/apikey.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ulf1/apikey/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/ulf1/apikey.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/ulf1/apikey/context:python)
[![deepcode](https://www.deepcode.ai/api/gh/badge?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwbGF0Zm9ybTEiOiJnaCIsIm93bmVyMSI6InVsZjEiLCJyZXBvMSI6ImFwaWtleSIsImluY2x1ZGVMaW50IjpmYWxzZSwiYXV0aG9ySWQiOjI5NDUyLCJpYXQiOjE2MTk1MzQzNjR9.HYt6QGsqQrKe5syLQKLclXYjzTz5IXz5jteA1knvwy8)](https://www.deepcode.ai/app/gh/ulf1/apikey/_/dashboard?utm_content=gh%2Fulf1%2Fapikey)

# apikey

## Installation 
The `apikey` [git repo](http://github.com/ulf1/apikey) is available as [PyPi package](https://pypi.org/project/apikey)

```
pip install "apikey>=0.2.4"
pip install git+ssh://git@github.com/ulf1/apikey.git
```

## Usage
Store in default location `$HOME/.apikey-store` 

```python
import apikey

apikey.save("service1", "supersecret")
apikey.save("service2", "donttellanyone")
apikey.save("service3", "aboutthiskey")

key1 = apikey.load("service1")
key2 = apikey.load("service2")
key3 = apikey.load("service3")
```

Store in a specific file

```python
apikey.save("service42", "topsecretkey", filename="/srv/.secretkeys")
key = apikey.load("service42", filename="/srv/.secretkeys")
```


## Appendix

### Install a virtual environment

```sh
python3.6 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements-dev.txt
```


### Python commands

* Check syntax: `flake8 --ignore=F401 --exclude=$(grep -v '^#' .gitignore | xargs | sed -e 's/ /,/g')`
* Run Unit Tests: `pytest`

Publish

```sh
pandoc README.md --from markdown --to rst -s -o README.rst
python setup.py sdist 
twine upload -r pypi dist/*
```