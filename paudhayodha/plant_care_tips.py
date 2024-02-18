class_code_to_label = {
    0: 'Tomato___Late_blight',
    1: 'Tomato___healthy',
    2: 'Grape___healthy',
    3: 'Orange___Haunglongbing_(Citrus_greening)',
    4: 'Soybean___healthy',
    5: 'Squash___Powdery_mildew',
    6: 'Potato___healthy',
    7: 'Corn_(maize)___Northern_Leaf_Blight',
    8: 'Tomato___Early_blight',
    9: 'Tomato___Septoria_leaf_spot',
    10: 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    11: 'Strawberry___Leaf_scorch',
    12: 'Peach___healthy',
    13: 'Apple___Apple_scab',
    14: 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
    15: 'Tomato___Bacterial_spot',
    16: 'Apple___Black_rot',
    17: 'Blueberry___healthy',
    18: 'Cherry_(including_sour)___Powdery_mildew',
    19: 'Peach___Bacterial_spot',
    20: 'Apple___Cedar_apple_rust',
    21: 'Tomato___Target_Spot',
    22: 'Pepper,_bell___healthy',
    23: 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    24: 'Potato___Late_blight',
    25: 'Tomato___Tomato_mosaic_virus',
    26: 'Strawberry___healthy',
    27: 'Apple___healthy',
    28: 'Grape___Black_rot',
    29: 'Potato___Early_blight',
    30: 'Cherry_(including_sour)___healthy',
    31: 'Corn_(maize)___Common_rust_',
    32: 'Grape___Esca_(Black_Measles)',
    33: 'Raspberry___healthy',
    34: 'Tomato___Leaf_Mold',
    35: 'Tomato___Spider_mites Two-spotted_spider_mite',
    36: 'Pepper,_bell___Bacterial_spot',
    37: 'Corn_(maize)___healthy',
}

label_to_name = {
    'Apple___Apple_scab': 'Apple with Apple Scab',
    'Apple___Black_rot': 'Apple with Black Rot',
    'Apple___Cedar_apple_rust': 'Apple with Cedar Apple Rust',
    'Apple___healthy': 'Healthy Apple',
    'Blueberry___healthy': 'Healty Blueberry',
    'Cherry_(including_sour)___Powdery_mildew': 'Cherry (including sour) with Powdery Mildew',
    'Cherry_(including_sour)___healthy': 'Healthy Cherry (including sour)',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 'Corn (maize) with Cercospora (gray leaf spot)',
    'Corn_(maize)___Common_rust_': 'Corn (maize) with Common Rust',
    'Corn_(maize)___Northern_Leaf_Blight': 'Corn (maize) with Northern Leaf Blight',
    'Corn_(maize)___healthy': 'Healthy Corn (maize)',
    'Grape___Black_rot': 'Grape with Black Rot',
    'Grape___Esca_(Black_Measles)': 'Grape with Esca [Black Measles]',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 'Grape with Leaf Blight [Isariopsis Leaf Spot]',
    'Grape___healthy': 'Healthy Grape',
    'Orange___Haunglongbing_(Citrus_greening)': 'Orange with Haunglongbing (citrus greening)',
    'Peach___Bacterial_spot': 'Peach with Bacterial Spot',
    'Peach___healthy': 'Healthy Peach',
    'Pepper,_bell___Bacterial_spot': 'Bell Pepper with Bacterial Spot',
    'Pepper,_bell___healthy': 'Healthy Bell Pepper',
    'Potato___Early_blight': 'Potato with Early Blight',
    'Potato___Late_blight': 'Potato with Late Blight',
    'Potato___healthy': 'Healthy Potato',
    'Raspberry___healthy': 'Healthy Raspberry',
    'Soybean___healthy': 'Healthy Soybean',
    'Squash___Powdery_mildew': 'Squash with Powdery Mildew',
    'Strawberry___Leaf_scorch': 'Strawberry with Leaf Scorch',
    'Strawberry___healthy': 'Healthy Strawberry',
    'Tomato___Bacterial_spot': 'Tomato with Bacterial Spot',
    'Tomato___Early_blight': 'Tomato with Early Blight',
    'Tomato___Late_blight': 'Tomato with Late Blight',
    'Tomato___Leaf_Mold': 'Tomato with Leaf Mold',
    'Tomato___Septoria_leaf_spot': 'Tomato with Septoria (leaf spot)',
    'Tomato___Spider_mites Two-spotted_spider_mite': 'Tomato with (two-spotted) Spider Mites',
    'Tomato___Target_Spot': 'Tomato with Target Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Tomato with Yellow Leaf Curl Virus',
    'Tomato___Tomato_mosaic_virus': 'Tomato with Mosaic Virus',
    'Tomato___healthy': 'Healthy Tomato'
}

