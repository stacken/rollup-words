#! /bin/sh
set -ex
virtualenv --system-site-packages ve
. ve/bin/activate
pip install wordcloud numpy
# Or git clone git@github.com:amueller/word_cloud.git and follow the
# installation instructions there.
