import bpy


print("[PETRA] Setup: Initial")

C = bpy.context
D = bpy.data

#####################
# RENDER PROPERTIES #
#####################

## Render transparent background
C.scene.render.film_transparent = True

#####################
# CREATE COLLECTION #
#####################

Asset_collection = D.collections.new("PETRA")
C.scene.collection.children.link(Asset_collection)

C.view_layer.active_layer_collection = C.view_layer.layer_collection.children["PETRA"]

###############
# FRAMING BOX #
###############

## Create a Cube
bpy.ops.mesh.primitive_cube_add(
    enter_editmode=False, align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
)
so = C.selected_objects[0]
so.name = "Framing Box"

## Skin modifyer
bpy.ops.object.modifier_add(type="SKIN")

## Skin resize
bpy.ops.object.editmode_toggle()
bpy.ops.transform.skin_resize(value=(0.1, 0.1, 0.1))
bpy.ops.object.editmode_toggle()

## Apply modifyer
bpy.ops.object.modifier_apply(modifier="Skin", report=True)

## Scale the box
C.object.scale = 0.487805, 0.487805, 0.487805
bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

####################
# Reference Sphere #
####################

bpy.ops.mesh.primitive_ico_sphere_add(
    radius=0.05, location=(0.4, 0.4, 0.4), scale=(1, 1, 1)
)
so = C.selected_objects[0]
so.name = "Reference Sphere"

bpy.ops.object.modifier_add(type="SUBSURF")
C.object.modifiers["Subdivision"].levels = 2
bpy.ops.object.shade_smooth()
bpy.ops.object.modifier_apply(modifier="Subdivision", report=True)

###########
# Cameras #
###########

## Cam-01
bpy.ops.object.camera_add(location=(0, -0.5, 0), rotation=(1.5708, 0, 0))
so = C.selected_objects[0]
so.name = "Cam-01"

## Cam-02
bpy.ops.object.camera_add(location=(0.5, 0, 0), rotation=(1.5708, 0.00, 1.5708))
so = C.selected_objects[0]
so.name = "Cam-02"
C.object.hide_set(True)

## Cam-03
bpy.ops.object.camera_add(location=(0, 0.5, 0), rotation=(1.5708, 0.00, 3.14159))
so = C.selected_objects[0]
so.name = "Cam-03"
C.object.hide_set(True)

## Cam-04
bpy.ops.object.camera_add(location=(-0.5, 0, 0), rotation=(1.5708, 0, -1.5708))
so = C.selected_objects[0]
so.name = "Cam-04"
C.object.hide_set(True)

## Cam-05
bpy.ops.object.camera_add(location=(0, 0, 0.5), rotation=(0, 0, 0))
so = C.selected_objects[0]
so.name = "Cam-05"
C.object.hide_set(True)

## Cam-06
bpy.ops.object.camera_add(location=(0, 0, -0.5), rotation=(0, 3.14159, 3.14159))
so = C.selected_objects[0]
so.name = "Cam-06"
C.object.hide_set(True)

## Set Camera Ortho
for obj in D.collections['PETRA'].all_objects:
    if obj.type == "CAMERA":
        print(obj.data.type)
        obj.data.type = "ORTHO"

## Define orthographic scale:

