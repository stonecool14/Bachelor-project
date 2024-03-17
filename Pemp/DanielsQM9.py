import argparse
import os.path as osp
import time

import torch
import torch.nn.functional as F

from torch_geometric.datasets import TUDataset
from torch_geometric.loader import DataLoader
from torch_geometric.logging import init_wandb, log
from torch_geometric.nn import MLP, GINConv, global_add_pool
from torch_geometric.transforms import BaseTransform
from torch_geometric.data import Data, InMemoryDataset

dataset_name = 'QM9'

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default=dataset_name)
parser.add_argument('--batch_size', type=int, default=128)
parser.add_argument('--hidden_channels', type=int, default=32)
parser.add_argument('--num_layers', type=int, default=5)
parser.add_argument('--lr', type=float, default=0.01)
parser.add_argument('--epochs', type=int, default=100)
parser.add_argument('--wandb', action='store_true', help='Track experiment')
args = parser.parse_args()

if torch.cuda.is_available():
    device = torch.device('cuda')
elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
    # MPS is currently slower than CPU due to missing int64 min/max ops
    device = torch.device('cpu')
else:
    device = torch.device('cpu')

init_wandb(
    name=f'GIN-{args.dataset}',
    batch_size=args.batch_size,
    lr=args.lr,
    epochs=args.epochs,
    hidden_channels=args.hidden_channels,
    num_layers=args.num_layers,
    device=device,
)


path = osp.join(osp.dirname(osp.realpath(__file__)), 'Data', dataset_name)
dataset = TUDataset(path, name=args.dataset, use_edge_attr=True, use_node_attr=True).shuffle()




train_loader = DataLoader(dataset[:0.9], args.batch_size, shuffle=True)
test_loader = DataLoader(dataset[0.9:], args.batch_size)
print(dataset[0].y)
f = open("Data/QM9/QM9_graph_attributes.txt", "r")
nodeattr = f.read().split("\n")
k = open("FuckMeDanielGraph.txt", "w")
res = ""
for i in range(len(nodeattr)-1):
    temp = nodeattr[i].split(",")
    res += temp[0]+","+temp[1]+","+temp[4]+","+temp[7]+","+temp[11]+"\n"
k.write(res)
k.close()
f.close()
