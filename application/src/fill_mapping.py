import random


def create_shopping_tour(order_products, min_products, max_products, randomness):
    num_products = random.randint(min_products, max_products)
    tour = []
    while len(order_products)>num_products:
        del(order_products[random.randint(0, len(order_products)-1)])

    for i in range(num_products):
        for j in range(len(order_products)):
            if random.random() < randomness or (j == len(order_products)-1):
                tour.append(order_products[j])
                del(order_products[j])
                break
    return tour

if __name__ == '__main__':
    tour = create_shopping_tour(order_products=[0,1,2,3,4,5,6,7,8,9,10], min_products=4, max_products=6, randomness=0.9)
    print(tour)