# TODO: Add better plant care tips
plant_care_tips = {
    'Apple___Apple_scab': 'To prevent apple scab, practice good sanitation by removing fallen leaves and fruit.   Apply fungicides at appropriate times in the growing season.   Prune the trees during the dormant season to improve air circulation.   Choose resistant apple varieties if available and ensure proper spacing between trees to promote airflow.  ',
    'Apple___Black_rot': 'Prune infected parts of the tree and remove mummified fruits to reduce overwintering inoculum.   Apply fungicides before bud break in the spring and as needed during the growing season.   Improve orchard drainage to minimize moisture around the trees.   Remove nearby wild apple and crabapple trees, which can serve as sources of inoculum.  ',
    'Apple___Cedar_apple_rust': 'Plant resistant apple varieties and remove cedar trees in the vicinity, as they serve as alternate hosts.   Apply fungicides preventively during the spring, especially during wet periods when spore release is likely.   Improve air circulation within the orchard through proper pruning and spacing.  ',
    'Apple___healthy': 'Regularly prune apple trees to improve air circulation and sunlight exposure.   Apply fertilizers as needed based on soil test results.   Monitor for pests such as aphids, mites, and codling moths, and take appropriate control measures if necessary.   Water the trees deeply during dry periods, especially in the summer months.  ',
    'Blueberry___healthy': 'Plant blueberries in well-drained, acidic soil with a pH between 4.  5 and 5.  5.   Provide regular irrigation, especially during dry spells, to keep the soil consistently moist.   Mulch around the base of the plants to suppress weeds and retain soil moisture.   Prune blueberry bushes annually to remove dead or diseased wood and promote new growth.  ',
    'Cherry_(including_sour)___Powdery_mildew': 'Improve air circulation around cherry trees by proper pruning to reduce humidity and minimize powdery mildew infection.   Apply fungicides preventively starting at bud break and continue throughout the growing season at regular intervals.   Monitor for symptoms and take immediate action at the first sign of infection.  ',
    'Cherry_(including_sour)___healthy': 'Prune cherry trees to open up the canopy and improve sunlight penetration, which helps prevent diseases.   Apply balanced fertilizers in early spring based on soil test results to promote tree health and fruit production.   Monitor for pests such as cherry fruit fly and cherry slug and apply appropriate control measures as needed.  ',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': 'Rotate crops to prevent buildup of pathogens in the soil.   Use resistant corn varieties when available and applicable.   Apply fungicides as soon as symptoms appear or preventively during periods of high humidity and warm temperatures.   Maintain optimal plant spacing and avoid overhead irrigation to reduce leaf wetness duration.  ',
    'Corn_(maize)___Common_rust_': 'Plant resistant corn varieties and remove crop debris after harvest to reduce overwintering inoculum.   Apply fungicides preventively if needed, especially during periods of high humidity and warm temperatures.   Monitor fields regularly for signs of rust infection and take immediate action to prevent its spread.  ',
    'Corn_(maize)___Northern_Leaf_Blight': 'Rotate crops and avoid planting corn in the same area multiple years in a row to reduce disease pressure.   Use resistant corn varieties and apply fungicides preventively during periods of high humidity and warm temperatures.   Practice proper field hygiene by removing crop debris after harvest to minimize overwintering inoculum.  ',
    'Corn_(maize)___healthy': 'Plant corn in well-drained soil with adequate nutrients.   Provide consistent irrigation, especially during the critical reproductive stages.   Monitor fields regularly for signs of pests such as corn borers and European corn borer and apply appropriate control measures if necessary.   Apply balanced fertilizers based on soil test results to optimize yield potential.  ',
    'Grape___Black_rot': 'Prune grapevines to improve air circulation and sunlight exposure, which helps reduce humidity and minimize black rot infection.   Apply fungicides preventively starting at bud break and continue at regular intervals throughout the growing season.   Remove and destroy mummified berries and infected plant parts to reduce overwintering inoculum.  ',
    'Grape___Esca_(Black_Measles)': 'Practice proper pruning techniques to minimize wounds on grapevines, which serve as entry points for the esca fungus.   Apply fungicides preventively, especially during periods of active growth and susceptibility.   Monitor vineyards regularly for symptoms of esca and take immediate action to prevent its spread.  ',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': 'Prune grapevines for good air circulation and apply fungicides preventively during the growing season, especially during periods of high humidity and warm temperatures.   Remove and destroy infected leaves and shoots to reduce disease spread within the vineyard.   Monitor vineyards regularly for signs of leaf blight and take immediate action if detected.  ',
    'Grape___healthy': 'Plant grapevines in well-drained soil with good sunlight exposure.   Prune vines annually to remove excess growth and promote fruiting.   Apply balanced fertilizers based on soil test results to maintain vine health and productivity.   Monitor vineyards regularly for signs of pests such as grape phylloxera and grapevine leafhopper and take appropriate control measures as needed.  ',
    'Orange___Haunglongbing_(Citrus_greening)': 'Control citrus psyllids, which spread the disease, with insecticides.   Remove and destroy infected trees to prevent further spread of the disease.   Plant disease-resistant citrus varieties when available and applicable.   Implement cultural practices such as mulching and proper irrigation to promote tree health and vigor.  ',
    'Peach___Bacterial_spot': 'Plant resistant peach varieties and avoid overhead irrigation to minimize leaf wetness duration.   Apply copper-based fungicides preventively starting at bud break and continue at regular intervals throughout the growing season.   Monitor orchards regularly for signs of bacterial spot and take immediate action to prevent its spread.  ',
    'Peach___healthy': 'Prune peach trees to improve airflow and sunlight penetration, which helps reduce disease incidence.   Apply balanced fertilizers in early spring based on soil test results to promote tree health and fruit production.   Monitor orchards regularly for signs of pests such as peach twig borer and oriental fruit moth and take appropriate control measures as needed.  ',
    'Pepper,_bell___Bacterial_spot': 'Plant disease-resistant pepper varieties and avoid overhead irrigation to minimize leaf wetness duration.   Apply copper-based fungicides preventively starting at transplanting and continue at regular intervals throughout the growing season.   Monitor pepper plants regularly for signs of bacterial spot and take immediate action to prevent its spread.  ',
    'Pepper,_bell___healthy': 'Provide well-drained soil and adequate spacing between pepper plants to promote airflow and reduce humidity.   Apply balanced fertilizers based on soil test results to promote plant growth and fruit production.   Monitor pepper plants regularly for signs of pests such as aphids and thrips and take appropriate control measures as needed.  ',
    'Potato___Early_blight': 'Practice crop rotation and remove infected plant debris to reduce overwintering inoculum.   Apply fungicides preventively starting at emergence and continue at regular intervals throughout the growing season.   Monitor potato fields regularly for signs of early blight and take immediate action to prevent its spread.  ',
    'Potato___Late_blight': 'Plant certified disease-free seed potatoes and practice good garden sanitation to reduce disease pressure.   Apply fungicides preventively starting at emergence and continue at regular intervals throughout the growing season, especially during periods of high humidity and cool temperatures.   Monitor potato fields regularly for signs of late blight and take immediate action to prevent its spread.  ',
    'Potato___healthy': 'Plant potatoes in well-drained, sandy loam soil with good fertility.   Apply balanced fertilizers based on soil test results to promote tuber development and yield.   Monitor potato fields regularly for signs of pests such as Colorado potato beetles and potato aphids and take appropriate control measures as needed.  ',
    'Raspberry___healthy': 'Plant raspberries in well-drained soil with good sunlight exposure.   Prune raspberry canes regularly to remove old and diseased wood and promote new growth.   Provide trellising support for trailing varieties to keep the canes off the ground and reduce disease incidence.   Apply balanced fertilizers based on soil test results to promote plant growth and fruit production.  ',
    'Soybean___healthy': 'Plant soybeans in well-drained soil with good fertility.   Rotate crops to reduce disease pressure and minimize pest populations.   Monitor soybean fields regularly for signs of pests such as soybean aphids and bean leaf beetles and take appropriate control measures as needed.   Apply balanced fertilizers based on soil test results to optimize yield potential.  ',
    'Squash___Powdery_mildew': 'Plant resistant squash varieties and provide good air circulation by proper spacing and pruning to reduce humidity.   Apply fungicides preventively starting at the first sign of powdery mildew and continue at regular intervals throughout the growing season.   Monitor squash plants regularly for signs of powdery mildew and take immediate action to prevent its spread.  ',
    'Strawberry___Leaf_scorch': 'Plant disease-resistant strawberry varieties and avoid overhead irrigation to minimize leaf wetness duration.   Apply fungicides preventively starting at bloom and continue at regular intervals throughout the growing season.   Monitor strawberry plants regularly for signs of leaf scorch and take immediate action to prevent its spread.  ',
    'Strawberry___healthy': 'Plant strawberries in well-drained soil with good sunlight exposure.   Mulch around plants to suppress weeds and conserve soil moisture.   Provide adequate irrigation, especially during dry periods, to promote plant growth and fruit production.   Monitor strawberry plants regularly for signs of pests such as slugs and strawberry root weevils and take appropriate control measures as needed.  ',
    'Tomato___Bacterial_spot': 'Plant disease-resistant tomato varieties and avoid overhead irrigation to minimize leaf wetness duration.   Apply copper-based fungicides preventively starting at transplanting and continue at regular intervals throughout the growing season.   Remove and destroy infected plant debris to reduce overwintering inoculum.  ',
    'Tomato___Early_blight': 'Rotate tomato crops and provide good air circulation by proper spacing and pruning to reduce humidity.   Apply fungicides preventively starting at transplanting and continue at regular intervals throughout the growing season.   Monitor tomato plants regularly for signs of early blight and take immediate action to prevent its spread.  ',
    'Tomato___Late_blight': 'Plant resistant tomato varieties and avoid overhead irrigation to minimize leaf wetness duration.   Apply fungicides preventively starting at transplanting and continue at regular intervals throughout the growing season.   Monitor tomato plants regularly for signs of late blight and take immediate action to prevent its spread.  ',
    'Tomato___Leaf_Mold': 'Plant tomatoes in well-drained soil with good air circulation to reduce humidity.   Apply fungicides preventively starting at transplanting and continue at regular intervals throughout the growing season.   Remove and destroy infected plant debris to reduce overwintering inoculum.  ',
    'Tomato___Septoria_leaf_spot': 'Rotate tomato crops and remove infected plant debris to reduce overwintering inoculum.   Apply fungicides preventively starting at transplanting and continue at regular intervals throughout the growing season.   Monitor tomato plants regularly for signs of septoria leaf spot and take immediate action to prevent its spread.  ',
    'Tomato___Spider_mites Two-spotted_spider_mite': 'Monitor for spider mites and apply miticides as needed, especially during hot and dry periods when populations are likely to increase.   Keep plants well-watered to reduce stress and minimize spider mite infestations.   Avoid excessive nitrogen fertilization, which can increase susceptibility to spider mite damage.  ',
    'Tomato___Target_Spot': 'Rotate tomato crops and provide good air circulation by proper spacing and pruning to reduce humidity.   Apply fungicides preventively starting at transplanting and continue at regular intervals throughout the growing season.   Monitor tomato plants regularly for signs of target spot and take immediate action to prevent its spread.  ',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': 'Control whiteflies, which spread the virus, with insecticides.   Remove and destroy infected plants to prevent further spread of the virus.   Plant disease-resistant tomato varieties when available and applicable.   Implement cultural practices such as mulching and proper irrigation to promote plant health and vigor.  ',
    'Tomato___Tomato_mosaic_virus': 'Control aphids, which spread the virus, with insecticides.   Remove and destroy infected plants to prevent further spread of the virus.   Plant disease-resistant tomato varieties when available and applicable.   Implement cultural practices such as mulching and proper irrigation to promote plant health and vigor.  ',
    'Tomato___healthy': 'Plant tomatoes in well-drained soil with good sunlight exposure.   Provide support for vines as needed to prevent fruit rot.   Apply balanced fertilizers based on soil test results to promote plant growth and fruit production.   Monitor tomato plants regularly for signs of pests such as tomato hornworms and tomato fruitworms and take appropriate control measures as needed.  '
}

