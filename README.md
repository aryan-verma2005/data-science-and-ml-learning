# Data Science and Machine Learning Learning Lab

A collection of notebooks, assignments, and small applications created while learning Python, data science, machine learning, and deep learning.

## Topics

- `numpy_tutorial.ipynb`, `pandas_tutorial*.ipynb`, and `thinking_data.ipynb`: introductory Python data work
- `Matplotlib/` and `Pandas Assignment/`: visualization and data-wrangling exercises
- `Supervised ML/`: supervised learning algorithms and scratch implementations
- `Unsupervised ML/`: clustering and dimensionality-reduction exercises
- `Deep Learning/`: neural networks, CNNs, GANs, RNNs, OpenAI API, and RAG notebooks
- `Reinforcement ML/`: Q-learning, SARSA, and a Flappy Bird project
- `Web-Scraping/` and `Assignment/`: scraping exercises and saved examples
- `FLASK/`: a small Flask application

## Separate Projects

These folders are independent GitHub repositories and are intentionally not included in this repository:

- CreditWise loan approval: [CreditWise-Loan-System](https://github.com/aryan-verma2005/CreditWise-Loan-System)
- SmartCart customer segmentation: [SmartCart-Segmentation-System](https://github.com/aryan-verma2005/SmartCart-Segmentation-System)

## API Notebook Setup

From the repository root, install the notebook dependencies and create a local environment file:

```sh
python -m pip install -r "Deep Learning/OpenAI/requirements.txt"
python -m pip install -r "Deep Learning/RAG/requirements.txt"
cp .env.example .env
```

Add your own `OPENAI_API_KEY` and/or `GROQ_API_KEY` values to `.env`. The OpenAI and RAG notebooks read their keys with `python-dotenv`. The `.env` file is ignored by Git; only the empty `.env.example` is intended to be shared.

## Data and Generated Files

Notebook checkpoint folders, local Python environments, model weights, generated RAG indexes, and large downloadable training datasets are excluded from Git. Keep private or licensed data out of a public repository; download excluded datasets separately where needed.