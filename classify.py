import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def buyer_classification(incomelevel, age, location, property_price, property_size, property_type, no_of_bedrooms,
                         property_amenities, property_condition, buying_history, market_trends, interest_rates):
    try:
        # Load dataset
        data = pd.read_csv("types_dataset.csv")  # Replace "types_dataset.csv" with the actual dataset filename
        df = pd.DataFrame(data)

        # Define features and target variable
        x = df.drop(columns=['Type of Buyer'])
        y = df['Type of Buyer']

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

        # One-hot encode categorical variables
        X_train_encoded = pd.get_dummies(X_train)
        X_test_encoded = pd.get_dummies(X_test)
        X_test_encoded = X_test_encoded.reindex(columns=X_train_encoded.columns, fill_value=0)

        # Train decision tree classifier
        decision_tree = DecisionTreeClassifier()
        decision_tree.fit(X_train_encoded, y_train)

        # Create new data for prediction
        new_data = pd.DataFrame({
            'Incomelevel': [incomelevel],
            'Age': [age],
            'Location': [location],
            'Property Price': [property_price],
            'Property Size': [property_size],
            'Property Type': [property_type],
            'No of BR': [no_of_bedrooms],
            'Property Amenities': [property_amenities],
            'Property Condition': [property_condition],
            'Buying History': [buying_history],
            'Market Trends': [market_trends],
            'Interest Rates': [interest_rates]
        })

        # One-hot encode new data and align with training data columns
        new_data_encoded = pd.get_dummies(new_data)
        new_data_encoded = new_data_encoded.reindex(columns=X_train_encoded.columns, fill_value=0)

        # Make predictions on new data
        prediction = decision_tree.predict(new_data_encoded)
        
        return prediction

    except Exception as e:
        print("An error occurred:", str(e))
        return None
