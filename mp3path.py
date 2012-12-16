#!/usr/bin/python
import sys
import Sorter

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-s", "--source", action="store", type="str", dest="src", help="Source directory")
parser.add_option("-d", "--destination", action="store", type="str", dest="dest", help="Destination directory")
parser.add_option("-q", "--quiet", action="store_true", dest="quiet", default=False, help="Don't print status messages to stdout")
parser.add_option("-x", "--debug", action="store_true", dest="debug", default=False, help="Do a debug run (simulate without copying files)")

(options, args) = parser.parse_args()

if not options.src:
    parser.print_help()
    sys.exit()

if not options.dest:
    parser.print_help()
    sys.exit()

#Sorter.sort(options.src, options.dest, options.debug)

