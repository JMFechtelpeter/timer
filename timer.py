from time import time
import numpy as np

class timer(object):
    
    def __init__(self, print_times=True, times_as_array=False):
        super().__init__()
        self.print_times = print_times
        self.times_as_array = times_as_array
        if times_as_array:
            self.times = []
        else:
            self.times = {}
            
    def __enter__(self):
        self.t0 = time()
        return self
    
    def __exit__(self, exept_type, value, traceback):
        self.stop()
        if self.times_as_array:
            self.times = np.array(self.times)
        if self.print_times:
            print(self.times)

    def elapsed(self):
        return time() - self.t0
    
    def stop(self, flag=''):
        assert type(flag)==str
        if self.times_as_array:
            self.times.append(self.elapsed())
            return self.times[-1]
        else:# self.times is dict:
            if len(flag)==0:
                flag = 't{}'.format(len(self.times)+1)
            self.times[flag] = self.elapsed()
            return self.times[flag]
        
    def reset(self, flag=''):
        t = self.stop(flag=flag)
        self.t0 = time()
        return t