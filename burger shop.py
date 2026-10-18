def make_burger(
    bun="Sesame",
    patty="Veggie",
    cheese="Cheddar",
    sauce="Ketchup",
    toppings="Lettuce & Tomato",
):
    """Assembles a burger using default ingredients unless told otherwise."""
    print("\n--- Flipping the Burger! ---")
    print(f"🍞 Bun:      {bun}")
    print(f"🥩 Patty:    {patty}")
    print(f"🧀 Cheese:   {cheese}")
    print(f"🥫 Sauce:    {sauce}")
    print(f"🥗 Toppings: {toppings}")
    print("🍔 Your order is ready! Enjoy your meal.\n")


# 1. The "Regular" Order (Uses every single default argument)
print("Customer 1: 'Give me the house regular!'")
make_burger()

# 2. Swapping just one thing (Order with Spicy Mayo instead of Ketchup)
print("Customer 2: 'Make it spicy, please!'")
make_burger(sauce="Spicy Mayo")

# 3. Customizing bun and patty, leaving the rest default
print("Customer 3: 'Brioche bun with double paneer, keep standard toppings.'")
make_burger(bun="Brioche", patty="Double Paneer")

# 4. Total custom burger (Overriding every default)
print("Customer 4: 'Total monster build!'")
make_burger(
    bun="Garlic Bread",
    patty="Crispy Mushroom",
    cheese="Mozzarella",
    sauce="Chipotle BBQ",
    toppings="Caramelized Onions & Jalapeños",
)
