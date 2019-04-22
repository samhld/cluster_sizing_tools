# Option 1: take command line args with `sys.argv[]` (same info as in config above)

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mps", help="Metrics per second", type=int)
parser.add_argument("nodes", help="Number of nodes", type=int)
parser.add_argument("rf", help="Replication factor", type=int)

args = parser.parse_args()

mps = args.mps
nodes = args.nodes
rf = args.rf

def totalInternalWrites(mps,nodes,rf):
    print(mps * (1 / (nodes / rf)) + (mps * (nodes-rf)/rf))

if __name__ == "__main__":
    totalInternalWrites(mps,nodes,rf)
