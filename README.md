# Medical Predicator

## Create venv

```bash
python -m venv venv
```

## Activate it

**macOS / Linux:**

```bash
source .venv/bin/activate
```

## Install the libraries

```bash
pip install pandas numpy scikit-learn gradio
```

## Save them to `requirements.txt`

After installing everything:

```bash
pip freeze > requirements.txt
```

## Later, recreate the same setup anywhere

```bash
python -m venv venv
source venv/bin/activate  # or Windows activate
pip install -r requirements.txt
```

Love this part — from zero → GitHub in one clean flow 🚀
Here’s the **full command sequence** you’ll use in a new project folder.

---

## Initialize git

```bash
git init
```

## Create .gitignore file

```bash
nxp gitignore python
```

## Stage your files

```bash
git add .
```

Adds everything in the project to the staging area.

## Make your first commit

```bash
git commit -m "Initial commit"
```

---

## Rename default branch to main (modern standard)

```bash
git branch -M main
```

## Connect local repo to GitHub

```bash
git remote add origin https://github.com/yourusername/your-repo-name.git
```

Check it:

```bash
git remote -v
```

---

## Push to GitHub

```bash
git push -u origin main
```

The `-u` sets upstream so next time you can just run `git push`.

---

## ✅ After this, your normal workflow is

```bash
git add .
git commit -m "Describe your changes"
git push
```

---

## 🆘 First-time Git setup (if needed)

If Git asks who you are:

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```
