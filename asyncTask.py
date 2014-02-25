import threading
from functools import partial
class Task(threading.Thread):
    def __init__(self,  targetMethod,  args = None):
        threading.Thread.__init__(self)
        self.targetMethod = targetMethod
        self.args = args
    def run(self):
        print("222")
        if(self.args is None or len(self.args) == 0):
            self.targetMethod()
        else:
            method = self.targetMethod
            for obj in self.args:
                method = partial(method,  obj)
            method()
    @staticmethod
    def Start(method,  args):
        thread = Task(method,  args)
        try:
            thread.start()
        except Exception as e:
            print(e)
def cb():
    print("3333")
def cb2(a, b):
    print("%s%s"%(a, b))
if __name__=="__main__":
    Task.Start(cb,  [])
    Task.Start(cb2,  (3, 4))
    
    print("1111")
    
