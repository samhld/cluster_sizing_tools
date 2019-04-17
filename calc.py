# Option 1: take command line args with `sys.argv[]` (same info as in config above)

import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("mps", help="Metrics per second", type=int)
parser.add_argument("nodes", help="Number of nodes", type=int)
parser.add_argument("rf", help="Replication factor", type=int)

args = parser.parse_args()

mps = args.mps
nodes = args.nodes
rf = args.rf

def totalInternalWrites(mps,nodes,rf):
    print(mps * (1 / (nodes / rf)) + (mps * (nodes-rf/rf)))

totalInternalWrites(mps,nodes,rf)

# # Math
print(1/(nodes/rf))
print(0/2)
# # per node writes when first write hits    +    per node writes when first write misses (chance of miss is rf/nodes)

# mps * (1 / (nodes / rf)) + (mps * (nodes-rf/rf))

# 10-node rf2:
# 100 * (1 / (10/2)) + 100 * (8/2)
# 100 * (1/5) + 400
# 20 + 400 = 420

# 2-node rf2:
# 100 * 1 + 0 = 100
