from os import listdir
from datetime import datetime
import re

file_regex = '.* - Challenge - (.*) Stats.csv'
score_pattern = 'Score:,(.+)'


def file_time(f):
    m = re.match(file_regex, f)
    return datetime.strptime(m[1], '%Y.%m.%d-%H.%M.%S')


def read_score(path):
    with(open(path)) as f:
        s = ''.join(f.readlines())
        m = re.search(score_pattern, s)
        score = float(m[1])
        return "{:.2f}".format(score)


kovaak_dir = "/mnt/c/Program Files (x86)/Steam/steamapps/common/FPSAimTrainer/FPSAimTrainer/stats/"


def process(scenario, last_n):

    all_files = listdir(kovaak_dir)

    files = [x for x in all_files if x.startswith(scenario)]
    sorted_files = sorted(files, key=file_time)
    new_files = sorted_files[-5:]
    for f in new_files:
        print(datetime.strftime(file_time(f), '%m/%d %H:%M'))
    scores = [read_score(kovaak_dir + path) for path in new_files]
    print(",".join(scores))


process('Ascended Tracking v3', 5)
process('Ascended Tracking 90 Small', 5)
