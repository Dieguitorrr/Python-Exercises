# Restaurants

class Restaurant:
    name = ""
    description = ""
    rating = 0.0
    delivery = True

bobs_burger = Restaurant()
bobs_burger.name = "Bob´s Burgers"
bobs_burger.description = "American Diner"
bobs_burger.rating = 4.2
bobs_burger.delivery = False

print (vars(bobs_burger))

rositas = Restaurant()
rositas.name = "Rositas Mex"
rositas.description = "Mexican Food"
rositas.rating = 4.9
rositas.delivery = True

print (vars(rositas))

chef_diego = Restaurant()
chef_diego.name = "Chef Diego"
chef_diego.description = "Spanish Food"
chef_diego.rating = 5.0
chef_diego.delivery = False

print (vars(chef_diego))

