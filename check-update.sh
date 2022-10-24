#!/bin/sh
# Deal with version scheme change -- sadly 2015-30-11 > 3.3.2, but that's
# not how the versioning goes here...
git ls-remote --tags https://github.com/Wargus/stratagus 2>/dev/null|awk '{ print $2; }' |grep 'refs/tags/v' |sed -e 's,refs/tags/,,;s,_,.,g;s,^v,,' |sort -V |tail -n1
