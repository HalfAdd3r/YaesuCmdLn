import Yaesu857D

bob = Yaesu857D.radio("COM3")

print(bob.freq())
print (bob.mode())

bob.toggleVFO()

print(bob.freq())
print (bob.mode())

