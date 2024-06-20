from countCoins import find_coins

def process_image(st, img):
    # Check if picture is passed
    if img:
        # find total coins and return labeled image
        coins, labeled_image = find_coins(img)
        # Creating 1 row by 2 column container to display picture side by side
        col1, col2 = st.columns(2)
        # Original Image
        with col1:
            st.image(img, caption="Original Image", use_column_width=True)
        # Counted Image
        with col2:
            st.image(labeled_image, caption="Detected Coins Image", use_column_width=True)
        
        st.write(f"Total coins found from image: {coins}")
            