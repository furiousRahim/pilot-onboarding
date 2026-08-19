## Paper Title
> Food Classification and Meal Intake Amount Estimation
through Deep Learning

**Authors:** Ji-hwan Kim, Dong-seok Lee and Soon-kak Kwon


**Year:**  2023

**Venue / Journal:** Applied Sciences

**File:**  https://www.mdpi.com/2076-3417/13/9/5742


---

## 1. Problem Statement
> What problem does this paper address? Why does it matter?

This paper proposes a method for food classification and estimation of meal intake using pre- ans post-consumption images, using a deep learning object detection network. This matter because our project is also trying to solve the same thing. Therefore, the techniques used in this paper could be very helpful when building our model.

---

## 2. Dataset(s) Used
> What data did the authors use? How large? How was it collected/labeled?

The author screated their own dataset using Korean food images. It included 20 different food types groupe dinto three categories: rice, soup, and side dishes. The full dtaset had 520 images, which were split into 416 training images and 104 validation images.

The foods were placed in a 40.5 cm x 29.5 cm tray, while soup was was served in a separate bowl with a 3,5 cm radius. The images were labeled based on the specific food type so the mmodel could learn both the food type and its location on the tray.



---

## 3. Methods
> What AI/ML approach was applied? Describe the model architecture or algorithm.

The authors used **Mask R-CNN** to detect the food regions and classify each food type in both the pre- and post-meal images. Mask R-CNN works at the pixel level, so it could separate the actual food region from the rest of the plate instead of only putting a box around it.


Since the before and after pictures might not be taken from exactly the same position, they used a **homography transformation** to align the post-meal image with the pre-meal image using the detected meal plate as a reference.


After detecting the food area, each food was assigned one of three basic 3-D shapes: spherical cap, cone, or cuboid, depending on the food type. The system then estimated the food volume from the detected area and its assigned shape. Finally, the amount consumed was calculated from the difference between the food volume before and after the meal.
So the general process was:


Pre/Post images → Mask R-CNN detection and classification → align images (homography transformation) → assign 3-D food shape → estimate volume → calculate amount consumed.


---

## 4. Key Results
> What were the main findings? Include specific metrics (accuracy, AUROC, RMSE, IoU, etc.).

The model performed pretty ewell for both food classification and food region detection:

| Metric | Value |
|---|---|
| Food classification accuracy | up to 97.57% |
| Food region detection accuracy | up to 93.6% |
| Rice Classification | 63/63 = 100% |
| Soup Classification | 17/18 = 94.44% |
| Side-dish classification | 89/94 = 94.68 % |


For the food region detection, they used IoU (Intersection over Union), which measures how much the predicted food region overlaps with the actual labeled food region:
$$
IoU = \frac{\text{Predicted Region} \cap \text{Ground Truth Region}}
{\text{Predicted Region} \cup \text{Ground Truth Region}}
$$
So an IoU closer to 1 (or 100%) means the predicted food region matches the ground truth very well. The results also showed that the volume-estimation approach could be used to estimate how much food was consumed by comparing the estimated volumes before and after the meal. 



---

## 5. Limitations
> What are the weaknesses or open questions the authors identify?

One limitation is that the dataset was pretty small and only included 20 types of Korean food, so the model was tested on a very limited set of meals. Because of that, even though it performed well on this dataset, it may not perform the same on foods that look very different.
This is especially important for our project since we are looking at U.S. high school lunch trays, which can have different foods, portions, shapes, and presentation. Another limitation is that the volume estimation depends on matching foods to simple shapes like a spherical cap, cone, or cuboid, which may not work as well for irregular or mixed foods.

---

## 6. Relevance to Our Project
> How does this paper connect to the AI dietary assessment pipeline we are building?

This paper is relevant to our project because we are also using AI to analyze food images and estimate food consumption. It uses before and after meal images to estimate how much food was consumed, which is very similar to what we are trying to do. It also shows that food detection and classification can work well, but the results depend a lot on the type of food the model was trained on. For our project, we would need to make sure the model works well with U.S. high school lunch foods and not just the Korean foods used in this study.


---

## 7. One Thing I Found Surprising or Didn't Understand
> Write one honest observation — this keeps the reviews useful and honest.

One thing I was curious about was how well the volume estimation would work on foods that do not fit simple shapes like a sphere, cone, or cuboid. A lot of real meals, especially mixed foods, can have irregular shapes, so it'll be interesting to see how much that affects the final consumption estimate.
