# GRE Sentence Equivalence Trainer

A simple tool to help memorize those annoying GRE word pairs.

## Setup

1.  **Prepare Data**: Put your word pairs in `gre_data.txt` (see `gre_data_example.txt`).
2.  **Process**: Run the script to generate data files:
    ```bash
    python preprocess.py
    ```
    *Creates: `gre_pair.js` and `gre_translation.js`*

## How to Run

### Option 1: Direct
Just open **`app.html`** in your browser.

### Option 2: Local Network (for Mobile)
To access the trainer from other devices on your Wi-Fi:

1.  Open your terminal in the project folder.
2.  Start a server:
    ```bash
    python -m http.server 8000
    ```
3.  Find your IP address (via `ipconfig`).
4.  On your phone/tablet, go to: `http://[YOUR-IP]:8000/app.html`