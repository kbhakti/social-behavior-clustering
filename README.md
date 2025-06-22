# social-behavior-clustering
Discovery of Personality Archetypes through Social Behavior Clustering - This project is a part of the "Machine learning: Fundamentals and Applications (AAI-510-IN3)" course in the Applied Artificial Intelligence Program at the University of San Diego (USD).

Project Status: Ongoing
## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   https://github.com/kbhakti/social-behavior-clustering
   cd social-behavior-clustering

2. Install Dependencies:

   ```bash
   pip install -r requirements.txt

3. Run the model clusters:
   
   ```bash
   python model_cluster_api.py

5. Run the Streamlit Application:
   
   ```bash
   streamlit run streamlit_cluster_app.py

## Objective

Project Description: This project aims to uncover hidden personality archetypes based on behavioral and social activity data using unsupervised machine learning techniques. By applying clustering algorithms to features such as time spent alone, social event attendance, and social media engagement, we aim to segment individuals into distinct personality-based groups beyond the binary classification of extrovert vs. introvert. These insights can drive targeted marketing, personalized content recommendations, and mental wellness interventions.

Project Objectives:
•	Preprocess and clean the dataset by handling missing values and encoding categorical variables.
•	Perform exploratory data analysis (EDA) to identify patterns and distributions across behavioral traits.
•	Apply clustering algorithms (e.g., K-Means) to group individuals into distinct personality archetypes.
•	Visualize the resulting clusters and interpret the defining features of each personality group.
•	Evaluate cluster quality using silhouette score and other metrics to ensure meaningful segmentation.
•	Provide business use-case recommendations for utilizing the identified personality segments (e.g., targeted digital campaigns, personalized user experiences).

## Dataset Used 
Extrovert vs. Introvert Personality Traits Dataset(https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data/data)

## Contributors
Teammates: Bhakti Kanungo, Manasa sai Karaka, Evin Joy
## License
This project is licensed under the MIT License, allowing users to freely use, modify, and distribute the work with proper attribution. The full license details are available in the LICENSE file included in the project folder.
