class simplecontext:
    def __enter__(self):
        print("Entering Context")
        return self
    
    def __exit__(self,exc_type, exc_value, traceback):
        print("Exiting Context")
    
# with simplecontext():
    # print("Inside the block")



#Performance testing
class Timer:
    def __enter__(self):
        from time import time
        self.start = time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        from time import time
        self.end = time()
        print(f"Elapsed time: {self.end - self.start:.2f} seconds")

with Timer():
    sum([i for i in range(100000)])