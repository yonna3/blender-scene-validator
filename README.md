# Blender Scene Validator ('bpy')

A lightweight Python tool for Blende that automatically audits 3D mesh objects in a scene and outputs a grouped summary report to the System Console.

## Features
- **Naming Convention Check:** Flags mesh objects that do not start with a required prefix (default: 'SM_')
- **Polygon Count Check:** Flags meshes that exceed a configurable face limit ('fixed_max')
- **Material & Texture Validation:** Identifies meshes that are missing a material slot or a node-based 'TEX_IMAGE' node with an assigned image. 
- **Unapplied Scale & Rotation Audit:** Checks mesh scale and Euler Rotation against '(1.0, 1.0, 1.0)' and '(0.0, 0.0, 0.0)' using rounded axis values, applying fixes per channel when 'AUTO_FIX' is enabled. 
- **Grouped Summary Report:** Collects all these issues and prints a categorized report at the end. 

## How to Run
1. Open your scene in **Blender** and ensure you are in **Object Mode**. 
2. Switch to the **Scripting** workspace tab.
3. Open 'scene_validator.py' in the Text Editor. 
4. Adjust 'fixed_pre' and 'fixed_max' at the top of the script if needed.
5. Open the System Console via **Window > Toggle System Console** (Windows).
6. Click **Run Script** (or press 'Alt + P') to view the validation report. 
