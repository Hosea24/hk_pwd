import keyboard
import win32gui
import win32process
import win32api
import win32con
import ctypes
import PySimpleGUI as sg
import aes
import pickle
import os

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

d29=[[True, True, True, True, True, True, True, False, False, True, True, True, True, False, True, False, False, False, False, False, True, False, True, True, True, True, True, True, True], [True, False, False, False, False, False, True, False, True, False, False, False, True, True, True, True, False, False, False, False, True, False, True, False, False, False, False, False, True], [True, False, True, True, True, False, True, False, False, True, True, True, True, False, True, True, False, False, True, False, False, False, True, False, True, True, True, False, True], [True, False, True, True, True, False, True, False, True, False, False, False, True, True, True, False, True, True, False, True, False, False, True, False, True, True, True, False, True], [True, False, True, True, True, False, True, False, False, True, True, True, False, False, False, False, False, False, False, False, True, False, True, False, True, True, True, False, True], [True, False, False, False, False, False, True, False, True, False, True, False, False, True, True, True, False, False, True, False, True, False, True, False, False, False, False, False, True], [True, True, True, True, True, True, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, True, True, True, True, True, True], [False, False, False, False, False, False, False, False, False, True, True, True, False, False, True, True, True, False, False, False, True, False, False, False, False, False, False, False, False], [True, True, True, True, True, False, True, True, True, True, True, False, False, True, False, False, False, False, False, False, True, True, False, True, False, True, False, True, False], [True, True, True, True, False, True, False, True, False, True, True, True, False, True, True, False, True, False, True, True, False, False, False, True, True, False, True, False, True], [True, False, False, True, True, False, True, True, True, True, False, False, False, False, False, True, False, True, False, False, True, True, False, True, True, False, True, True, False], [True, False, True, False, True, False, False, False, True, True, True, True, True, False, True, True, False, False, True, True, False, False, False, False, False, False, False, True, False], [True, True, False, True, True, True, True, False, False, True, False, False, True, False, True, False, True, True, False, False, True, True, False, False, True, False, True, True, False], [True, False, True, True, True, False, False, False, True, True, False, True, False, False, True, False, True, False, True, False, True, False, True, True, True, True, True, False, True], [True, False, False, True, False, True, True, False, False, True, False, False, False, True, False, True, True, False, False, False, True, True, True, False, True, True, True, False, False], [False, False, True, True, True, False, False, False, False, False, False, False, True, False, False, True, True, False, True, False, False, False, False, True, True, False, False, True, False], [False, False, False, True, True, True, True, True, True, True, False, False, False, False, True, True, True, False, False, False, True, False, False, False, True, False, True, True, True], [True, True, True, False, True, True, False, True, False, False, True, True, False, False, False, True, True, False, True, False, True, True, False, True, True, True, True, False, True], [True, False, False, False, True, False, True, True, False, True, True, False, True, True, False, True, True, False, True, False, False, False, False, False, True, True, True, False, False], [True, False, True, True, False, False, False, False, False, True, False, False, False, False, False, True, True, False, False, True, False, False, True, False, True, True, False, False, True], [True, False, True, False, False, True, True, True, True, True, True, False, False, True, True, False, False, True, False, False, True, True, True, True, True, False, True, False, False], [False, False, False, False, False, False, False, False, True, False, False, True, True, True, False, False, True, True, True, True, True, False, False, False, True, True, False, False, True], [True, True, True, True, True, True, True, False, True, True, False, False, False, False, True, True, False, False, False, True, True, False, True, False, True, False, True, False, False], [True, False, False, False, False, False, True, False, False, False, False, False, True, False, False, True, True, False, False, True, True, False, False, False, True, False, False, False, False], [True, False, True, True, True, False, True, False, True, True, True, True, True, False, True, True, True, True, False, False, True, True, True, True, True, True, True, False, False], [True, False, True, True, True, False, True, False, True, False, False, True, False, False, True, False, False, True, True, False, True, False, False, True, False, False, False, False, True], [True, False, True, True, True, False, True, False, True, True, False, False, False, False, False, True, True, True, True, False, True, False, False, False, True, False, True, True, False], [True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, True, False, True, True, True, True, True, False, False, True, False, True, False], [True, True, True, True, True, True, True, False, True, False, False, False, False, True, False, True, False, False, False, True, False, True, False, True, True, False, True, False, False]]
sg.theme('Black')
KCODE="???????????????  ???????????????"
gui=None
def char2key(c):
    result = ctypes.windll.User32.VkKeyScanW(ord(c))
    # shift_state = (result & 0xFF00) >> 8
    vk_key = result & 0xFF
    return vk_key

def readp():
    with open("hkpwd.pwd","rb") as f:
        pwd=pickle.load(f)
    return pwd

