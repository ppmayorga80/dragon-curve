#!/bin/bash
N=10
D=1200
LW=1.00
INKSCAPE=/Applications/Inkscape.app/Contents/MacOS/inkscape
seq 0 1 $N | xargs -I % sh -c "python dragon.py --rounded --gradient -n % --line-width=${LW} --output=$HOME/Downloads/dragon%.svg"
seq 0 1 $N | xargs -I % sh -c "${INKSCAPE} /Users/pedro/Downloads/dragon%.svg --export-pdf=$HOME/Downloads/dragon%.pdf"
seq 0 1 $N | xargs -I % sh -c "convert -density ${D}x${D} /Users/pedro/Downloads/dragon%.svg $HOME/Downloads/dragon%.png"
seq 0 1 $N | xargs -I % sh -c "rm $HOME/Downloads/dragon%.svg"

