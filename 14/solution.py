def main(recipe, available_ingredients):
    # Calculate the ratio for each ingredient in the recipe
    ratios = []
    for ingredient, amount in recipe.items():
        if ingredient in available_ingredients:
            ratios.append(available_ingredients[ingredient] // amount)
        else:
            return 0  # Ingredient not present, so can't bake even one cake.
    return min(ratios)  # Return the smallest ratio, which indicates max number of cakes.

