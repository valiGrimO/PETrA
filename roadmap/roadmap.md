# List of tasks for the development of PETrA

**Legend:**
- [ ] **M** :large_blue_circle: task to do, dedicated to **Michael**, with low priority
- [ ] **V** :yellow_circle: task to do, dedicated to **Valentin**, with medium priority
- [ ] :red_circle: task to do, with high priority
- [x] completed task
- [x] :green_circle: validated task

## Camera Management
- [x] **M** :green_circle: when previewing a camera, we should look through this camera and select this camera
- [x] **M** :green_circle: Rename the editable value "resolution" into "spatial resolution"
- [x] **M** :green_circle: show uneditable resolution (in ppi)
- [ ] **M** :red_circle: How to manage more than 6 cameras?
- [ ] **M** :red_circle: Fix the dimensions (H and V) of the camera. The resolution is wrong too... :confused: Results should be the same as what we get with `PETrA/roadmap/renderSize.ods`
- [ ] **M** :red_circle: Compute in real time H and V value of the camera, depending on the size of the "framing box", the scale of documentation, and the spatial resolution
  - Would it be still possible to get the size in pixel later in the paradata file?
- [ ] **M** :red_circle: show in real time uneditable printed size of rendered pictures (in cm)

## Developments about materials
### C1, color
- [ ] :large_blue_circle: : Image decorrelation

### R2, contour lines
- [x] **M** :green_circle: **render script** : we have a weird effect if rotation is different of 0, and scale different of 1. We should warn the user to apply rotation and scale (`ctrl` + `A`) or propose to apply it for him. -> add a warning about orientation and scale
- [x] **M** :green_circle: **render script** : how to affect the output name with the spacing value? The idea is to achieve an output file name like 'cam##_R2_CL-xmm'
- [ ] **M** :yellow_circle: **user interaction** : integrate the control of spacing in the side bar

### R3, deviation map
- [x] **M** :green_circle: **external plugin** : in the DM plugin, how to name correctly output (for instance ,"DM1" instead of "DM", "DM2" instead of "DM.001")
- [ ] **M** :yellow_circle: **external plugin** : integrate the plugin "deviation map" to compute the distance between 2 meshes. It is already configured to meet the PETrA requirement. We don't need to show him, just compute the distance
- [ ] **V** :red_circle: **material** : add control on median value in the material node
- [ ] **V** :red_circle: **material** : add out of range value (blue colored vertices) in the mask layer
- [ ] **M** :yellow_circle: **render script** : how to affect the output name with the extreme and median values? The idea is to achieve an output file name like 'cam##_R3_DM`a`-`b`-`c`-`d`mm' where `a` is the ID of the deviation map computation ; `b` is the minimum value ; `c` is the median value ; `d` is the maximum value.
- [ ] **M** :large_blue_circle: **render script** when rendering, if R3 is selected, check if one `DM` vertex color at least is present on the selected mesh
- [ ] **M** :large_blue_circle: **render script** if there is several `DM` vertex color, create a loop to render each one
- [ ] **M** :large_blue_circle: **user interaction** : interact in the side panel with median and extreme values

**_Open questions_**
- user can produce several `DM` layer. How to document them? In a sense of which parameters were used to produce the comparison mesh, and for which purpose?

## Layer of information Setup
- [x] **M** :green_circle: **render script:** help to finish to write action's scripts
  - [x] how to remove a link?
  - [x] how to apply (and not rename) a matrial to a selected object, and a specific object?
  - [x] how to hit "produce documentation"?
  - [x] how to mute and unmute a node?
- [x] **M** :green_circle: How to rename a node?
- [ ] **V** :red_circle: Finish to write each layer
- [ ] **M** :yellow_circle: Integrate scripts in the user interface

## User interface, general interactions
- [ ] **M** :yellow_circle: load action's scripts and add a player to execute them (layer renderer), when every script will work fine
- [ ] **M+V** :large_blue_circle: add "help button" in the panel, in relation with each layer and/or parameter, linking to a specific page of the documentation for R3 at least, but probably each layer
- [ ] **V** :yellow_circle: rewrite the whole documentation, but in English this time
- [ ] **M** or **V** :yellow_circle: How to remove the `modelling` tab present by default in Blender? In this tab, we enter directly in edit mode, and since we are working with huge meshes, it is time consumming to wait until everything is loaded as we don't need to interact...

## Other
- Need feedback about paradata and automatic layout

# Roadmap for the development of ICEO
- Coming after PETrA will be completed!