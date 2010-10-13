#!/bin/bash

# runs MyBot against sample bot
# pass bot name and map # as a parameter, for instance bot.sh BullyBot 1

java -jar tools/PlayGame.jar maps/map$1.txt 1000 200 bot_$1.log "java -jar example_bots/$2.jar" "python MyBot.py --log MyBot.log" | python visualizer/visualize_localy.py
