## Bento Playwright

### Requirements:

1. Python 3.7.0 or higher.
   1. To handle different versions of python it is recommended to use a python version management like: [pyenv](https://github.com/pyenv/pyenv)
   2. Install a specific python version `pyenv install 3.7.0`
2. Python virtual environment.
   1. If you have already installed [pyenv](https://github.com/pyenv/pyenv), you need an extra package called [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
   2. Once installed [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) and installed a python version (3.7.0 or higher) you can create a virtual environment using the next command: `pyenv virtualenv 3.7.0 <virtual-env-name>`
   3. Activate virtualenv `pyenv activate <virtual-env-name>`

### Installation

With your virtual environment activated you can run the following command:

```bash
pip install -r requirements.txt
```

### Usage

To run the tests you have created just execute the following command:

```bash
pytest
```

You can see more useful commands in this [link](https://playwright.dev/python/docs/test-runners)