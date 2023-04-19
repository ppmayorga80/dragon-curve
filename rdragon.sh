#!/bin/bash
N=10
D=1200
LW=1.00
INKSCAPE=/Applications/Inkscape.app/Contents/MacOS/inkscape
seq 0 1 $N | xargs -I % sh -c "python rdragon_curve.py -n % --line-width=${LW} --output=/Users/pedro/Downloads/dragon%.svg"
seq 0 1 $N | xargs -I % sh -c "${INKSCAPE} /Users/pedro/Downloads/dragon%.svg --export-pdf=/Users/pedro/Downloads/dragon%.pdf"
seq 0 1 $N | xargs -I % sh -c "convert -density ${D}x${D} /Users/pedro/Downloads/dragon%.svg /Users/pedro/Downloads/dragon%.png"
seq 0 1 $N | xargs -I % sh -c 'rm /Users/pedro/Downloads/dragon%.svg'
