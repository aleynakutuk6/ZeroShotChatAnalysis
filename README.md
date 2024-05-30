# Zero-Shot Sentiment Analysis
This project is developed to perform sentiment and intention analysis on a given textual dialog between a customer and an agent. It utilizes a pre-trained Zero-Shot Learning Model from Hugging Face.

The input data consists of a synthetic textual dialog between a customer and an agent, which is generated using ChatGPT. The dialogs are produced approximately in 20 steps, and the customer starts to the dialog by asking to purchase an iPhone 14.

This repository includes a codebase for Sentiment (positive, negative, neutral) and Intention Analysis (e.g., 'change_package,' 'upgrade,' etc.) utilizing [Facebook/BART-Large-MNLI](https://huggingface.co/facebook/bart-large-mnli) from Hugging Face.

###  File Structure
This repository have the following directory structure:

```
.
├── config
│   ├── bart_dialog_sentiment_config.ini
│   └── ...
├── resources
│   └── facebook-bart-large-mnli
│       ├── model.safetensors / pytorch_model.bin
│       └── ...
├── datasets
│   └── dialog_data
│       ├── dialog_1.json
│       └── ...
├── zero_shot_sentiment_analysis
│   ├── data
│   │   ├── __init__.py
│   │   └── dialog_dataset.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── io_utils.py
│   │   ├── model_loading.py
│   │   └── logger.py
│   ├── __init__.py
│   └── main.py
├── .pre-commit-config.yaml
├── .flake8
├── .gitattributes
├── .gitignore
├── LICENSE
├── setup.py
├── requirements.txt
└── README.md
```

## Installation

The code requires `python>=3.9`, as well as `pytorch>=2.0`. Please follow the instructions [here](https://pytorch.org/get-started/locally/) to install PyTorch dependencies.

1. Clone the repository:

    ```
    git clone https://github.com/aleynakutuk6/Zero-Shot-Sentiment-Analysis.git
    cd Zero-Shot-Sentiment-Analysis
    ```

2. To create and activate an environment, either:

   - install anaconda and run:

    ```
    conda create -n my_env python=3.9
    conda activate my_env
    ```

   - or run (in the root of the repository):

    ```
    python3 -m venv my_env
    source my_env/bin/activate
    ```

3. Run the following command to install required libraries:

    ```
    pip install -r requirements.txt
    ```

4. Run the code by providing a config file path:

    ```
    python zero_shot_sentiment_analysis/main.py -cfg config/bart_dialog_sentiment_config.ini
    ```

## Pre-Commit

Git hook scripts are useful for identifying simple issues. For this purpose, you are encouraged to run pre-commit before each commit. Please visit [here](https://pre-commit.com/) for detailed instructions.

```
# to install
pip install pre-commit
# to run
pre-commit run --all-files
```

## Acknowledgment

This repository is developed by utilizing a pre-trained deep learning model from Hugging Face Transformers library.
