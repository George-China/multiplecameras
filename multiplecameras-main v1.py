import multiplecameras




deviceList = multiplecameras.get_caminf()
cam = multiplecameras.init_cam(deviceList,0)
multiplecameras.GetImage(cam)
multiplecameras.cam_show(cam)
multiplecameras.stop_cam(cam)

