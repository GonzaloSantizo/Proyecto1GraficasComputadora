import ml
#import random
#viewMatrix=None
#projectionMatrix=None


def vertexShader(vertex,**kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix= kwargs["viewMatrix"]
    projectionMatrix= kwargs["projectionMatrix"]
    vpMatrix= kwargs["vpMatrix"]
    vt = [vertex[0],vertex[1],vertex[2],1]

    vt =vpMatrix* projectionMatrix*viewMatrix*modelMatrix @ vt
    vt = vt.tolist()[0]
    vt = [vt[0] / vt[3], vt[1] / vt[3], vt[2] / vt[3]]
    return vt


# Original
# def fragmentShader(**kwargs):
#     textCoords = kwargs["textCoords"]
#     texture = kwargs["texture"]

#     if texture !=None:
#         color = texture.getColor(textCoords[0],textCoords[1])
#     else:
#         color = (1,1,1)
#     return color


#Black and White Shader
# def fragmentShader(**kwargs):
#     textCoords = kwargs["textCoords"]
#     texture = kwargs["texture"]
#     edgeThreshold = 0.1  # Umbral para detectar bordes

#     if texture != None:
#         color = texture.getColor(textCoords[0], textCoords[1])
#     else:
#         color = (1, 1, 1)
    
#     # Detectar bordes usando diferencias en los canales de color
#     grayscale = 0.2989 * color[0] + 0.5870 * color[1] + 0.1140 * color[2]
#     edgeColor = (0, 0, 0)
#     if abs(color[0] - grayscale) > edgeThreshold or \
#        abs(color[1] - grayscale) > edgeThreshold or \
#        abs(color[2] - grayscale) > edgeThreshold:
#         color = edgeColor
#     else:
#         # Reducir el número de niveles de color para lograr el aspecto de caricatura
#         numLevels = 6
#         color = tuple(round(c * (numLevels - 1)) / (numLevels - 1) for c in color)

#     return color



#Negative colors
# def fragmentShader(**kwargs):
#     textCoords = kwargs["textCoords"]
#     texture = kwargs["texture"]

#     if texture != None:
#         color = texture.getColor(textCoords[0], textCoords[1])
#     else:
#         color = (1, 1, 1)
    
#     invertedColor = (1 - color[0], 1 - color[1], 1 - color[2])

#     return invertedColor


def fragmentShader(**kwargs):
    textCoords = kwargs["textCoords"]
    texture = kwargs["texture"]

    if texture != None:
        color = texture.getColor(textCoords[0], textCoords[1])
    else:
        color = (1, 1, 1)
    
    grayscaleValue = 0.2989 * color[0] + 0.5870 * color[1] + 0.1140 * color[2]
    grayColor = (grayscaleValue, grayscaleValue, grayscaleValue)
    
    return grayColor



