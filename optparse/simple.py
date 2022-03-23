from optparse import OptionParser


# python3 ./simple.py -h
# python3 ./simple.py a b -f <file> -q

usage = "usage: %prog [options] arg1 arg2"



parser = OptionParser(usage=usage)

parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE", type=str)

parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")


(options, args) = parser.parse_args()

print(options, args)
print(options.filename)

if len(args):
    print(args[0])
