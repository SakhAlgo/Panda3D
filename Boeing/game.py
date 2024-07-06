# напиши здесь код основного окна игры
from math import pi, sin, cos

from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        self.model = loader.loadModel('Sailboat.egg')
        # self.scene.setPos(2, 2, 0.5)
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        self.model.reparentTo(self.render)
        
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, -1)
        base.camLens.setFov(70)
        self.scene.setScale(0.2)


        self.model.setScale(0.25, 0.25, 0.25)
        self.model.setPos(-8, 12, 0)
        base.camLens.setFov(70)
        self.model.setScale(0.5)
        # Add the spinCameraTask procedure to the task manager.
        # self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

    # # Define a procedure to move the camera.
    # def spinCameraTask(self, task):
    #     angleDegrees = task.time * 6.0
    #     angleRadians = angleDegrees * (pi / 180.0)
    #     self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
    #     self.camera.setHpr(angleDegrees, 0, 0)
    #     return Task.cont


app = MyApp()
app.run()