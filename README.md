# oncotreenx
light wrapper networkx wrapper around the oncotree data structure

## installing
The library can be installed using pip and the github package path.
```bash
pip install git+https://github.com/jim-bo/oncotreenx.git
```

## examples
```python
# import
import oncotreenx

# create graph.
g = oncotreenx.build_oncotree()

# get the ancestor.
p = get_basal(g, "CCHDM")

# make sure it is correct.
assert 'BONE' == p
```
