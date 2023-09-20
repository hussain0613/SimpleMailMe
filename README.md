# SimpleMailMe

A simple mailer to integrate with web application.

## Endpoints

### [POST] /send/
#### Request
**Parameters:** 
- `ignore_headers` (optional): boolean, default `false`
    if `true`, ignore the headers in the request body

**Body:**
```
{
    "name": str,
    "email": str,
    "subject": str,
    "message": str
}*
```
Content-Type: `application/json`
_Note_: Body may contain additional fields

#### Response
**204 No Content**



## Installation

- clone the repository, `git clone ...`
- change directory, `cd SimpleMailMe`
- create a virtual environment, `python -m venv venv`
- initialize the virtual environment, `source venv/bin/activate`
- install required packages, `python -m pip install -r requirements.txt`

- clone the submodules, `git submodule update --init --recursive`


## Configuration
- run `python generate_config.py` to generate the configuration file
- update the configuration file, `config.json`

## Run
- run `python main.py` to start the development server

