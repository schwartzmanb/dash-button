# Dash Button 
### This is the source code for detecting and acting on presses from Amazon Dash Buttons

[![Build Status](https://travis-ci.org/schwartzmanb/dash-button.svg?branch=master)](https://travis-ci.org/schwartzmanb/dash-button)

## Installation

Clone this repository and install with pip:

```
pip3 install -e .
```

### Using this package

Run with:

```
python3 src/dashbutton/dashButton.py
```

Use the `-r` or `--read` flag followed by a filename to specify a csv file of button name + MAC pairs:

```
python3 src/dashbutton/dashButton.py -r path/to/file.csv
```

Use the `-l` or `--listen` flag with no other arguments to print all detected ARP packets to discern buttons:

```
python3 src/dashbutton/dashButton.py -l`
```

### Testing

Execute pytest in the package root:

```
pytest
```
