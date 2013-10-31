import numpy 
import gauss2d as agpy

def makeGaussian(size, fwhm = 3, center=None):
    """ Make a square gaussian kernel.

    size is the length of a side of the square
    fwhm is full-width-half-maximum, which
    can be thought of as an effective radius.
    """

    x = numpy.arange(0, size, 1, float)
    y = x[:,numpy.newaxis]

    if center is None:
        x0 = y0 = size // 2
    else:
        x0 = center[0]
        y0 = center[1]

    return numpy.exp(-4*numpy.log(2) * ((x-x0)**2 + (y-y0)**2) / fwhm**2)



def gauss2d(backgr, height, shape, center=None, width=None, theta=None):
    if type(shape) != list :
	shape = [float(shape), float(shape)]
    else:
	shape = [float(shape[0]), float(shape[1])]

    if center == None :
	center = [float(shape[0])/2, float(shape[1])/2]
    else:
	center = [float(center[0]), float(center[1])]

    if width == None :
	width = [float(shape[0])/5, float(shape[1])/5]
    else:
	width = [float(width[0]), float(width[1])]

    if theta == None :
	theta = 0
    else:
	theta = float(theta)

    return agpy.twodgaussian([backgr, height, float(center[0]), float(center[1])
					    , float(width[0]) , float(width[1]), float(theta)], shape=shape)

def gauss2d_shim(b, a, par):
    return gauss2d(b, a, *par)

def init():
	rpndef("gauss", makeGaussian, [num, num, num])
	rpndef("gauss2d", gauss2d_shim, [num, num, any])
	rpndef("poisson", numpy.random.poisson, [num])

