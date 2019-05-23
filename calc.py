import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mps", help="Metrics per second", type=int)
parser.add_argument("nodes", help="Number of nodes", type=int)
parser.add_argument("rf", help="Replication factor", type=int)

args = parser.parse_args()

mps = args.mps
nodes = args.nodes
rf = args.rf
hitNumber = ((mps * (1 / (nodes/rf))) * rf)
missNumber = ((mps * ((nodes-rf)/nodes) * (rf+1)))
totalHits = ((mps * (1 / (nodes/rf))) * rf) + ((mps * ((nodes-rf)/nodes) * (rf+1)))
def totalInternalWrites(mps,nodes,rf):
    #print(((mps * rf) / (nodes/rf)) + ((mps * (rf+1)) / (((nodes-rf)/rf))))

    print(f"Total hits to nodes per second is:  {totalHits}")

    print(f"When metrics hit, they will write {hitNumber} times.")
    print(f"When metrics miss, they will write {missNumber} times.")
    #  print(mps * (1 / (nodes / rf)) + (mps * (nodes-rf)/rf))
if __name__ == "__main__":
    totalInternalWrites(mps,nodes,rf)