### ------
### CAM-01
cam_01 = bpy.data.objects["Cam-01"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_01.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var1a = fcurve.driver.variables.new()
var1a.targets[0].id = framing_box
var1a.targets[0].data_path = "dimensions[0]"

var1b = fcurve.driver.variables.new()
var1b.targets[0].id = framing_box
var1b.targets[0].data_path = "dimensions[2]"

### ------
### CAM-02
cam_02 = bpy.data.objects["Cam-02"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_02.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var2a = fcurve.driver.variables.new()
var2a.targets[0].id = framing_box
var2a.targets[0].data_path = "dimensions[1]"

var2b = fcurve.driver.variables.new()
var2b.targets[0].id = framing_box
var2b.targets[0].data_path = "dimensions[2]"

### ------
### CAM-03
cam_03 = bpy.data.objects["Cam-03"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_03.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var3a = fcurve.driver.variables.new()
var3a.targets[0].id = framing_box
var3a.targets[0].data_path = "dimensions[0]"

var3b = fcurve.driver.variables.new()
var3b.targets[0].id = framing_box
var3b.targets[0].data_path = "dimensions[2]"

### ------
### CAM-04
cam_04 = bpy.data.objects["Cam-04"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_04.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var4a = fcurve.driver.variables.new()
var4a.targets[0].id = framing_box
var4a.targets[0].data_path = "dimensions[1]"

var4b = fcurve.driver.variables.new()
var4b.targets[0].id = framing_box
var4b.targets[0].data_path = "dimensions[2]"

### ------
### CAM-05
cam_05 = bpy.data.objects["Cam-05"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_05.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var5a = fcurve.driver.variables.new()
var5a.targets[0].id = framing_box
var5a.targets[0].data_path = "dimensions[0]"

var5b = fcurve.driver.variables.new()
var5b.targets[0].id = framing_box
var5b.targets[0].data_path = "dimensions[1]"

### ------
### CAM-06
cam_06 = bpy.data.objects["Cam-06"].data
framing_box = bpy.data.objects["Framing Box"]
fcurve = cam_06.driver_add("ortho_scale")
fcurve.driver.type = "MAX"

var6a = fcurve.driver.variables.new()
var6a.targets[0].id = framing_box
var6a.targets[0].data_path = "dimensions[0]"

var6b = fcurve.driver.variables.new()
var6b.targets[0].id = framing_box
var6b.targets[0].data_path = "dimensions[1]"

## Parenting Cameras to 'Framing Box'
a = D.objects["Framing Box"]
b = D.objects["Cam-01"]
c = D.objects["Cam-02"]
d = D.objects["Cam-03"]
e = D.objects["Cam-04"]
f = D.objects["Cam-05"]
g = D.objects["Cam-06"]
h = D.objects["Reference Sphere"]

b.parent = a
c.parent = a
d.parent = a
e.parent = a
f.parent = a
g.parent = a
h.parent = a

## Cameras Binding
scene = C.scene
markers = {
    "F_01": {"frame": 1, "camera": "Cam-01", "frame_time": 1},
    "F_02": {"frame": 2, "camera": "Cam-02", "frame_time": 2},
    "F_03": {"frame": 3, "camera": "Cam-03", "frame_time": 3},
    "F_04": {"frame": 4, "camera": "Cam-04", "frame_time": 4},
    "F_05": {"frame": 5, "camera": "Cam-05", "frame_time": 5},
    "F_06": {"frame": 6, "camera": "Cam-06", "frame_time": 6},
}
for name, m_data in markers.items():
    # add a marker
    marker = scene.timeline_markers.new(name, frame=m_data["frame"])
    marker.camera = scene.objects.get(m_data["camera"])

## Set the length of the timeline
D.scenes[0].frame_start = 1
D.scenes[0].frame_end = 7

####################
# MOVE TO 3DCURSOR #
####################


def snap_active_to_cursor(obj: bpy.types.Object, copy_rotation=False):
    cursor = C.scene.cursor
    active_object = D.objects["Framing Box"]
    active_object.location = cursor.location

    if copy_rotation:
        active_object.rotation_euler = cursor.rotation_euler


obj = C.scene.objects["Framing Box"]
snap_active_to_cursor(obj)

####################################
# MAKE SOME OBJECTS NOT RENDERABLE #
####################################

## Deselect all objects
bpy.ops.object.select_all(action="DESELECT")

## Select some objects
for o in D.objects:
    # Check for given object names
    if o.name in ("Framing Box", "Reference Sphere"):
        o.select_set(True)

## Make those objects not renderable
selection = C.selected_objects

for obj in selection:
    obj.hide_render = not obj.hide_render

## Deselect all objects
bpy.ops.object.select_all(action="DESELECT")

## Select Framing Box (to ease resizing)
D.objects["Framing Box"].select_set(True)