## Paper Title
> A Cross-Sectional Reproducibility Study of a Standard Camera
Sensor Using Artificial Intelligence to Assess Food Items:
The FoodIntech Project

**Authors:** Virginie Van Wymelbeke-Delannoy, Charles Juhel, Hugo Bole, Amadou-Khalilou Sow,
Charline Guyot, Farah Belbaghdadi, Olivier Brousse and Michel Paindavoine
Hennessy 
**Year:**  2022
**Venue / Journal:** Nutrients 
**File:**  https://www.mdpi.com/2072-6643/14/1/221

---

## 1. Problem Statement
> What problem does this paper address? Why does it matter?

This paper looks at whether the FoodIntech, a smartphone-based food consumption assessment system, can accurately estimate how much food is on a plate using a regular camera and AI. The main goal was to see if the system could give consistent portion-size estimates when the same foods were measured multiple times. This matters for our project because we are also trying to estimate food consumption from images, so understanding how reliable AI-based portion estimation can be is directly related to the kind of system we are building.

---

## 2. Dataset(s) Used
> What data did the authors use? How large? How was it collected/labeled?

The study used 169 different dishes prepared by the Dijon University Hospital between December 2020 and May 2021. The meals were prepared the same way they would normally be served to patients. Each food item was identified from 77 food categories, while the exact recipe was already known from the hospital menu. The trays also used a QR code label to match the before- and after-consumption images. Each dish was photographed under different simulated consumption levels, with conditions repeated 4 to 14 times.


---

## 3. Methods
> What AI/ML approach was applied? Describe the model architecture or algorithm.

The FoodIntech system used **deep neural networks** (DNNs) to automatically detect, segment, and recognize the different food items in the images. The system used an image taken before eating and another one taken after eating, and a QR code on the tray was used to match the two images together. It then compared the images to estimate how much food was left and how much was consumed.


To test how consistent the system was, the authors repeated the measurements for each dish and used a **Type 3 Intraclass Correlation Coefficient (ICC)** to measure reproducibility. The ICC was calculated for each dish, and the authors also reported a 95% confidence interval for the ICC values. Here's how they split the ICC reesluts:

* ICC close to **1** = very constant measurements
* ICC around **0.7 or higher** = henrally acceptable/ good reproducibility
* Low ICC = the system gave more variable results between repeated measurements


The pipeline is as follows:

pre/post consumption images --> match images using a QR code --> detect and segment items on the tray --> recognize food --> estimate consumption


---

## 4. Key Results
> What were the main findings? Include specific metrics (accuracy, AUROC, RMSE, IoU, etc.).

Overall, the FoodIntech system showed different levels of reliability depending on the type of food. Out of the dishes they were able to evaluate, the system had excellent reliability for 39% (n = 58 dishes) and good reliability for 19% (n = 28 dishes). 


| Metric | Value |
|---|---|
| Excellent reliability | 39% (58 dishes) |
| Good reliability | 19% (28 dishes) |

These results show that the system worked well for a good number of the dishes, but it was not equally reliable for every type of food. The authors mention that things like the shape, texture, and presentation of the food could affect how well the system estimated the amount consumed. 


---

## 5. Limitations
> What are the weaknesses or open questions the authors identify?





---

## 6. Relevance to Our Project
> How does this paper connect to the AI dietary assessment pipeline we are building?

This paper is relevant to our project because we are also using AI to analyze food images and estimate food consumption. It also shows why having a good ground truth is important so we can compare our AI estimates to the actual food amount.

---

## 7. One Thing I Found Surprising or Didn't Understand
> Write one honest observation — this keeps the reviews useful and honest.

One thing I did not fully understand was how the authors could confidently compare the different error rates when the studies were using very different datasets and evaluation methods.
