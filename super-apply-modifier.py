import bpy

original = bpy.context.object
# create duplicate
bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'})

source = bpy.context.object
source_keys = source.data.shape_keys.key_blocks
pinned = source.show_only_shape_key
keyed_meshes = []


source.show_only_shape_key = True

for name, block in source_keys.items():
    if name == source_keys.items()[0][0]:
        continue
    bpy.context.object.active_shape_key_index = 1
#    magic
    depth = bpy.context.evaluated_depsgraph_get()
    eobj = source.evaluated_get(depth)
    mesh = bpy.data.meshes.new_from_object(eobj)
    new_object = bpy.data.objects.new(name, mesh)
    new_object.data = mesh
    bpy.context.collection.objects.link(new_object)
    
#   Select object and remove shape key    
    new_object.select_set(True)
    bpy.ops.object.shape_key_remove()
    
# remove basis shape key, done last to keep original basis
bpy.ops.object.shape_key_remove()

for m in source.modifiers:
    if (m.type == 'SUBSURF') or (m.type == ('MIRROR')):
        bpy.ops.object.modifier_apply(modifier=m.name) 

bpy.ops.object.join_shapes()

source.select_set(False)

bpy.ops.object.delete(use_global=False)

original.select_set(True)
source.select_set(True)

bpy.ops.object.make_links_data(type='OBDATA')
original.select_set(False)
bpy.ops.object.delete(use_global=False)

for m in original.modifiers:
    if (m.type == 'SUBSURF') or (m.type == ('MIRROR')):
        original.modifiers.remove(m)
