import os
import json
import random
import inspect

filename = 'words.json'
basedir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
FILENAME = os.path.abspath(os.path.join(basedir, '..', 'static', filename))

def dump(outfile=FILENAME):
    from pattern.en import wordnet, conjugate, pluralize
    from pattern.en.wordlist import BASIC
    basic_words = lambda pos, fcn=(lambda x: x): [fcn(w) for w in BASIC if wordnet.synsets(w, pos=pos)]
    lkp = {'NOUNS': basic_words('NNS', pluralize), 'VERBS': basic_words('VB', lambda x: conjugate(x, 'part')), 'ADJS': basic_words('JJ')}
    json.dump(lkp, open(outfile, 'w'))

def load(infile=FILENAME):
    return json.load(open(infile))

def phrase(lkp):
    return '{0} the {1}'.format(random.choice(lkp['VERBS']), random.choice(lkp['NOUNS']))

if __name__ == '__main__':
    dump()
