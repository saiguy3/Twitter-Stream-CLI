import click
import re
from stream_handler import setup_stream

def validate_words(ctx, param, value):
    try:
        if not bool(re.match('^[a-zA-Z0-9, ]+$', value)):
            raise(ValueError)

        words = value.split(',')
        words = list(map(str.strip, words))
        return words
    except ValueError:
        raise click.BadParameter('Words should be a comma separated list.')

@click.command()
@click.option('-v', '--verbose', is_flag=True,
    help='Print to standard out.')
@click.option('--output', default='tweets.txt', prompt='Output File',
    help='Output file to store tweets.')
@click.option('--words', prompt='Words to Follow', callback=validate_words,
    help='List the words to follow in a comma separated list.')
def main(verbose, output, words):
    stream = setup_stream(verbose, output)
    stream.filter(track=words, languages=['en'])

if __name__ == '__main__':
    click.echo('Use Ctrl+C to stop the stream.')
    main()
