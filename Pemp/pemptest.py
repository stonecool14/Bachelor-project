from torch import nn as nn
from grovermain.grover.model.models import GROVEREmbedding
from grovermain.grover.util.parsing import parse_args
temp = parse_args()
print(temp.embedding_output_type)
test = GROVEREmbedding(parse_args())