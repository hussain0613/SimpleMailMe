# SimpleMailMe

An easy and simple mailer API to integrate with web applications' contact us/me forms.
The endpoints are descriptions are given in the [endpoints.md](endpoints.md)


## Prerequisites
- python 3 installed

_Note:_ the project is developed and tested on Python3.11. \
This project was also tested on Python3.9 successfully.


## Installation

- clone the repository, `git clone ...`
- enter the project directory, `cd SimpleMailMe`
- clone the submodules, `git submodule update --init --recursive`

- create a virtual environment, `python -m venv venv`
- initialize the virtual environment, `source venv/bin/activate`
- install required packages, `python -m pip install -r requirements.txt`


## Configuration
- run `python generate_config.py` to generate the configuration file
- update the configuration file, `config.json`


## Run
- run `python main.py` to start the development server

