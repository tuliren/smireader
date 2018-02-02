# Smireader

## About

Smireader can read SMS (text) backups generated by old Siemens phones and output the stored message text, time and date and phone number details.

Usually these files have `*.smi` (incoming) and `*.smo` (outgoing) extensions.

## Installation

Script has no external dependencies (besides python >= 3.5), so just copy the file somewhere and run it.

## Usage

```
usage: smireader.py [-h] [-d] [-m] [-n] [-t] [-v] file

Read data from Siemens SMI and SMO files.

positional arguments:
  file            File to read (*.smi and *.smo are supported)

optional arguments:
  -h, --help      show this help message and exit
  -d, --detailed  Show message with details. (alias for -mnt)
  -m, --message   Show message text.
  -n, --number    Show message sender/receiver number.
  -t, --time      Show message date and time.
  -v, --verbose   Increase verbosity.
```

### Library usage

*TODO* - see the source code for now, it should be easy enough to follow. ;)

## Status

This is still in early stage of development with couple hours spent so far and tested with limited number of files, so bugs are quite likely, however it can already quite reliably extract data from files I had access to. (these were generated by Siemens C55, other models might not be as well supported) Output from multipart messages contains extra characters, which should be hidden and only GSM7 encoded messages are supported - mostly due to the fact that I only have those files to test with. 


Any pull requests or sample files for testing will be very appreciated. 