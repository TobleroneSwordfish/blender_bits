# Useful Blender node groups, utilities and scripts
## starfield
Just a coloured random starfield shader
![starfield](./readme_files/starfield.png)
## spiral
A customizable spiral generator node group

![spiral node group](./readme_files/spiral_node_group.png)

The ```Spin``` value can be animated to make the spiral spin.

![spiral screenshot](./readme_files/spiral.png)

## eyelids
A first person eyelids closing effect compositor node group, has a single value that can be animated representing how open or closed the eyelids are.
<!-- I stg why am I even using markdown if I have to write html every other line to get it to work -->
![eyelids demo](./readme_files/eyelids.png)

<!-- <video width="320" height="240" controls>
    <source src="readme_files/eyelids.mp4" type="video/mp4">
    <source src="readme_files/eyelids.webm" type="video/webm">
</video> -->

With a blur effect applied (see blender file)

## get_vertex_groups.py

Simple script to get the vertex groups selected vertices belong to along with the weights of each vertex in group.
This is needed because apparently there is no way to do this in the blender UI.
The output is written to the system console ("Window -> Toggle system console" to enable) in the following format:
```
{<vertex id>: [('<node group name>', <weight of vertex in node group>), ...]}
```
Example output with some wonderfully named node groups:

![script output](readme_files/script_output1.png)

## xor_vertex_groups

Slightly more complex script to compare vertex groups of two different vertices. The script outputs a list of all vertex groups for each node that are unique to it, along with weights for each group.

![script output](readme_files/script_output2.png)