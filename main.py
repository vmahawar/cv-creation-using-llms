"""
main.py
---------
Capstone Project: Automatic CV Creation using LLMs
Submitted by: Vijay Mahawar
Submitted to: IIT Kharagpur (TCS iON HAAI++ Capstone Project)

This is the main entry point for running the CV Creation app.
It checks if Streamlit is installed and launches the local UI defined in `streamlit_cv_llm_demo.py`.
"""

import os
import sys
import subprocess

APP_FILE = "streamlit_cv_llm_demo.py"

def run_streamlit_app():
    """Launch Streamlit app if Streamlit is installed."""
    try:
        import streamlit
        print("✅ Streamlit detected. Launching app...")
        subprocess.run(["streamlit", "run", APP_FILE])
    except ModuleNotFoundError:
        print("⚠️ Streamlit not found.")
        print("To install dependencies, run:")
        print("   pip install streamlit pdfplumber python-docx requests")
        print("\nThen start the app with:")
        print(f"   python {APP_FILE} --serve")

def run_tests():
    """Run built-in tests for the app."""
    print("🧪 Running internal unit tests...")
    subprocess.run([sys.executable, APP_FILE, "--run-tests"])

def main():
    print("🚀 Automatic CV Creation using LLMs — Local Setup (Ollama)")
    print("----------------------------------------------------------")
    print("1. Run Streamlit UI")
    print("2. Run internal tests")
    print("3. Exit")
    choice = input("\nSelect an option (1/2/3): ").strip()

    if choice == "1":
        run_streamlit_app()
    elif choice == "2":
        run_tests()
    else:
        print("👋 Exiting. Have a great day!")

if __name__ == "__main__":
    main()
