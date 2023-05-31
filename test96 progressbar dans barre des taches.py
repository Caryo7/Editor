import tkinter
import time
import PyTaskbar # the module

class gui(object):
    def __init__(self, root):
        self.root = root

if __name__ == "__main__":
    root = tkinter.Tk()
    app = gui(root)

    taskbar_progress = PyTaskbar.Progress(root.winfo_id()) # Instantiate a new progress object
    taskbar_progress.init() # Initialize the progress bar
    taskbar_progress.setState("normal") # Set the progress bar state to normal (Available: loading, normal, warning, error)
    root.update()

    for i in range(100):
        taskbar_progress.setProgress(i) # Set the progress bar value to 50%
        time.sleep(0.1)

    root.mainloop()
