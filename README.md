# Color Segmentation App using K-Means Clustering

An interactive Streamlit web application that extracts dominant colors from an image using **unsupervised learning (K-Means clustering)**.

The app analyzes pixel distributions, clusters similar colors, and displays the dominant color palette sorted by percentage contribution.

---

## Live Demo

Check out the live application here: (https://color-segmentation-fzdnoryj4zp6wc99geykqo.streamlit.app/)

---

## Features

- Upload JPG / PNG images
- Extract dominant colors using K-Means clustering
- Sort colors by dominance percentage
- Display RGB values and percentage contribution
- Optimized performance using image resizing
- Cached clustering using `@st.cache_data`

---

## How It Works

1. The uploaded image is converted to RGB format.
2. A resized copy is used for faster clustering.
3. Pixel values are reshaped into a 2D feature matrix.
4. K-Means clustering groups pixels into `k` clusters.
5. Clusters are sorted based on pixel frequency.
6. The dominant color palette is generated and displayed.

---

## Tech Stack

- Python
- Streamlit
- NumPy
- Scikit-learn
- Pillow

---

## Project Structure

```
color-segmentation/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Run Locally

Clone the repository:

```bash
git clone https://github.com/your-username/color-segmentation.git
cd color-segmentation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## Key Concepts Applied

- Unsupervised Learning
- K-Means Clustering
- Feature Engineering (Pixel Reshaping)
- Cluster Dominance Analysis
- Performance Optimization with Caching
- Interactive ML Application Development

---

## Author

Shubham Redkar
