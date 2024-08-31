
import random

class Environment(object):
    def __init__(self):
        # Initialize location and condition
        # 0 means clean, 1 means dirty
        self.locationcondition = {'A': '1', 'B': '1'}
        # Randomize condition in location A and B
        self.locationcondition['A'] = random.randint(0, 1)
        self.locationcondition['B'] = random.randint(0, 1)
class SRagent(Environment):
    def __init__(self, environment):
        print(environment.locationcondition)
        # Place vacuum cleaner at random location
        vacuumlocation = random.randint(0, 1)
        # If vacuum is at location A
        if vacuumlocation == 0:
            print("Vacuum is randomly located at location A.")
            # If location A is dirty
            if environment.locationcondition['A'] == 1:
                print("Location A is dirty")
                # Suck the dirt and mark it clean
                environment.locationcondition['A'] = 0
                print("Location A has been cleaned")
                # If B is dirty
                if environment.locationcondition['B'] == 1:
                    print("Location B is dirty")
                    # Suck the dirt and mark it clean
                    environment.locationcondition['B'] = 0
                    print("Location B has been cleaned")
            else:
                # Move to B
                print("Moving to location B")
                # If B is dirty
                if environment.locationcondition['B'] == 1:
                    print("Location B is dirty")
                    # Suck the dirt and mark it clean
                    environment.locationcondition['B'] = 0
                    print("Location B has been cleaned")
        # If vacuum is at location B
        elif vacuumlocation == 1:
            print("Vacuum is randomly located at location B.")
            # If location B is dirty
            if environment.locationcondition['B'] == 1:
                print("Location B is dirty")
                # Suck the dirt and mark it clean
                environment.locationcondition['B'] = 0
                print("Location B has been cleaned")
                # If A is dirty
                if environment.locationcondition['A'] == 1:
                    print("Location A is dirty")
                    # Suck the dirt and mark it clean
                    environment.locationcondition['A'] = 0
                    print("Location A has been cleaned")
            else:
                # Move to A
                print("Moving to location A")
                # If A is dirty
                if environment.locationcondition['A'] == 1:
                    print("Location A is dirty")
                    # Suck the dirt and mark it clean
                    environment.locationcondition['A'] = 0
                    print("Location A has been cleaned")
        # Done cleaning
        print("Final location conditions:", environment.locationcondition)

theenvironment = Environment()
thevacuum = SRagent(theenvironment)
