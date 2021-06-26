import bpy
import bmesh

ob = bpy.context.object
assert ob is not None and ob.type == 'MESH', "active object invalid"

# ensure we got the latest assignments and weights
ob.update_from_editmode()
mesh = ob.data

bm = bmesh.from_edit_mesh(mesh)
active_vert_id = 0
for elem in reversed(bm.select_history):
    if isinstance(elem, bmesh.types.BMVert):
        active_vert_id = elem.index
        break

selected_verts = [v for v in mesh.vertices if v.select]
assert len(selected_verts) == 2, "select 2 verts"

# create vertex group lookup dictionary for names
vgroup_names = {vgroup.index: vgroup.name for vgroup in ob.vertex_groups}

# create dictionary of vertex group assignments per vertex
vgroups = {v.index: [(vgroup_names[g.group], g.weight) for g in v.groups if g.weight > 0] for v in selected_verts}

#remove any groups that appear in both lists
values = list(vgroups.values())

for i,pairs in enumerate(values):
    opposite_groups = [pair[0] for pair in values[1 - i]]
    if list(vgroups.keys())[i] == active_vert_id:
        print("Active vertex:")
    print([pair for pair in pairs if opposite_groups.count(pair[0]) == 0])
    print()