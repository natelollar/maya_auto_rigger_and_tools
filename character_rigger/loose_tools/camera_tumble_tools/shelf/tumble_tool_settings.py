// set camera Tumble Tool correct settings
// View < Camera Tools
tumbleCtx -e -localTumble 0 tumbleContext;
tumbleCtx -e -objectTumble false tumbleContext;
tumbleCtx -e -autoSetPivot false tumbleContext;
tumbleCtx -e -orthoLock true tumbleContext;
print "----Tumble pivot ONLY----"


#resetTool tumbleContext;
#print "----Tumble Tool RESET----";