# plant_care_tips_md = {
#     'Apple___Apple_scab': """**Preventing Apple Scab:**

#     * **Practice good sanitation:** Remove fallen leaves and fruit regularly.
#     * **Apply fungicides:** Use them at appropriate times during the growing season.
#     * **Prune trees during dormancy:** Improve air circulation.
#     * **Choose resistant varieties:** Opt for apple varieties resistant to scab if available.
#     * **Ensure proper spacing:** Allow proper space between trees for better airflow.
#     """,
#     'Apple___Black_rot': """**Managing Apple Black Rot:**

#     * **Prune infected parts:** Remove infected branches and remove mummified fruits.
#     * **Apply fungicides:** Use them before bud break in spring and as needed during the season.
#     * **Improve drainage:** Enhance orchard drainage to minimize moisture around trees.
#     * **Remove nearby wild apples:** Eliminate nearby wild apple and crabapple trees that can harbor the disease.
#     """,
#     'Apple___Cedar_apple_rust': """**Controlling Cedar-Apple Rust:**

#     * **Plant resistant varieties:** Choose apple varieties resistant to the disease.
#     * **Remove cedar trees:** Eliminate cedar trees in the vicinity, which act as alternate hosts.
#     * **Apply fungicides preventively:** Use them during spring, especially during wet periods.
#     * **Improve air circulation:** Prune and space trees appropriately for better air flow.
#     """,
#     'Apple___healthy': """**Keeping Apple Trees Healthy:**

