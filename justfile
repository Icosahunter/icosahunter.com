build:
    python3 build.py

publish:
    #!/usr/bin/env bash
    rm -rf /tmp/icosahunter
    mkdir /tmp/icosahunter
    mv -f dist /tmp/icosahunter
    git checkout website
    for f in `ls`
    do
        rm -rf $f
    done
    for f in `ls /tmp/icosahunter/dist`
    do
        mv /tmp/icosahunter/dist/$f .
    done
    git add --all
    git commit -m "Publish"
