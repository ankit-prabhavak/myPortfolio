from flask import Flask, render_template, request
from database import create_db, save_message  # Import the functions to interact with the database

app = Flask(__name__)

# Initialize the database (create table if it doesn't exist)
create_db()

# Route to render the index page (which contains the contact form)
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission from the contact form
@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Save the message to the database
        save_message(name, email, message)

        # After saving the message, show a thank you message
        return 'Success', 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
