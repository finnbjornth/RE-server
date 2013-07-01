import math

class ExtensionInfo:
	def __init__(self, init_name, init_permissions, init_enabled, init_id):
		self.name = init_name
		self.permissions = init_permissions
		self.enabled = init_enabled
		self.id = init_id
	def toString(self):
		return "Name: " + self.name + \
			", Permissions: " + self.permissions + \
			", Enabled: " + str(self.enabled) + \
			". [Class: ExtensionInfo]"

class ProcessedExtensionInfo:
	def __init__(self, extensionInfo):
		self.name = extensionInfo.name
		self.enabled = extensionInfo.enabled
		self.SetCategory( extensionInfo.permissions )
		self.SetRank( extensionInfo.permissions )
		self.id = extensionInfo.id

	def SetCategory(self, permissions):
		websiteAccess = 0
		dataAccess = 0
		crazy = "experimental" in permissions
		for p in permissions:
			if websiteAccess < 2 and p[:10] == "http://*/*":
				websiteAccess = 2
			elif websiteAccess < 1 and p[:4] == "http":
				websiteAccess = 1
			if dataAccess < 2 and p in ["privacy", "management", "clipboardWrite", "bookmarks", "webRequestBlocking"]:
				dataAccess = 2
			elif dataAccess < 1 and p in ["tabs", "activeTab", "clipboardRead", "contentSettings", "geolocation", "history", "idle", "proxy", "topSites", "webNavigation", "webRequest"]:
				dataAccess = 1

		if websiteAccess == 0 and dataAccess == 0 and not crazy:
			self.category = "Dumb Machine"
		else:
			composite = websiteAccess + dataAccess * 3
			crazy = ("crazy" if crazy else "") + (" " if crazy and composite > 0 else "")
			
			result = {#switch case
				0: "",
				1: "Snoop",
				2: "Omnipresent Being",

				3: "Ninja",
				4: "Snooping Ninja",
				5: "Omnipresent Ninja",

				6: "Stalker",
				7: "Snooping Stalker",
				8: "Omnipresent Stalker"
			}[composite]

			self.category = crazy + result
	def SetRank(self, permissions):
		ranks = {
			0 : "Pipsqueak",
			1 : "Small Fry",
			2 : "Average Joe",
			3 : "Titan",
			4 : "Zeus"
		}
		weights = {
			"privacy" : 2,
			"management" : 1,
			"bookmarks" : 0.75,
			"tabs" : 0.75,
			"history" : 0.75,
			"webRequestBlocking" : 0.5,
			"proxy" : 0.5,
			"topSites" : 0.5,
			"webNavigation" : 0.5,
			"webRequest" : 0.5,
			"idle" : 0.375,
			"activeTab" : 0.25,
			"contentSettings" : 0.25,
			"clipboardWrite" : 0.25,
			"clipboardRead" : 0.125,
			"geolocation" : 0.125
		}
		weightedSum = 0
		for p in permissions:
			weightedSum += weights.get(p, 0.125)#0.125 is the default value
		weightedSum = math.floor(weightedSum)
		if weightedSum > 4:
			weightedSum = 4
		self.rank = ranks[weightedSum]

	def toString(self):
		return "Name: " + self.name + \
			", Category: " + self.category + \
			", Rank: " + self.rank + \
			", Enabled: " + str(self.enabled) + \
			". [Class: ProcessedExtensionInfo]"

def Rate(extensionList):#takes a list of ExtensionInfo instances
	processedList = []
	for x in extensionList:
		processedList.append( ProcessedExtensionInfo(x) )
	return processedList

"""
#a simple test
list = [ExtensionInfo("yay", ["tabs"], True), ExtensionInfo("hmmm", ["management"], False)]
list = Rate(list)
for x in list:
	print x.name + ", " + x.category + ", " + x.rank + ", " + str(x.enabled)
"""