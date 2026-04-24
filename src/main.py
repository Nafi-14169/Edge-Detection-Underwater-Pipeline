import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('images/sample.jpg')
img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)

sobelx=cv2.Sobel(blur,cv2.CV_64F,1,0,ksize=3)
sobely=cv2.Sobel(blur,cv2.CV_64F,0,1,ksize=3)
sobelx=np.absolute(sobelx)
sobely=np.absolute(sobely)
sobel_combined=cv2.magnitude(sobelx,sobely)
sobel_combined=cv2.normalize(sobel_combined,None,0,255,cv2.NORM_MINMAX)
sobel_combined=sobel_combined.astype('uint8')

scharrx=cv2.Scharr(blur,cv2.CV_64F,1,0)
scharry=cv2.Scharr(blur,cv2.CV_64F,0,1)
scharrx=abs(scharrx)
scharry=abs(scharry)
scharr_combined=cv2.magnitude(scharrx,scharry)
scharr_combined=cv2.normalize(scharr_combined,None,0,255,cv2.NORM_MINMAX)
scharr_combined=scharr_combined.astype('uint8')


lap=cv2.Laplacian(blur,cv2.CV_64F)
lap=abs(lap)
lap=cv2.normalize(lap,None,0,255,cv2.NORM_MINMAX)
lap=lap.astype('uint8')

edges=cv2.Canny(blur,100,200)
# edges1=cv2.Canny(blur,50,150)
# edges2=cv2.Canny(blur,10,100)
# edges3=cv2.Canny(blur,100,200)


plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.imshow(img_rgb)
plt.title("Sample pic")
plt.axis("off")

# plt.subplot(2,3,2)
# plt.imshow(blur,cmap='gray')
# plt.title("Blurred")
# plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(edges,cmap='gray')
plt.title('Canny')
plt.axis('off')

# plt.subplot(2,3,4)
# plt.imshow(sobelx,cmap='gray')
# plt.title("Sobel X")
# plt.axis('off')

# plt.subplot(2,3,5)
# plt.imshow(sobely,cmap='gray')
# plt.title("Sobel Y")
# plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(sobel_combined,cmap='gray')
plt.title("Sobel")
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(scharr_combined,cmap='gray')
plt.title('Scharr')
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(lap,cmap='gray')
plt.title("Laplacian")
plt.axis('off')

# plt.subplot(2,3,4)
# plt.imshow(edges1,cmap='gray')
# plt.title("Canny Edges 50-150")
# plt.axis('off')

# plt.subplot(2,3,5)
# plt.imshow(edges2,cmap='gray')
# plt.title("Canny Edges 10-100")
# plt.axis('off')

# plt.subplot(2,3,6)
# plt.imshow(edges3,cmap='gray')
# plt.title("Canny Edges 100-200")
# plt.axis('off')

# plt.figure(figsize=(12,8))

# plt.subplot(2,3,1)
# plt.imshow(img_rgb)
# plt.title("Sample pic")
# plt.axis('off')

# plt.subplot(2,3,2)
# plt.imshow(blur,cmap='gray')
# plt.title("Blurred")
# pl



plt.tight_layout()
plt.show()

# cv2.imwrite('outputs/canny 50-150.jpg',edges1)
# cv2.imwrite('outputs/canny 10-100.jpg',edges2)
# cv2.imwrite('outputs/canny 100-200.jpg',edges3)

# cv2.imwrite('outputs/sobel_x.jpg',sobelx)
# cv2.imwrite('outputs/sobel_y.jpg',sobely)
# cv2.imwrite('outputs/sobel_combined.jpg',sobel_combined)

comparison = cv2.hconcat([
    cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR),
    cv2.cvtColor(sobel_combined, cv2.COLOR_GRAY2BGR),
    cv2.cvtColor(scharr_combined, cv2.COLOR_GRAY2BGR),
    cv2.cvtColor(lap, cv2.COLOR_GRAY2BGR)
])

cv2.imwrite('outputs/final_comparison.jpg', comparison)



cv2.imwrite('outputs/laplacian.jpg',lap)
cv2.imwrite('outputs/scharr.jpg',scharr_combined)

