import multiplecameras
from multiprocessing import Process
import os






def camobj(cnt,name):
    cam = multiplecameras.init_cam(deviceList,cnt)
    frame = multiplecameras.GetImage(cam)
    multiplecameras.cam_show(cam,name)
    multiplecameras.stop_cam(cam)



if __name__ == "__main__":
    deviceList = multiplecameras.get_caminf()
    # camobj(0)
    print(deviceList.nDeviceNum)
    task = []
    for i in range(deviceList.nDeviceNum):
        t = Process(target=camobj, args=(i,'cam '+str(i)))
        t.start()
        task.append(t)
    
