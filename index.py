import simulation

if __name__ == '__main__':
    market.addAssetInTransfer(1, 2, 1, 5)
    market.addAssetInTransfer(1, 2, 2, 8)

    market.addAssetInTransfer(2, 2, 3, 3)
    market.addAssetInTransfer(2, 2, 4, 4)

    '''market.addAssetInTransfer(3, 2, 5, 7)
    market.addAssetInTransfer(3, 2, 6, 1)

    market.addAssetInTransfer(4, 2, 7, 12)
    market.addAssetInTransfer(4, 2, 8, 3)'''

    for k in market.collections.keys():
        for k2 in market.collections[k].keys():
            print("utente")
            for k3 in market.collections[k][k2].keys():
                print(k3)

    #print(market.getAssetsInTransfer(3, 2))
    # print(market.getAssetsInTransfer(3, 2))
