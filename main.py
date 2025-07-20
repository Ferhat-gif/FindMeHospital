from flask import Flask, render_template, request, session, redirect, url_for
import os
import csv

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session

CSV_FILE = "data/patient_records.csv"

# CSV başlıkları
fieldnames = [
    "First Name", "Last Name", "Age", "Gender", "Email", "Phone",
    "Weight (kg)", "Height (cm)", "Location", "Has Insurance", "Insurance Type",
    "Complaint", "Symptoms", "Symptom Duration"
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form.to_dict(flat=False)

        symptoms_combined = ", ".join(data.get("symptoms", []))

        record = {
            "First Name": data["name"][0],
            "Last Name": data["surname"][0],
            "Age": data["age"][0],
            "Gender": data["gender"][0],
            "Email": data["email"][0],
            "Phone": data["phone"][0],
            "Weight (kg)": data["weight"][0],
            "Height (cm)": data["height"][0],
            "Location": data["location"][0],
            "Has Insurance": data.get("hasInsurance", [""])[0],
            "Insurance Type": data.get("insuranceType", [""])[0],
            "Complaint": data["complaint"][0],
            "Symptoms": symptoms_combined,
            "Symptom Duration": data["symptom_duration"][0]
        }

        os.makedirs("data", exist_ok=True)
        file_missing = not os.path.isfile(CSV_FILE)

        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if file_missing:
                writer.writeheader()
            writer.writerow(record)

        # Store the user's complaint and symptoms in the session
        session['complaint'] = data["complaint"][0]
        session['symptoms'] = symptoms_combined
        return render_template("formConfirmationMessage.html", message="Information has been successfully saved.")
    else:
        return render_template("form2.html")
from hospital_data import find_hospitals_for_disease

@app.route("/hospitals")
def hospitals():
    complaint = session.get('complaint', '')
    symptoms = session.get('symptoms', '')
    # Combine complaint and symptoms for matching
    search_text = complaint + ", " + symptoms if symptoms else complaint
    hospitals = find_hospitals_for_disease(search_text)
    return render_template("hospitals.html", hospitals=hospitals)


if __name__ == "__main__":
    app.run(debug=True)
