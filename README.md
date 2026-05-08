# RigModular
The goal of this tool is to make rigging modular to reduce repetition and speed up basic character controls.

### How to Install
##### Download ZIP
- Click green 'Code' Button
- Click 'Download ZIP'
- Extract folder
- Place the extracted folder under Maya's 'scripts' folder
- Open Maya
- Copy and paste this code into Maya's script editor:

import rigModule
import importlib
importlib.reload(rigModule)

win = rigModule.windowGui()
win.show()

### Features
UI
- Have a clean and clear GUI for this tool
Controller Generator
- pulls unique controller from folder
- edit color, size, shape
- used for the rest of the rif modular
Rig Handle Generator
- able to make ik, fk, ikfk, spline, ribbons
- ability to customize and put multiple handles into a BIND skeleton, ie: ik/fk
- used for the more complex rig modules
Body Part Rig Modulars
- ability to select body part from drop-down
- make handles based on body part, ie: spline for spine
- hopefully be able to make more complex handles outside of the rig handle generator, ie: reverse foot setup
Human/Biped Skeleton Creator/Simulator
- spits out a human/quadruped skeleton for the user to move
- eventually will also spit out curbs used for the PVs and maybe ribbons
- after satified with skeleton placements, selecting the whole skeleton and interacting with the tool again will generate a fully modular human rig
- *hardest feature*

### Goals
- Create an easy-to-use UI window and improve on PySide.
- Make sure the tool works on different kinds of joints.
- Create unique controls.
- Help speed up making a functioning rig.
- Improve on GitHub commits and naming.
- Have controls and groups follow a common joint naming convention.

## TODO:

Make UI
  -make a window
  -make dividers to separate each feature
  - controller ui
    - shape
    - size
    - color
  - rig handles ui
    - ik
    - fk
    - spline
    - ribbon
    - ikfk
    - custom handle switch
  - body part modular ui
    - body part
    - size
    - shape
    - colors
  - full modular skeleton ui
    - make skeleton: human/quadruped
    - generate rig

Rig Modular
~~-Controllers~~
  ~~-editable shapes~~
  ~~-editable colors~~
  ~~-editable sizes~~
-Switches/Handles
  -ik
  -fk
  -spline
  -ribbon
  -ikfk switch
  -customizable switch
-Body Part
  -legs, arms, spine, tail, tongue, eye, mouth, brow, ect...
  -size
  -color
-Skeleton Modular
  -spits out human/quad skeleton
  -editable skeleton size?
  -generates modular after selecting skeleton (or maybe automatically?) and clicking generate



