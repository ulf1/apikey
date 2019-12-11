<!-- [![Build Status](https://travis-ci.org/ulf1/apikey.svg?branch=master)](https://travis-ci.org/ulf1/apikey)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ulf1/apikey/master?urlpath=lab) -->

# apikey

## Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [Commands](#commands)
* [Support](#support)
* [Contributing](#contributing)


## Installation
The `apikey` [git repo](http://github.com/ulf1/apikey) is a private package

```
pip install git+ssh://git@github.com/ulf1/apikey.git
```

## Usage
Store in default location `$HOME/.apikey-store` 

```
from apikey import save_apikey, read_apikey

save_apikey("service1", "supersecret")
save_apikey("service2", "donttellanyone")
save_apikey("service3", "aboutthiskey")

key1 = read_apikey("service1")
key2 = read_apikey("service2")
key3 = read_apikey("service3")
```

Store in a specific file

```
save_apikey("service42", "topsecretkey", filename="/srv/.secretkeys")
key = read_apikey("service42", filename="/srv/.secretkeys")
```



## Commands
* Check syntax: `flake8 --ignore=F401`
* Run Unit Tests: `pytest`
* Remove `.pyc` files: `find . -type f -name "*.pyc" | xargs rm`
* Remove `__pycache__` folders: `find . -type d -name "__pycache__" | xargs rm -rf`


## Support
Please [open an issue](https://github.com/ulf1/apikey/issues/new) for support.


## Contributing
Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/ulf1/apikey/compare/).
