class ExtensionInfo:
	def __init__(self, init_name, init_permissions, init_enabled):
		self.name = init_name
		self.permissions = init_permissions
		self.enabled = init_enabled
class ProcessedExtensionInfo:
	def __init__(self, extensionInfo):
		self.name = extensionInfo.name
		self.enabled = extensionInfo.enabled
		self.category = "Dumb Machine"
		self.rank = "Pipsqueek"
		"""self.setCategory( extensionInfo.permissions )
		self.setRank( extensionInfo.permissions )
	def setCategory(self, permissions):
		websiteAccess = 0
		dataAccess = 0
		crazy = "experimental" in permissions
		for p in permissions:

			if(websiteAccess < 2 and p[:10] == "http://*/*" )
				websiteAccess = 2
			else if(websiteAccess < 1 and p[:4] == "http")
				websiteAccess = 1

			if(dataAccess < 2 and (p == "privacy" or p == "management"))
				dataAccess = 2
			else if(dataAccess < 1 and (p == "tabs" or p == "activeTab"))
				dataAccess = 1
		

	def setRank(self, permissions):"""

def Rate(extensionList):#takes a list of ExtensionInfo instances
	processedList = []
	for x in extensionList:
		processedList.append( ProcessedExtensionInfo(x) )
	return processedList
"""
list = [ExtensionInfo("yay", ["tabs"], True), ExtensionInfo("hmmm", ["management"], False)]
list = Rate(list)
for x in list:
	print x.name + ", " + x.category + ", " + x.rank + ", " + str(x.enabled)"""