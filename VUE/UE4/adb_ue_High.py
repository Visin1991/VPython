import os
import re

def get_devices():
    p = os.popen('adb devices')
    devices_str = p.read()
    devices = re.findall(r'(\w+)\s+device\s', devices_str)
    return devices

def shellcmd(device_id,command):
    cmd = 'adb -s %s shell "%s"' % (device_id, command)
    print(cmd)
    p = os.popen(cmd)
    result = p.read()
    print(result)  

devices = get_devices()
for device in devices:
    print(device)
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.MobileHDR 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.ShadowQuality 2'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'foliage.MinimumScreenSize 0.01'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'foliage.LODDistanceScale 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'grass.CullDistanceScale 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'grass.densityScale 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.MaterialQualityLevel 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.Streaming.MipBias 0'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.Mobile.SceneColorFormat 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.BloomQuality 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.DetailMode 2'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.MobileContentScaleFactor 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.SkeletalMeshLODBias 0'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.StaticMeshLODDistanceScale 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.LLSDirectionalScattering 1'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.Mobile.AllowDitheredLODTransition 0'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.DeviceFPSMin 30'")
    shellcmd(device,"am broadcast -a android.intent.action.RUN -e cmd 'r.DeviceFPSMax 60'")


    
    





