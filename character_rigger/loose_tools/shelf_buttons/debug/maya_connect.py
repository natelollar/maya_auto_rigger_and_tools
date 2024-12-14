from maya import cmds

cmds.commandPort(name=":7001", sourceType="mel", echoOutput=True)
cmds.commandPort(name=":7002", sourceType="python", echoOutput=True)

# Update line 826:
# C:\Program Files\Autodesk\Maya2024\Python\Lib\socketserver.py
#
# def write(self, b):
#     if isinstance(b, str):
#         b = b.encode("utf-8")
#     self._sock.sendall(b)
#     with memoryview(b) as view:
#         return view.nbytes
