import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nodes", help="Number of nodes", type=int)
parser.add_argument("alloc", help="Allocated storage", type=int)
parser.add_argument("rf", help="Replication factor", type=int)

args = parser.parse_args()

nodes = args.nodes
alloc = args.alloc
rf = args.rf

provisioned_less = 2 * alloc
provisioned_more = alloc + 500

def calc_provisioned(nodes,alloc,rf):
    
    effective = (nodes * alloc) / rf
    
    if effective <= 500:
        print(f"Provisioned storage per node should be: {provisioned_less} GB")
    else:
        print(f"Provisioned storage per node should be: {provisioned_more} GB")
    print(f"Total effective storage is: {effective} GB")
    
if __name__ == "__main__":
    calc_provisioned(nodes,alloc,rf)



