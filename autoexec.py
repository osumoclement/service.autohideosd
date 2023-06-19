# old way: /Internal shared storage/Android/data/org.xbmc.kodi/files/.kodi/userdata
# matrix: /Internal shared storage/Android/data/org.xbmc.kodi/files/.kodi/addons/service.autoexec/{autoexec.py,addon.xml}

import xbmc
import threading

def log(msg, loglevel=xbmc.LOGDEBUG):
    xbmc.log("[autoexec.py] --> %s" % msg, level=loglevel)

def check_osd():
    while True:
        if xbmc.getCondVisibility("System.IdleTime(5)"):
            if xbmc.getCondVisibility("Window.IsActive(videoosd)"):
                xbmc.executebuiltin("Dialog.Close(videoosd)")
        xbmc.sleep(500)
        
log("starting autoexec")        
threading.Thread(target=check_osd).start()