def writep(pwd:dict):
    with open("hkpwd.pwd","wb") as f:
        pickle.dump(pwd,f)
    print("?????????")
    
def getwin():
    global gui
    hwndnow = ctypes.windll.user32.GetForegroundWindow()
    clsname = win32gui.GetClassName(hwndnow)
    hwndname=win32gui.GetWindowText(hwndnow)
    pid = win32process.GetWindowThreadProcessId(hwndnow)
    handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, pid[1])
    proc_name = win32process.GetModuleFileNameEx(handle, 0)
    rec=(clsname,hwndname,proc_name)
    return rec

def savwin():
    rec=getwin()
    gui.write_event_value('hotkey',rec)

def sendk():
    pwd=readp()
    rec=getwin()
    if rec in pwd:
        for d in pwd[rec]:
            win32api.keybd_event(9,0,0,0)
            win32api.keybd_event(9,0, win32con.KEYEVENTF_KEYUP, 0)
            k=aes.decrypt(KCODE,d).decode()
            print(k)
            for c in k:
                kcode=char2key(c)
                win32api.keybd_event(kcode,0,0,0)
                win32api.keybd_event(kcode,0, win32con.KEYEVENTF_KEYUP, 0)
                
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0, win32con.KEYEVENTF_KEYUP, 0)

    sg.Frame()
def main():
    global gui
    eico=sg.Button('???',button_color=("white","black"),border_width=0, key='Exit')
    qr = [[sg.Graph(canvas_size=(90, 90), graph_bottom_left=(0, 0), graph_top_right=(90, 90), background_color='white', enable_events=True, key='graph')]]
    gui=sg.Window('???',[[sg.Push(),eico],[sg.Column([[sg.T('F7???\n??????????????????')],[sg.T('F6???\n??????????????????')]]),sg.Push(),sg.Column(qr)]], keep_on_top=True,no_titlebar=True, alpha_channel=.5, grab_anywhere=True,finalize=True)
    graph = gui['graph']         # type: sg.Graph
    for i in range(len(d29)):
        for j in range(len(d29)):
            if d29[i][j]:
                graph.draw_rectangle((j*3+1,87-i*3),(j*3+3,89-i*3,),fill_color="black")
    gs=0
    keyboard.add_hotkey('f7',savwin)
    keyboard.add_hotkey('f6',sendk)
    while True:
        e,v=gui.read()
        print(e,v)
        if e in (sg.WIN_CLOSED, 'Exit'): 
            break
        if e=='hotkey' and gs==0:
            gs=1
            gui.hide()
            print(v)
            clsname,hwndname,proc_name=v['hotkey']
            inbox=sg.Frame('??????-??????',[[sg.In(key='in1')],[sg.In(key='in2')]],key='box')
            gsui=sg.Window('??????',[[sg.T("??????: "+clsname)],[sg.T("??????: "+hwndname)],[sg.T("??????: "+proc_name)],
                            [inbox],[sg.B("??????",bind_return_key=True),sg.B("??????"),sg.Push(),sg.B("???????????????")]],
                            finalize=True, no_titlebar=True, alpha_channel=.5, grab_anywhere=True)
            pwd=readp()
            print(pwd)
            i=3
            if v['hotkey'] in pwd:
                print("!")
                d=pwd[v['hotkey']]
                for i in range(1,len(d)+1):
                    if i>2:gsui.extend_layout(gsui['box'], [[sg.I(key=f'in{i}')]])
                    print(aes.decrypt(KCODE,d[i-1]).decode())
                    gsui[f'in{i}'](aes.decrypt(KCODE,d[i-1]).decode())
                i=len(d)+1
            while True:
                eve, val = gsui.read()
                print(eve,val)
                if eve is None or eve == 'Exit' or eve=='??????':
                    gsui.close()
                    gs=0
                    gui.UnHide()
                    break
                elif eve=="???????????????":
                    gsui.extend_layout(gsui['box'], [[sg.I(key=f'in{i}')]])
                    i+=1
                elif eve=="??????":
                    if v['hotkey'] in pwd:
                        sure,_=sg.Window("????????????",[[sg.T("?????????????????????????????????")],[sg.B('??????'), sg.B('??????',bind_return_key=True)]]).read(close=True)
                        if sure!="??????":continue    
                    d=[]
                    for j in range(1,i):
                        print(val[f'in{j}'])
                        d.append(aes.encrypt(KCODE,val[f'in{j}']))
                    pwd[v['hotkey']]=d
                    writep(pwd)

                                
                            

    gui.close()

if __name__ == "__main__":
    if not os.path.isfile("hkpwd.pwd"):
        pwd={}
        writep(pwd)
    main()

