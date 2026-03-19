# Two-Sample T-Test Web App

A Flask web application for performing two-sample independent t-tests with a clean UI.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Flask backend with the `two_sample()` function |
| `index.html` | Frontend UI |
| `requirements.txt` | Python dependencies |
| `Procfile` | Process file for deployment |

---

## Step-by-Step Deployment (GitHub → Replit)

### Step 1: Create a GitHub Repository

1. Go to [github.com](https://github.com) → click **New repository**
2. Name it e.g. `ttest-app`, set to **Public**
3. Click **Create repository**

### Step 2: Push Your Files to GitHub

In your terminal:

```bash
git init
git add app.py index.html requirements.txt Procfile
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ttest-app.git
git push -u origin main
```

### Step 3: Import into Replit

1. Go to [replit.com](https://replit.com) → click **+ Create Repl**
2. Choose **Import from GitHub**
3. Paste your GitHub repo URL and click **Import**
4. Replit will detect it as a Python project

### Step 4: Configure Replit Run Command

In Replit, open the **Shell** and run:

```bash
pip install -r requirements.txt
```

Then set the **Run** command in `.replit` config or the Run button to:

```
gunicorn app:app --bind 0.0.0.0:8080
```

Or simply:
```
python app.py
```

### Step 5: Deploy / Go Live

1. Click the green **Run** button
2. Replit will give you a public URL like: `https://ttest-app.yourname.repl.co`
3. Share that URL — your app is live!

---

## Local Development

```bash
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```

## API Usage

**POST** `/compute`

```json
{
  "sample_a": "12.5, 14.2, 13.8, 15.1, 11.9",
  "sample_b": "10.3, 11.7, 12.0, 9.8, 13.2",
  "alternative": "two-sided"
}
```

`alternative` options: `two-sided`, `left`, `right`
