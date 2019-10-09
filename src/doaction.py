import os

class DoAction():
    def __init__(self, parent):
        self.window = parent

    def OnRename(self, source_, target_):
        #print(source)
        #print(target)
        source = self._removeEmptyItem(source_)
        sourceCount = len(source)
        target = self._removeEmptyItem(target_)
        targetCount = len(target)

        if (sourceCount == 0):
            return False, "There is no source filenames!"

        if (targetCount == 0):
            return False, "There is no target filenames!"
        
        if (sourceCount != targetCount):
            return False, "File count is not matched!"

        idx = 0
        result = True
        erroFileList = []
        for f in source:
            tmpResult = self._renameFile(f, target[idx])
            if (tmpResult == False):
                erroFileList.append(f)
                result = False
            idx += 1

        if (result == False):
            errorMsg = "Fail to reanme: " + "".join(erroFileList)
            return False, errorMsg
        return result, "Finish!"

    def _removeEmptyItem(self, filelist):
        result = []
        for f in filelist:
            if len(f) == 0:
                continue
            result.append(f)
        return result

    def _renameFile(self, source, target):
        if os.path.exists(source) == False:
            return False
        if source == target:
            print("source and target is same!")
            return True
        try:
            os.rename(source, target)
        except:
            return False

        return True