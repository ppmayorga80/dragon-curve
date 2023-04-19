# dragon-curve

use a fractal code to generate my own version of dragon curve.
See the wikipedia reference: [Dragon Curve at Wikipedia](https://en.wikipedia.org/wiki/Dragon_curve) 

## Pre Installation

Be sure you have installed:

* Python 3 ```brew install python3```
* PkgConfig ```brew install pkg-config```

## Installation

* Create the environment ```python3 -m venv venv```
* Upgrade pip ```pip install --upgrade pip```
* Install packages ```pip install -r requirements.txt```

## Use

### Option 1: Run from virtual environment

* Activate environment ```source venv/bin/activate```
* Run ```python dragon.py --output dragon.svg```

### Option 2: Run from the system

Install step is performed just one time in order to install
the command into the system, then, you only need to run the script

* Install (1 time): ```python setup.py develop```
* Run: ```dragon --output dragon.svg```
