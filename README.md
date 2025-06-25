# GextonPython-Intern_Task05
Build a real-time currency converter using Python, API, and a simple graphical user interface (GUI).

💱 Real-Time Currency Converter (Streamlit)

This is a **Python + Streamlit** project that converts currencies in real time using a free exchange rates API.

---

## 🎯 Features
- **User-friendly GUI** built with Streamlit:
  - Input box for amount
  - Drop-downs for `From Currency` and `To Currency`
  - `Convert` and `Clear` buttons
- Fetches **live exchange rates** from the `https://api.exchangerate-api.com` API
- Converts amounts in real-time
- Displays **error messages** for invalid inputs or failed API calls
- Logs all conversions to a file (`conversion_log.txt`) with **date & time**
- Conversion history can be viewed in the app
- Added simple **hover effects** for better UI experience

---

## 🧰 Requirements
- Python 3.x
- Streamlit
- Requests

Install dependencies using:
```bash
pip install streamlit requests
