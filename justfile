build:
    python3 build.py

publish: build
    #!/usr/bin/env bash
    rm -rf /tmp/icosahunter
    mkdir /tmp/icosahunter
    mv -f dist /tmp/icosahunter
    git checkout website
    for f in `ls`
    do
        rm -rf $f
    done
    for f in `ls /tmp/icosahunter/`
    do
        mv /tmp/icosahunter/$f .
    done
