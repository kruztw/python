from optparse import *


parser = OptionParser(usage="%prog [-g] [-d] [-d]", version="%prog 1.0")


group1 = OptionGroup(parser, "Options 1", "This is Options 1")
group1.add_option("-g", action="store_true", help="Group option.")
parser.add_option_group(group1)

group2 = OptionGroup(parser, "Options 2")
group2.add_option("-d", "--debug", action="store_true", help="Print debug information")
group2.add_option("-e", action="store_true", help="Print every action done")
parser.add_option_group(group2)


(options, args) = parser.parse_args()

print(options, args)
