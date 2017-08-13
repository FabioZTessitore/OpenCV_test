import cv2
import optparse

usage = "$ python %prog OPTIONS"

def handleOptions():
    parser = optparse.OptionParser(usage)

    parser.add_option('-f', dest='filename', help='read data from FILENAME')

    (options, args) = parser.parse_args()
    if options.filename==None:
        parser.error("incorrect number of arguments, use -h for help")
        exit(0)

    return options

options = handleOptions()
filename = options.filename

img = cv2.imread(filename)
if img is None:
    print "file not found"
    exit(0)

cv2.namedWindow("DisplayImage")
cv2.imshow('DisplayImage', img)

cv2.waitKey(0)
cv2.destroyWindow("DisplayImage")
