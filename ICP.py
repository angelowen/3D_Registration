import open3d as o3d
import numpy as np
import copy


def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])
    return source_temp+target_temp


if __name__ == "__main__":
    
    source = o3d.io.read_point_cloud("DOLL_PLY/XYZ_1.ply")
    target = o3d.io.read_point_cloud("DOLL_PLY/XYZ_2.ply")
    threshold = 0.2
    th = np.deg2rad(15.0)
    # trans_init = np.asarray([[1, 0, 0, 0],
    #                          [0, 1, 0, 0],
    #                          [0, 0, 1, 0],
    #                          [0, 0, 0, 1]])
    o3d.visualization.draw_geometries([source+target])
    trans_init = np.asarray([[np.cos(th), -np.sin(th),  0, 0],
                             [np.sin(th), np.cos(th), 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])
    # draw_registration_result(source, target, trans_init)
    # print("Initial alignment")
    # evaluation = o3d.pipelines.registration.evaluate_registration(source, target,
    #                                                     threshold, trans_init)
    # print(evaluation)
    # # exit()
    # print("Apply point-to-point ICP")
    # reg_p2p = o3d.pipelines.registration.registration_icp(
    #     source, target, threshold, trans_init,
    #     o3d.pipelines.registration.TransformationEstimationPointToPoint())
    # print(reg_p2p)
    # print("Transformation is:")
    # print(reg_p2p.transformation)
    # print("")
    # draw_registration_result(source, target, reg_p2p.transformation)
    
    print("Apply point-to-plane ICP")
    reg_p2l = o3d.pipelines.registration.registration_icp(
        source, target, threshold, trans_init,
        o3d.pipelines.registration.TransformationEstimationPointToPlane())
    print(reg_p2l)
    print("Transformation is:")
    print(reg_p2l.transformation)
    print("")
    source = draw_registration_result(source, target, reg_p2l.transformation)
    # target = o3d.io.read_point_cloud("XYZ_0.ply")
    # reg_p2l = o3d.pipelines.registration.registration_icp(
    #     source, target, threshold, trans_init,
    #     o3d.pipelines.registration.TransformationEstimationPointToPlane())
    # draw_registration_result(source, target, reg_p2l.transformation)

