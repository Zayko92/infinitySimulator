import copy

# collectionId => userId => tokenId => price
# mapping(collectionId => mapping(userId => mapping(tokenId => price)))

tokenId = dict()
userId = dict()
collections = dict()


# Add asset in transfer
def addAssetInTransfer(_userId, _collectionId, _tokenId, _price):
    try:
        collections[_collectionId][_userId][_tokenId]
        return False

    except:

        if len(collections.keys()) == 0 or _userId not in collections[_collectionId].keys():
            tokenId[_tokenId] = _price
            userId[_userId] = tokenId
            collections[_collectionId] = userId

        else:
            collections[_collectionId][_userId][_tokenId] = _price

        return True


# Remove asset from transfer
def removeAssetFromTransfer(_userId, _collectionId, _tokenId, _price):
    try:
        del collections[_collectionId][_userId][_tokenId]
        return True

    except:
        return False


# Buy Item
def buyItem(_currentUserId, _newUserId, _collectionId, _tokenId):
    try:
        del collections[_collectionId][_currentUserId][_tokenId]
        # transferToken(_currentUserId, _newUserId, _tokenId)
        return True
    except:
        return False


# Get the assets in transfer of a user of a specific collection
def getAssetsInTransfer(_userId, _collectionId):
    try:
        assets = collections[_collectionId][_userId]

        ids = []

        for k in assets.keys():
            ids.append(k)

        return ids

    except:
        return []


# Returns the id of an asset belonging to a certain collection with the lowest price removing owned
def lowestPriceAsset(_userId, _collectionId):
    try:
        collection = copy.deepcopy(collections[_collectionId])

        minPrice = None
        referenceId = None
        owner = None

        if _userId in collection.keys():
            del collection[_userId]

        for k in collection.keys():
            for k2 in collection[k].keys():
                if minPrice is None or minPrice < collection[k][k2]:
                    minPrice = collection[k][k2]
                    referenceId = k2
                    owner = k

        return owner, referenceId

    except:
        return []
