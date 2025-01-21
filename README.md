# Intrusion Detection System Using Machine Learning

## Project Overview

An Intrusion Detection System (IDS) monitors network traffic to identify potential threats and ensure cybersecurity. This project leverages machine learning techniques to classify and detect various types of network intrusions. The system provides a robust solution for identifying anomalies and suggesting preventive measures, enhancing security for users and organizations.

## Key Features

- **Machine Learning Models**: Implements XGBoost, Random Forest, Decision Trees, and Extra Trees for intrusion detection.
- **Ensemble Model**: Combines multiple models to improve detection accuracy.
- **Prevention Suggestions**: Offers actionable recommendations to mitigate detected threats.
- **User-Friendly Interface**: A web-based platform for uploading files and reviewing intrusion reports.
- **Real-Time Detection**: Analyzes real-time network traffic to dynamically detect intrusions.

## Datasets Used

The system was trained and tested using the following datasets:  
1. **[CICIDS2017](https://www.unb.ca/cic/datasets/ids-2017.html)**  
2. **[UNSW_NB15](https://research.unsw.edu.au/projects/unsw-nb15-dataset)**  
4. **[KDDCup-99](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html)**  


## Results and Performance

- **Accuracy**: Achieved high accuracy on multiple datasets, with XGBoost consistently delivering superior results post-optimization.
- **Optimization**: Bayesian optimization was used to enhance model performance.
- **Ensemble Model**: Improved overall performance by combining individual models.


## Installation and Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/idkupickaname/Intrusion-Detection-System.git
   ```
2. Navigate to the project directory:  
   ```bash
   cd Intrusion-Detection-System
   ```
3. Install dependencies:  
   ```bash
   npm install
   ```
4. Start the application:  
   ```bash
   npm start
   ```

## Usage

1. Open the web interface.  
2. Upload network traffic data files.  
3. View intrusion detection reports and receive preventive measures.  

## Future Work

- Integration with newer datasets to tackle emerging cybersecurity threats.
- Exploration of models for connected vehicles, IoT, and other advanced use cases.
- Enhancements in scalability and user interface.
