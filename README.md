# super-apply-modifier
Applies Subdivision Surface or Mirror modifier on Meshes with Shape Keys on Blender.

Normally, Blender doesn't allow you to apply a mirror/subdivison surface modifier to the mesh when it has shapekeys. This works around that limitation by creating a separate mesh for each shape key, applying the modifiers on the separate meshes, and then merge them back together as shapekeys.

## Steps to use
1. Copy the script in to the Blender project
2. Select the Mesh to apply the modifiers with
3. Run the script!

## Caveats (if a shape key is missing)
The script would fail if the shape key variants of the meshes end up having a different vertex count than the basis shape key, i.e. when vertexes are merged together in a mirror modifier. To start over, you can undo the changes with ctrl+z.
