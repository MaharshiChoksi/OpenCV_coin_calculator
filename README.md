# COIN COUNTER OPENCV BASED PROJECT

<hr/>

### Steps involved in program

* User Captures or uploads picture of the coins
* Convert picture to grayscale (black & white)
* Mark down coins
* Mark counted coins as green
* Show total coins on the top of the left corner

> NOTE: This this program only counts total coins not its value

1. Init program
2. Ask for picture (via camera or photo)
3. Convert to opencv format
4. Convert to Grayscale
5. apply otsu threshhold
6. find coin like shape
7. Draw the outline to each shape
8. Label the coins using watershed
9. Add it to total counter
10. Capture the calculated labeled picture and return it along with counted coins
11. Dispaly the original and labeled image side by size and Exit program

> In this program I have used watershed OpenCV algorithm