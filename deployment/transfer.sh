#!/bin/bash

echo "Starting sync"
rsync -avz --progress --exclude-from 'exclude-list.txt' ../ dev:/home/sid/
echo "Done!"
