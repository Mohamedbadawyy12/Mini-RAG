

# 📝 mini-rag

Minimal implementation of the **RAG model** for Question Answering.

---

## 📦 Requirements
- **Python 3.8** or later

### 🔹 Install Python using MiniConda
1. Download and install **MiniConda** from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)  
2. Create a new environment:
   ```bash
   conda create -n mini-rag python=3.8
````

3. Activate the environment:

   ```bash
   conda activate mini-rag
   ```

---

## 🎨 (Optional) Setup your CLI for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

---

## ⚙️ Installation

### 1. Install required packages

```bash
pip install -r requirements.txt
```

### 2. Setup environment variables

```bash
cp .env.example .env
```

👉 Update the `.env` file with your values (e.g., `OPENAI_API_KEY`).

---

## 🚀 Run the FastAPI Server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

### 🐳 Docker setup

```bash
cd docker
cp .env.example .env
```

👉 Update `.env` with your credentials.

---

```

تحب أعملهولك ملف **README.md** جاهز للتحميل دلوقتي ولا هتنسخه وتحطه بنفسك؟
```
