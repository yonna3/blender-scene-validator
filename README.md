# Blender Scene Validator ('bpy')

A lightweight Python tool for Blende that automatically audits 3D mesh objects in a scene and outputs a grouped summary report to the System Console.

## Features
- **Naming Convention Check:** Flags mesh objects that do not start with a required prefix (default: 'SM_')
- **Polygon Count Check:** Flags meshes that exceed a configurable face limit
- **Material & Texture Validation:** Identifies meshes that are missing a material slot or a loaded image texture node
- **Grouped Summary Report:** Collects all these issues and prints a categorized report at the end. 

## How to Run
1. Open your scene in **Blender**.
2. Switch to the **Scripting** workspace tab.
3. Open 'scene_validator.py' in the Text Editor. 
4. Adjust 'fixed_pre' and 'fixed_max' at the top of the script if needed.
5. Open the System Console via **Window > Toggle System Console** (Windows).
6. Click **Run Script** to view the validation report. 