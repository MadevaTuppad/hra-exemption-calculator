from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate_hra_exemption', methods=['POST'])
def calculate_hra_exemption():
    try:
        salary = float(request.form['salary'])
        rent = float(request.form['rent'])
        hra_received = float(request.form['hra'])
        da = float(request.form['da'])  # Read DA from the form
        city = request.form['city']

        # Step 1: Determine the Actual Monthly HRA Received
        actual_hra_received = hra_received
        explanation = "Step 1:Actual Monthly HRA Received:\n\nIn this case, it is Rs. " + str(actual_hra_received) + ".\n\n"

        # Step 2: Calculate the HRA Exemption for Metro and Non-Metro Cities
        if city in ["New Delhi", "Chennai", "Kolkata", "Mumbai"]:
            hra_exemption = 0.5 * (salary + da)
            explanation += "Step 2:HRA Exemption for Metropolitan Cities:\nFor metropolitan cities, the HRA exemption is computed as 50% of the sum of the monthly basic salary and monthly dearness allowance.\n\n50% of (" + str(salary) + " + " + str(da) + ") = Rs. " + str(hra_exemption) + ".\n\n"
        else:
            hra_exemption = 0.4 * (salary + da)
            explanation += "Step 2:HRA Exemption for Non-Metro Cities:\nFor non-metro cities, the HRA exemption is computed as 40% of the sum of the monthly basic salary and monthly dearness allowance.\n\n40% of (" + str(salary) + " + " + str(da) + ") = Rs. " + str(hra_exemption) + ".\n\n"

        # Step 3: Determine the Actual Rent Paid minus 10% of Salary
        rent_minus_10_percent = rent - (0.1 * (salary + da))
        explanation += "Step 3: Actual Rent Paid minus 10% of Basic Salary +DA:\n\nRs. " + str(rent) + " - [10% of (" + str(salary) + " + " + str(da) + ")] = Rs. " + str(rent_minus_10_percent) + ".\n\n"

        # Step 4: Identify the Minimum of the Above Three Calculations
        hra_exempt = min(actual_hra_received, hra_exemption, rent_minus_10_percent)
        hra_exempt = max(hra_exempt, 0)
        explanation += "Step 4: Identify the Minimum of the Above Three Calculations:\n\nIn this case, it is " + str(hra_exempt) + "\n\n"

        response = {
            'hra_exempt': hra_exempt,
            'explanation': explanation
        }

        return jsonify(response)
    except ValueError:
        return jsonify({'error': 'Invalid input! Please enter numeric values.'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
