import bpy

# Get reference
C = bpy.context
D = bpy.data
S = D.scenes["Scene"]
nodetree = bpy.context.scene.node_tree

nodeRL = S.node_tree.nodes["Render Layers"] # This is "Render Layer"
nodeHub = S.node_tree.nodes["Hub"] # This is "Hub"
nodeR4 = S.node_tree.nodes["R4_pointiness"]# This is "Pointiness"

# Select render Engine
C.scene.render.engine = "CYCLES"

# Apply material to selected objects
material = bpy.data.materials["r4_pointiness"]
selected_object = C.selected_objects[0]
selected_object.material_slots[0].material = material

# Remove links in compositor
def remove_link(socket_out, socket_in):
    for link in socket_out.links:
        if link.to_socket == socket_in:
            nodetree.links.remove(link)

remove_link(nodeHub.outputs[4], nodeR4.inputs[0])
remove_link(nodeHub.outputs[4], nodeR4.inputs[1])
remove_link(nodeHub.outputs[4], nodeR4.inputs[2])

# 100% #################################################
## Delete DECIMATE modifyer on selected object
bpy.ops.object.modifier_remove(modifier="Decimate")

## Create link
nodetree.links.new(nodeRL.outputs[0], nodeHub.inputs[7])
nodetree.links.new(nodeHub.outputs[4], nodeR4.inputs[0])
