import bpy, bmesh
import numpy as np

from utils.ambientOcclusion import *
from utils.blenderInit import *
from utils.colorMap import *
from utils.drawPointCloud import *
from utils.invisibleGround import *
from utils.lookAt import *
from utils.readPLY import *
from utils.readOBJ import *
from utils.setCamera import *
from utils.setLight_sun import *
from utils.setLight_ambient import *
from utils.setMat_edge import *
from utils.setMat_normal import *
from utils.setMat_transparent import *
from utils.setMat_VColor import *
from utils.setVColor import *
from utils.subdivision import *

derekBlue = (144.0/255, 210.0/255, 236.0/255, 0)
coralRed = (250.0/255, 114.0/255, 104.0/255, 0)
iglGreen = (153.0/255, 203.0/255, 67.0/255, 0)