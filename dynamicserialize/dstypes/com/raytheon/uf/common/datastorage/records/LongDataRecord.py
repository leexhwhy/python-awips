
# File auto-generated against equivalent DynamicSerialize Java class
# and then modified by njensen

class LongDataRecord(object):

    def __init__(self):
        self.longData = None
        self.name = None
        self.dimension = None
        self.sizes = None
        self.maxSizes = None
        self.props = None
        self.minIndex = None
        self.group = None
        self.dataAttributes = None
        self.fillValue = None
        self.maxChunkSize = None

    def getLongData(self):
        return self.longData

    def setLongData(self, longData):
        self.longData = longData

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDimension(self):
        return self.dimension

    def setDimension(self, dimension):
        self.dimension = dimension

    def getSizes(self):
        return self.sizes

    def setSizes(self, sizes):
        self.sizes = sizes

    def getMaxSizes(self):
        return self.maxSizes

    def setMaxSizes(self, maxSizes):
        self.maxSizes = maxSizes

    def getProps(self):
        return self.props

    def setProps(self, props):
        self.props = props

    def getMinIndex(self):
        return self.minIndex

    def setMinIndex(self, minIndex):
        self.minIndex = minIndex

    def getGroup(self):
        return self.group

    def setGroup(self, group):
        self.group = group

    def getDataAttributes(self):
        return self.dataAttributes

    def setDataAttributes(self, dataAttributes):
        self.dataAttributes = dataAttributes

    def getFillValue(self):
        return self.fillValue

    def setFillValue(self, fillValue):
        self.fillValue = fillValue

    def getMaxChunkSize(self):
        return self.maxChunkSize

    def setMaxChunkSize(self, maxChunkSize):
        self.maxChunkSize = maxChunkSize

    def retrieveDataObject(self):
        return self.getLongData()

    def putDataObject(self, obj):
        self.setLongData(obj)
