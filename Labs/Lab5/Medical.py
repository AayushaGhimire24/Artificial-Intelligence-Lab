class Disease:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms

class MedicalExpertSystem:
    def __init__(self):
        self.diseases = []

    def add_disease(self, name, symptoms):
        disease = Disease(name, symptoms)
        self.diseases.append(disease)

    def diagnose(self, input_symptoms):
        matched_diseases = []
        for disease in self.diseases:
            if set(disease.symptoms).issubset(input_symptoms):
                matched_diseases.append(disease)
        
        if len(matched_diseases) == 0:
            print("No matching disease found.")
        else:
            print("Possible diseases:")
            for disease in matched_diseases:
                print("- ", disease.name)

# Create a medical expert system
expert_system = MedicalExpertSystem()

# Add diseases and their symptoms
expert_system.add_disease("Common Cold", ["sore throat", "runny nose", "cough"])
expert_system.add_disease("Flu", ["fever", "headache", "muscle pain"])
expert_system.add_disease("Allergies", ["sneezing", "itchy eyes", "rash"])

# Get user input for symptoms
user_input = input("Enter the symptoms (comma-separated): ")
input_symptoms = [symptom.strip() for symptom in user_input.split(",")]

# Diagnose the disease based on symptoms
expert_system.diagnose(input_symptoms)