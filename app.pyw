from infi.systray import SysTrayIcon
import win32serviceutil as service
import time, threading, os

hover_text = "Vanguard Toggler"

def vgc_off(sysTrayIcon):
    print ("Attempting tp stop VGC service.")
    os.system('net stop vgc')
    
def vgc_on(sysTrayIcon):
    print ("Attempting tp start VGC service.")
    os.system('net start vgc')
    
def bye(sysTrayIcon):
    exit()
    print ('Go with honor, friend.')
def do_nothing(sysTrayIcon):
    pass
menu_options = (('Stop VGC Service', None, vgc_off),
                ('Start VGC Service', None, vgc_on),
                                              )
sysTrayIcon = SysTrayIcon("resources/warn.ico", hover_text, menu_options, on_quit=bye, default_menu_index=1)
sysTrayIcon.start()
WAIT_SECONDS = 1

def foo():
    if service.QueryServiceStatus('vgc')[1] == 4:
        sysTrayIcon.update(icon='resources/on.ico')
    else:
        sysTrayIcon.update(icon='resources/off.ico')

    threading.Timer(WAIT_SECONDS, foo).start()
    
foo()
