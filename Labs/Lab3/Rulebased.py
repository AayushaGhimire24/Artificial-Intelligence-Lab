# Define the facts about the animal
animal_facts = {
    "feathers": False,
    "flies": False,
    "fur": True,
    "barks": True,
    "scales": False,
    "swims": False
}

# Define the rules
def check_bird(facts):
    if facts["feathers"] and facts["flies"]:
        return "The animal is a bird."
    return None

def check_dog(facts):
    if facts["fur"] and facts["barks"]:
        return "The animal is a dog."
    return None

def check_fish(facts):
    if facts["scales"] and facts["swims"]:
        return "The animal is a fish."
    return None

# List of rules
rules = [check_bird, check_dog, check_fish]

# Apply the rules to the facts
def classify_animal(facts, rules):
    classification = []
    for rule in rules:
        result = rule(facts)
        if result:
            classification.append(result)
    return classification

# Get the classification
classification = classify_animal(animal_facts, rules)

# Print the classification
for c in classification:
    print(c)