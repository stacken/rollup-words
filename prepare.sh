#! /bin/sh
set -ex
virtualenv --system-site-packages ve
. ve/bin/activate
#git clone git@github.com:amueller/word_cloud.git
#cd word_cloud
#pip install -r requirements.txt
pip install wordcloud
