import streamlit as st
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw

st.title("Color Segmentation using Clustering")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"],
)

k = st.slider("Select Number of Colors", min_value=3, max_value=10, value=3)


def create_color_palette(dominant_colors, palette_size=(300, 50)):
    palette = Image.new("RGB", palette_size)
    draw = ImageDraw.Draw(palette)

    swatch_width = palette_size[0] // len(dominant_colors)

    for i, color in enumerate(dominant_colors):
        rgb = tuple(int(c) for c in color)

        draw.rectangle(
            [i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]],
            fill=rgb,
        )

    return palette


@st.cache_data
def perform_clustering(image_array, k):
    X = image_array.reshape(-1, 3)
    kmeans = KMeans(n_clusters=k, n_init=10, init="k-means++", random_state=42)
    kmeans.fit(X)
    return kmeans.cluster_centers_, kmeans.labels_


if uploaded_file is not None:
    original_image = Image.open(uploaded_file).convert("RGB")
    resized_image = original_image.copy()
    resized_image.thumbnail((300, 300))

    st.subheader("Original Image")
    st.image(original_image, width="stretch")

    image_np = np.array(resized_image)

    dominant_colors, labels = perform_clustering(image_np, k)

    counts = np.bincount(labels)

    sorted_indices = np.argsort(-counts)

    sorted_colors = dominant_colors[sorted_indices]
    sorted_counts = counts[sorted_indices]

    st.subheader("Dominant Color Palette")

    palette = create_color_palette(sorted_colors)
    st.image(palette, width="stretch")

    total_pixels = sum(sorted_counts)

    for i, (color, count) in enumerate(zip(sorted_colors, sorted_counts)):
        percentage = count / total_pixels
        rgb = tuple(int(c) for c in color)
        st.write(f"Color {i+1}: RGB {rgb} -> {percentage:.2%}")
