# Blogger

[![Build Status](https://travis-ci.org/ozcanyarimdunya/blogger.svg?branch=master)](https://travis-ci.org/ozcanyarimdunya/blogger)
[![Coverage Status](https://coveralls.io/repos/github/ozcanyarimdunya/blogger/badge.svg?branch=master)](https://coveralls.io/github/ozcanyarimdunya/blogger?branch=master)

A blog application with django


## Installation

1. Clone the repository.
   ```
   $ git clone https://github.com/ozcanyarimdunya/blogger.git
   $ cd blogger/
   ```

2. Install the virtualenv package, create new virtual environment and activate it.
   ```
   $ pip install virtualenv
   $ virtualenv venv
   $ source venv/bin/activate
   ```

3. Install all dependencies and start application on [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
   ```
   $ make
   ```

## Running in docker

1. Make sure you have installed **docker** and **docker-compose**.
   ```
   make docd
   ```
