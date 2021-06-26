import bpy

ob = bpy.context.object
assert ob is not None and ob.type == 'MESH', "active object invalid"

# ensure we got the latest assignments and weights
ob.update_from_editmode()
mesh = ob.data

selected_verts = [v for v in mesh.vertices if v.select]

# create vertex group lookup dictionary for names
vgroup_names = {vgroup.index: vgroup.name for vgroup in ob.vertex_groups}

# create dictionary of vertex group assignments per vertex where 
vgroups = {v.index: [(vgroup_names[g.group], g.weight) for g in v.groups if g.weight > 0] for v in selected_verts}

print(vgroups)