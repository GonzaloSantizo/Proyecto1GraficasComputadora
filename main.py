import shaders
from gl import Renderer, V2, color

width = 1000
height = 1000

rend = Renderer(width,height)

rend.glBackgroundTexture("textures/pic1.bmp")
rend.glClearBackground()

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader
#rend.glCamMatrix(translate=(1,2,0))


#distancia de camera x,y,z
#distancia de camara x,y,y
rend.glLookAt(camPos=(0,0,0),eyePos=(0,0,-3))


# Modelo 1
#rend.glLoadModel(filename="Squid.obj",textureName="model.bmp",translate=(0,0,-5),rotate=(0,0,0),scale=(0.25,0.25,0.25))

#Modelo 2
#rend.glLoadModel(filename="Patrick.obj",textureName="model.bmp",translate=(0,0,-5),rotate=(0,0,0),scale=(0.5,0.5,0.5))

# Modelo 3
#rend.glLoadModel(filename="Kevin.obj",textureName="model.bmp",translate=(0,0,-5),rotate=(0,0,0),scale=(1,1,1))

# Modelo 4
rend.glLoadModel(filename="Crabs.obj",textureName="model.bmp",translate=(0,0,-5),rotate=(0,0,0),scale=(0.25,0.25,0.25))

rend.glRender()
rend.glFinish("output.bmp")