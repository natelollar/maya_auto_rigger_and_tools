import maya.mel as mel



def vs_code_port_connect():
    mel.eval('commandPort -n "localhost:7001" -stp "mel" -echoOutput')
