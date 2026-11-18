import bpy

# ===============================
# Configuration Settings
# ===============================
fixed_pre = "SM_"
fixed_max = 100

# ===============================
# Data Collections
# ===============================
bad_names = []
high_poly = []
missing_materials = []
missing_textures = []

# ===============================
# Scene Validation
# ===============================
for obj in bpy.data.objects:
    # Only runs checks for 3D mesh objcts
    if obj.type == "MESH":
        
        # 1. Naming Convention Check
        if not obj.name.startswith(fixed_pre):
            bad_names.append(obj.name)
            # prepends
            obj.name = f"SM_{obj.name}"
            
        # 2. Polygon Limit Check
        poly_count = len(obj.data.polygons)
        if poly_count >= fixed_max:
            high_poly.append(obj.name)
            
        # 3. Material & Image Texture Check
        if len(obj.material_slots) > 0 and obj.material_slots[0].material is not None:
            mat = obj.material_slots[0].material
            has_image = False
            if mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == "TEX_IMAGE" and node.image is not NONE:
                        has_image = true
                        break
                if not has_image:
                    missing_textures.append(obj.name)
            else:
                missing_materials.append(obj.name)
         # 4. Unapplied Scale Check
        if any(round(axis, 4) != 1.0 for axis in obj.scale):
            unapplied_scales.append(obj.name)
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.transform_apply(location = False, rotation = False, scale = True)
            obj.select_set(False)
             
# ===============================
# Summary Output
# ===============================
print("\n" + "=" * 40)
print("          SCENE VALIDATION REPORT          ")
print("=" * 40)
   
print(f"\n[!] Bad Naming Prefix (Expected '{fixed_pre}'): {len(bad_names)}")
for name in bad_names:
  print(f"    - {name}")

print(f"\n[!] High Polygon Count (>= {fixed_max}): {len(high_poly)}")
for name in high_poly:
  print(f"    - {name}")

print(f"\n[!] Missing Materials: {len(missing_materials)}")
for name in missing_materials:
  print(f"    - {name}")

print(f"\n[!] Missing Image Textures: {len(missing_textures)}")
for name in missing_textures:
  print(f"    - {name}")

print(f"\n[!] Unscaled Meshes: {len(unapplied_scales)}")
for name in unapplied_scales:
    print(f"  -{name}")

print("\n" + "=" * 40)
print("              AUDIT COMPLETE               ")
print("=" * 40)