#     * **Regular pruning:** Prune regularly to improve air circulation and sunlight exposure.
#     * **Balanced fertilization:** Apply fertilizers based on soil test results.
#     * **Pest monitoring:** Watch for aphids, mites, and codling moths, and take control measures if needed.
#     * **Deep watering:** Water trees deeply during dry periods, especially in summer.
#     """,
#     'Blueberry___healthy': """**Growing Healthy Blueberries:**

#     * **Well-drained, acidic soil:** Plant blueberries in soil with a pH between 4.5 and 5.5.
#     * **Regular irrigation:** Water regularly, especially during dry spells, to maintain consistent moisture.
#     * **Mulching:** Apply mulch around the base of plants to suppress weeds and retain moisture.
#     * **Annual pruning:** Prune annually to remove dead or diseased wood and encourage new growth.
#     """,
#     'Cherry_(including_sour)___Powdery_mildew': """**Combating Powdery Mildew in Cherries:**

#     * **Improve air circulation:** Prune properly to reduce humidity and minimize infection.
#     * **Apply fungicides preventively:** Start at bud break and continue throughout the season.
#     * **Monitor for symptoms:** Take immediate action at the first sign of infection.
#     """,
#     'Cherry_(including_sour)___healthy': """**Maintaining Healthy Cherry Trees:**

