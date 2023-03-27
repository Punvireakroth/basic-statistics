from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
            gender = request.form['gender']
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            bmi = round((weight / (height ** 2)),2)

            if gender == 'male':
                if bmi < 20.7:
                    result = 'Underweight'
                elif bmi >= 20.7 and bmi < 26.4:
                    result = 'Normal'
                elif bmi >= 26.4 and bmi < 27.8:
                    result = 'Overweight'
                else:
                    result = 'Obese'
            else:
                if bmi < 19.1:
                    result = 'Underweight'
                elif bmi >= 19.1 and bmi < 25.8:
                    result = 'Normal'
                elif bmi >= 25.8 and bmi < 27.3:
                    result = 'Overweight'     
                else:
                    result = 'Obese'
            return render_template('result.html', bmi=bmi, result=result)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=8080)
