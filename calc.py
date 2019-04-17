# Option 1: take command line args with `sys.argv[]` (same info as in config above)

import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("mps", help="Metrics per second", type=int)
parser.add_argument("nodes", help="Number of nodes", type=int)
parser.add_argument("rf", help="Replication factor", type=int)

args = parser.parse_args()

# mps = int(sys.argv[1])
# nodes = int(sys.argv[2])
# rf = int(sys.argv[3])

print(args.nodes)

def totalInternalWrites(mps,nodes,rf):
    print((args.mps * (rf / nodes)) + (mps * ((nodes - rf ) / nodes)))

totalInternalWrites(args.mps,args.nodes,args.rf)

# # Math

# # per node writes when first write hits    +    per node writes when first write misses (chance of miss is rf/nodes)

# mps * (1 / (nodes / rf)) + (mps * (nodes-rf/rf))

# 10-node rf2:
# 100 * (1 / (10/2)) + 100 * (8/2)
# 100 * (1/5) + 400
# 20 + 400 = 420

# 2-node rf2:
# 100 * 1 + 0 = 100





# # Option 2: take config file 'specs.ini' (in this directory) with node count, metrics per second, RF, and storage needs

# import configparser

# parser = configparser.ConfigParser()
# parser.read(open('params.ini'))

# print(parser.get('specs', 'rf'))
