import collections
free_items_offer = {'E' : (2, 'B')}
pricelist = {'A' : 50, 'B' : 30, 'C': 20, 'D': 15, 'E': 40}
special_offers = {'A' :[(5, 250-200), (3, 150-130)], "B" : [(2, 60-45)]}
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    bought_items = collections.Counter(skus)
    price = 0
    # Remove all free items
    for offer in free_items_offer:
        (amount, free_item) = free_items_offer[offer]
        nbr_of_free_items = bought_items[offer]/amount
        if bought_items[free_item] - nbr_of_free_items < 0:
            bought_items[free_item] = 0
        else:
            bought_items[free_item] -= nbr_of_free_items

    # Calculate total price
    for e in bought_items.keys():
        if e not in pricelist:
            return -1
        price += bought_items[e]*pricelist[e]

    #Deduct any offers
    for item in special_offers.keys():
        nbr_of_items = bought_items[item]
        for offer in special_offers[item]:
            (amount, deduct) = offer

            price -= (nbr_of_items/amount)*deduct
            nbr_of_items = bought_items[item] % amount

    return price
