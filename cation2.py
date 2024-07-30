from flask import Flask, render_template, request

from classify import buyer_classification

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('types_buyers.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        incomelevel=request.form['incomeLevel']
        age = int(request.form['age'])
        location = request.form['location']
        property_price = request.form['price']
        property_size = request.form['size']
        property_type = request.form['type']
        no_of_bedrooms = int(request.form['numberOfBedrooms'])
        property_amenities = request.form['amenities']
        property_condition = request.form['propertyCondition']
        buying_history = request.form['buyingHistory']
        market_trends = request.form['marketTrends']
        interest_rates = request.form['interestRates']

        # Call the buyer_classification function
        predicted_buyer = buyer_classification(incomelevel,age, location, property_price, property_size, property_type, no_of_bedrooms,
                         property_amenities, property_condition, buying_history, market_trends, interest_rates)

        #return render_template('types_buyers.html', predicted_buyer=predicted_buyer)
        return render_template("types_buyers.html",predicted_buyer=predicted_buyer)

if __name__ == '__main__':
    app.run(debug=True)
