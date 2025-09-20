<div align="center">

# 🏥 Healthcare Claims Fraud Detection

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Machine Learning](https://img.shields.io/badge/ML-XGBoost-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://xgboost.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-brightgreen?style=for-the-badge)](https://github.com)

*A machine learning-powered web application that detects fraudulent healthcare insurance claims using advanced gradient boosting algorithms and explainable AI.*

</div>

---

## 📌 Introduction

This project implements a sophisticated **Healthcare Claims Fraud Detection System** that leverages machine learning to automatically classify insurance claims as legitimate or fraudulent. Built with a modern tech stack including **XGBoost**, **Streamlit**, and **SHAP**, it provides real-time fraud predictions with detailed explanations.

The application processes healthcare provider data, beneficiary information, and claim details to identify suspicious patterns and potential fraud cases, helping insurance companies save millions while ensuring legitimate claims are processed efficiently.

---

## 🚀 Features

- 🎯 **Real-time Fraud Detection** - Instant classification of healthcare claims
- 📊 **Interactive Data Analysis** - Comprehensive visualization of claim patterns
- 🔍 **Explainable AI** - SHAP values provide transparent model decisions
- 🎨 **Modern Web Interface** - Clean, responsive Streamlit-based UI
- 📈 **Performance Metrics** - Detailed model evaluation and statistics
- 🔄 **Model Retraining** - Easy model updates with new data
- 📱 **Responsive Design** - Works seamlessly across devices

---

## 📸 Screenshots

<div align="center">

### Main Dashboard
<img src="UIImages/screenshots/output.png" alt="Main Dashboard" width="800"/>

### Fraud Detection Interface
<img src="UIImages/screenshots/Fraud_vs_Lagitimate_clam.png" alt="Fraud Detection" width="400"/>
<img src="UIImages/screenshots/BarGraph.png" alt="Analysis Graphs" width="400"/>

### Data Analysis Views
<img src="UIImages/screenshots/Analysis_raw_dataset.png" alt="Raw Dataset Analysis" width="400"/>
<img src="UIImages/screenshots/Desriptive_Statistics.png" alt="Descriptive Statistics" width="400"/>

### Correlation Analysis
<img src="UIImages/screenshots/Correlation_matix_of_key_features.png" alt="Correlation Matrix" width="400"/>
<img src="UIImages/screenshots/Detailed_analysis_output_graph.png" alt="Detailed Analysis" width="400"/>

### About Page
<img src="UIImages/screenshots/About_me_page.png" alt="About Page" width="400"/>

</div>

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
|----------|------------|---------|
| **Backend** | Python 3.x | Core programming language |
| **ML Framework** | XGBoost, Scikit-learn | Gradient boosting & model evaluation |
| **Web Framework** | Streamlit | Interactive web application |
| **Data Processing** | Pandas, NumPy | Data manipulation and analysis |
| **Visualization** | Matplotlib, Seaborn, Altair | Charts and graphs |
| **Model Interpretation** | SHAP | Explainable AI |
| **Data Storage** | CSV, PKL | Model persistence and data storage |

---

## ⚙️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/FraudDetectionApp.git
   cd FraudDetectionApp
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv fraud_detection_env
   
   # Windows
   fraud_detection_env\Scripts\activate
   
   # macOS/Linux
   source fraud_detection_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset**
   
   Download the following files from [Kaggle Medicare Fraud Detection](https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis) and place them in the project root:
   - `Train-1542865627584.csv`
   - `Train_Beneficiarydata-1542865627584.csv`
   - `Train_Inpatientdata-1542865627584.csv`
   - `Train_Outpatientdata-1542865627584.csv`

---

## 📖 Usage

### Quick Start

1. **Preprocess the data**
   ```bash
   python preprocess_data.py
   ```

2. **Train the model**
   ```bash
   python train_model.py
   ```

3. **Launch the application**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Access the app**
   
   Open your browser and navigate to `http://localhost:8501`

### Application Features

- **🏠 Fraud Detection**: Upload claim data or enter details manually for real-time fraud prediction
- **📊 Data Analysis**: Explore comprehensive statistics and visualizations of your dataset
- **👤 About**: Learn more about the project and developer

### Model Testing

Test the trained model performance:
```bash
python test_model.py
```

---

## 🏗️ Project Structure

```
FraudDetectionApp/
├── 📁 UIImages/
│   ├── 📁 Screenshots/          # Application screenshots
│   └── 📁 Diagrams/             # Architecture diagrams
├── 📁 views/                    # Streamlit page modules
│   ├── fraud_detection.py      # Main fraud detection interface
│   ├── analysis.py             # Data analysis page
│   └── about_me.py             # About page
├── 📁 forms/                    # Form handling modules
├── 📁 assets/                   # Static assets
├── 🐍 streamlit_app.py         # Main application entry point
├── 🐍 train_model.py           # Model training script
├── 🐍 test_model.py            # Model testing script
├── 🐍 preprocess_data.py       # Data preprocessing pipeline
├── 📄 requirements.txt         # Python dependencies
├── 💾 *.pkl                    # Trained models and scalers
└── 📊 *.csv                    # Dataset files
```

---

## 🤝 Contributing

We welcome contributions to improve this fraud detection system! Here's how you can help:

### Ways to Contribute

- 🐛 **Report bugs** and issues
- 💡 **Suggest new features** or improvements
- 📝 **Improve documentation**
- 🔧 **Submit code improvements**
- 🧪 **Add test cases**

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 Python style guidelines
- Add docstrings to functions and classes
- Include comments for complex logic
- Test your changes thoroughly

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 FraudDetectionApp

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## ⭐ Support

If you found this project helpful or interesting, please consider:

- ⭐ **Starring** this repository
- 🍴 **Forking** it for your own use
- 📢 **Sharing** with others in the community
- 💬 **Opening issues** for bugs or feature requests

### Contact

- 📧 **Email**: [atif738738@gmail.com](mailto:atif738738@gmail.com)
- 🔗 **LinkedIn**: [Connect with me](https://www.linkedin.com/in/atif-raja-570853275)

### Acknowledgments

- Dataset provided by [Kaggle Medicare Fraud Detection](https://www.kaggle.com/datasets/rohitrox/healthcare-provider-fraud-detection-analysis)
- Built with ❤️ using Python, Streamlit, and XGBoost

---

<div align="center">

**Made with ❤️ for the Healthcare Community**

[⬆ Back to Top](#-healthcare-claims-fraud-detection)

</div>