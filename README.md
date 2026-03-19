# Two-Sample-T-Test
A Flask web application for performing two-sample independent t-tests with a clean UI.
Files
FilePurposeapp.pyFlask backend with the two_sample() functionindex.htmlFrontend UIrequirements.txtPython dependenciesProcfileProcess file for deployment

Step-by-Step Deployment (GitHub → Replit)
Step 1: Create a GitHub Repository

Go to github.com → click New repository
Name it e.g. ttest-app, set to Public
Click Create repository

Step 2: Push Your Files to GitHub
In your terminal:
bashgit init
git add app.py index.html requirements.txt Procfile
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ttest-app.git
git push -u origin main
Step 3: Import into Replit

Go to replit.com → click + Create Repl
Choose Import from GitHub
Paste your GitHub repo URL and click Import
Replit will detect it as a Python project

Step 4: Configure Replit Run Command
In Replit, open the Shell and run:
bashpip install -r requirements.txt
Then set the Run command in .replit config or the Run button to:
gunicorn app:app --bind 0.0.0.0:8080
Or simply:
python app.py
Step 5: Deploy / Go Live

Click the green Run button
Replit will give you a public URL like: https://ttest-app.yourname.repl.co
Share that URL — your app is live!


Local Development
bashpip install -r requirements.txt
python app.py
# Open http://localhost:5000
API Usage
POST /compute
json{
  "sample_a": "12.5, 14.2, 13.8, 15.1, 11.9",
  "sample_b": "10.3, 11.7, 12.0, 9.8, 13.2",
  "alternative": "two-sided"
}
alternative options: two-sided, left, right
