import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "/home/tarena/PycharmProjects/")))
from unit1.project.msg_system.system_view import SystemView

if __name__ == "__main__":
    view = SystemView()
    view.start()
    view.update()