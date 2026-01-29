HeartLens ❤️

Multi-Source Cardiovascular Risk Tool

HeartLens is a web-based tool built with Streamlit that helps users quickly assess their cardiovascular risk using lifestyle, clinical, and ECG factors. The app is designed to be simple, visually appealing, and interactive, making heart health insights accessible to everyone.

📝 Features

Multi-source risk calculation: Combines lifestyle, clinical, and ECG data.

Interactive inputs: Users can enter age, blood pressure, cholesterol, activity level, chest pain type, and max heart rate.

Clear results: Risk summary displayed in easy-to-read cards with color-coded indicators.

Modern UI: Purple-themed background with white text, styled inputs, and buttons.

⚡ Demo

You can see the live app here (if deployed to Streamlit Cloud):
HeartLens on Streamlit
 (replace # with your Streamlit app link)

📂 Folder Structure
HeartLensApp/
│
├─ app.py         # Main Streamlit app
├─ predict.py     # Risk calculation logic
├─ style.css      # Styling for the app (purple + white theme)
└─ data/          # Optional: JSON or data files if needed

💻 Installation

Clone the repository:

git clone https://github.com/yourusername/HeartLens.git
cd HeartLens


Create a virtual environment (recommended):

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install required packages:

pip install -r requirements.txt


(Example requirements.txt content: streamlit + any other libraries used in predict.py)

🚀 Run the App Locally
streamlit run app.py


The app will open in your browser at http://localhost:8501.

Enter your details and click Analyze Heart Risk to see your risk summary.

🎨 Custom Styling

Background: Light/mid purple

Text: White, large, readable

Cards & Inputs: Styled for modern look

Buttons: Dark purple with white text

All styling is included in style.css and loaded automatically in app.py.

📖 How It Works

Lifestyle Risk – Age, activity level, blood pressure, cholesterol.

Clinical Risk – Chest pain type, max heart rate.

ECG Risk – Age and blood pressure-related ECG risk.

Summary – Each risk is displayed in a color-coded card for clarity.

All calculations are handled in predict.py, keeping the app logic separate from UI styling.

🛠 Tech Stack

Python 3.x

Streamlit

HTML/CSS for styling

Optional: JSON for input data

📌 Future Improvements

Add multi-page workflow (home → login → input → results)

Export risk summary as PDF or email

Include more clinical parameters for accuracy

Add charts to visualize trends over time

📄 License

MIT License – feel free to use and modify for personal or educational projects.
