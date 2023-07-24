from flask import Flask, render_template, request

app = Flask(__name__)


global GLOBALS

GLOBALS = {
    'name': '',
    'age': '',
    'major': '',
    'credits': 0,
    'gpa': 0.0,
    'target_gpa': 0.0,
}


@app.get('/')
def index():
    return render_template('index.html')


# We use POST to send our previous data and GET to get the data from the form
@app.route('/task1', methods=['POST', 'GET'])

#in each render, we check if the method is 'GET' or 'POST'. if it is 'POST' it means the user has submitted
# some data in the previous step so we retrieve this data from accessing the "GLOBALS" dictionary that we are
# updating after every entry. if it is "GET", it means that the page has been reloaded and we need to start
# over, so we give everything default values. source: 'https://pythonprogramming.net/flask-get-post-requests-handling-tutorial/' 

def task1():
    
    if request.method == 'POST':
    # Get the data from the form
        name = request.form['name']
        age = request.form['age']

    # TODO 1: Update the `age` variable and assign the value of the age field from the form to it

        GLOBALS['age'] = age

    # TODO 2: Update the `GLOBALS` dictionary with the new values

        GLOBALS['name'] = name

    # Returns the data to the template
        return render_template('task1.html', name=name, age=age)
    else:
        return render_template('task1.html', name='', age='')


@app.route('/task2', methods=['POST', 'GET'])
def task2():
    # TODO 3: Get the user's major, credits, and gpa from the form

    if request.method == 'POST':
        major = request.form['major']
        credits = int(request.form['credits'])
        gpa = float(request.form['gpa'])

    # TODO 4: Update the `GLOBALS` dictionary with the new values

        GLOBALS['major'] = major
        GLOBALS['credits'] = credits
        GLOBALS['gpa'] = gpa

    # TODO 5: Return the data to the template
        return render_template('task2.html', name=GLOBALS['name'], age=GLOBALS['age'], major=major, credits=credits, gpa=gpa)
    else:
        return render_template('task2.html', name='', age='', major='', credits=0, gpa=0.0)


@app.route('/task3', methods=['POST', 'GET'])
def task3():
    # TODO 6: Retreive the target_gpa from the form, and update the `GLOBALS` dictionary

    if request.method == 'POST':

        target_gpa = float(request.form['target_gpa'])
        GLOBALS['target_gpa'] = target_gpa

    # TODO 7: Use the `credits_to_target` function to calculate the number of credits needed to reach the target GPA

        credits_needed = credits_to_target(GLOBALS['gpa'], target_gpa, GLOBALS['credits'])

    # TODO 8: Return the data to the template
        return render_template('task3.html', name=GLOBALS['name'], age=GLOBALS['age'], major=GLOBALS['major'], credits=GLOBALS['credits'], gpa=GLOBALS['gpa'], target_gpa=target_gpa, credits_needed=credits_needed)
    else:
        return render_template('task3.html', name='', age='', major='', credits=0, gpa=0.0, target_gpa='', credits_needed='')


def credits_to_target(current_gpa: float, target_gpa: float, current_credits: int) -> int:
    """
    Calculates the number of credits needed to reach a target GPA

    args:
        - current_gpa: The student's current GPA
        - target_gpa: The student's target GPA
        - current_credits: The student's current number of credits

    returns:
        - The number of credits needed to reach the target GPA
    """
    quality_points_needed = (target_gpa * current_credits) - \
        (current_gpa * current_credits)
    credits_needed = quality_points_needed / 4

    return credits_needed


if __name__ == '__main__':
    app.run(debug=True)
