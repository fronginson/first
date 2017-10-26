class Door:
    def __init__(self, a, b):
        self.width = a
        self.height = b
    def polotno(self):
        area = self.height * self.width
        return area


bdoor = Door(1000, 2200)
mdoor = Door(900, 2100)
sdoor = Door(800, 2100)

print('Big door parameters:')
print('Width: %s mm' %bdoor.width)
print('Height: %s mm' %bdoor.height)
print('Area: %s m\u00b2' %(Door.polotno(bdoor)/1000000))
