##
##

# File auto-generated against equivalent DynamicSerialize Java class
# and then modified post-generation to add additional features to better
# match Java implementation.
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    05/29/13         2023         dgilling       Initial Creation.
#    06/29/15         4480         dgilling       Implement __hash__, __eq__
#                                                 and __str__.
#
#

class MasterLevel(object):

    def __init__(self, name=None):
        self.name = name
        self.description = None
        self.unitString = None
        self.type = None
        self.identifier = None

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        else:
            return self.name == other.name

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        retVal = "MasterLevel["
        retVal += "name=" + str(self.name) + ","
        retVal += "type=" + str(self.type) + ","
        retVal += "unit=" + str(self.unitString) + ","
        retVal += "description=" + str(self.description)
        retVal += "]"
        return retVal

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getUnitString(self):
        return self.unitString

    def setUnitString(self, unitString):
        self.unitString = unitString

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def getIdentifier(self):
        return self.identifier

    def setIdentifier(self, identifier):
        self.identifier = identifier

