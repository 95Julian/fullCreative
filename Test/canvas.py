from Pages.canvaspage import Canvas


class CanvasTest(Canvas):
    def __int__(self, driver):
        super().__int__(driver)


exe = CanvasTest()
exe.drawline()
exe.drawrectangle()
exe.eraseline()
exe.drawcircle()
exe.erasecircle()

