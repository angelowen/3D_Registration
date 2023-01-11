import open3d as o3d
import numpy as np
import copy

pcd_combined = o3d.io.read_point_cloud("multiway_registration_all.pcd")
pcd_combined.paint_uniform_color([1, 0.706, 0])
o3d.visualization.draw_geometries([pcd_combined])