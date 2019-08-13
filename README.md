# Twitter Stream CLI
This is CLI for the Twitter Streams Filter API.

## Set-Up
1. Create a Twitter Developer account and set a `.env` file with the following four variables:
    * CONSUMER_KEY
    * CONSUMER_SECRET_KEY
    * ACCESS_TOKEN
    * ACCESS_TOKEN_SECRET
2. Run `python3 -m venv ./venv` to create a virtual environment
3. Run `pip install -r requirements.txt` to install the necessary dependencies

## Usage
`python3 stream.py [OPTIONS]`

Options:
* `-v`, `--verbose`: Print to standard out.
* `--output file_name`: Output file to store tweets. [Default: tweets.txt]
* `--words TEXT`: List the words to follow in a comma separated list.
* `--help`: Show help message and exit.
