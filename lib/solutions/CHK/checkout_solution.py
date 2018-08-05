import collections
pricelist = {'A' : 50, 'B' : 30, 'C': 20, 'D': 15}
special_offers = {'A' :(3, 150-130), "B" : (2, 60-45)}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    bought_items = collections.Counter(skus)
    price = 0
    for e in bought_items.keys():
        if e not in pricelist:
            return -1
        price += bought_items[e]*pricelist[e]
    for offer in special_offers.keys():
        (amount, deduct) = special_offers[offer]
        price -= (bought_items[offer]/amount)*deduct

    return price