#     * **Open the canopy:** Prune to improve sunlight penetration and prevent diseases.
#     * **Balanced fertilization:** Apply fertilizers based on soil test results in early spring.
#     * **Pest control:** Monitor for cherry fruit fly and cherry slug, and take necessary measures.
#     """,
#     'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': """**Managing Cercospora and Gray Leaf Spot in Corn:**

#     * **Crop rotation:** Rotate crops to prevent pathogen buildup in the soil.
#     * **Resistant varieties:** Use resistant corn varieties when available.
#     * **Fungicide application:** Apply fungicides upon symptom appearance or preventively during high humidity and warm temperatures.
#     * **Optimal plant spacing:** Maintain proper spacing and avoid overhead irrigation to reduce leaf wetness.
#     """,
#     'Corn_(maize)___Common_rust_': """**Controlling Common Rust in Corn:**

#     * **Resistant varieties:** Plant corn varieties resistant to rust.
#     * **Crop debris removal:** Remove crop debris after harvest to reduce overwintering inoculum.
#     * **Fungicide application:** Apply fungicides preventively if needed, especially during high humidity and warm temperatures.
#     * **Monitor fields regularly:** Watch for signs of rust infection and take action to prevent spread.
#     """,
#     'Corn_(maize)___Northern_Leaf_Blight': """**Preventing Northern Leaf Blight in Corn:**

#     * **Crop rotation:** Rotate crops to avoid planting corn in the same area consecutively.
#     * **Resistant varieties:** Use corn varieties resistant to northern leaf blight.
#     * **Fungicide application:** Apply fungicides preventively during high humidity and warm temperatures.
#     * **Proper field hygiene:** Remove crop debris after harvest to minimize overwintering inoculum.
#     """,
# }
