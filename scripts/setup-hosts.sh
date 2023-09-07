#!/usr/bin/sh

# Adds flask.test to hosts file

if [ "$(uname)" = "Darwin" ]; then
    echo "Setting hosts file for Mac"
    echo "127.0.0.1 flask.test" >> /private/etc/hosts
elif [ "$(uname -s | cut -c1-5)" = "Linux" ]; then
    echo "Setting hosts file for Linux"
    echo "127.0.0.1 flask.test" >> /etc/hosts
fi
