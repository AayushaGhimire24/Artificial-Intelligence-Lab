import pandas as pd
from collections import Counter

# Data from the table
data = {
    'age': ['youth', 'youth', 'middle_aged', 'senior', 'senior', 'senior', 'middle_aged', 'youth', 'youth', 'senior', 'youth', 'middle_aged', 'middle_aged', 'senior'],
    'income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'medium', 'high', 'medium'],
    'student': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'no'],
    'credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'excellent'],
    'buys_computer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Function to calculate the probability
def calculate_probability(df, feature, value, target, target_value):
    sub_df = df[df[target] == target_value]
    count_value = len(sub_df[sub_df[feature] == value])
    count_target = len(sub_df)
    probability = count_value / count_target
    return probability

# Prior probabilities
P_yes = len(df[df['buys_computer'] == 'yes']) / len(df)
P_no = len(df[df['buys_computer'] == 'no']) / len(df)

# Likelihoods
P_age_youth_given_yes = calculate_probability(df, 'age', 'youth', 'buys_computer', 'yes')
P_income_medium_given_yes = calculate_probability(df, 'income', 'medium', 'buys_computer', 'yes')
P_student_yes_given_yes = calculate_probability(df, 'student', 'yes', 'buys_computer', 'yes')
P_credit_rating_fair_given_yes = calculate_probability(df, 'credit_rating', 'fair', 'buys_computer', 'yes')

P_age_youth_given_no = calculate_probability(df, 'age', 'youth', 'buys_computer', 'no')
P_income_medium_given_no = calculate_probability(df, 'income', 'medium', 'buys_computer', 'no')
P_student_yes_given_no = calculate_probability(df, 'student', 'yes', 'buys_computer', 'no')
P_credit_rating_fair_given_no = calculate_probability(df, 'credit_rating', 'fair', 'buys_computer', 'no')

# Posterior probabilities
P_yes_given_X = P_yes * P_age_youth_given_yes * P_income_medium_given_yes * P_student_yes_given_yes * P_credit_rating_fair_given_yes
P_no_given_X = P_no * P_age_youth_given_no * P_income_medium_given_no * P_student_yes_given_no * P_credit_rating_fair_given_no

# Normalize
P_sum = P_yes_given_X + P_no_given_X
P_yes_given_X_normalized = P_yes_given_X / P_sum
P_no_given_X_normalized = P_no_given_X / P_sum

# Prediction
if P_yes_given_X_normalized > P_no_given_X_normalized:
    prediction = 'yes'
else:
    prediction = 'no'

print(f"The predicted class for X is: {prediction}")