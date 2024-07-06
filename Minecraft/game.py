from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand('land.txt')
        self.hero = Hero((10,10,1.5), self.land)
        
        base.camLens.setFov(90)

app = MyApp()
app.run()

