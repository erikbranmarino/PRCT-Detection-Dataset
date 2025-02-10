# Technical Setup and Replication Information

## Hardware Configuration
- CPU: Apple M3 Max Pro
- GPU: 40-core GPU
- RAM: 64GB
- OS: macOS

## Model Versions
### BERT Models
- mBERT: bert-base-multilingual-cased
- CT-BERT: digitalepidemiologylab/covid-twitter-bert-v2
- HateBERT: GroNLP/hateBERT

### LLMs
- GPT-4o (gpt-4o-2024-08-06)
- DeepSeek-V3 (2024-12-26)

## Data Repository Structure
- Gold standard dataset (n=500): `/data/anonymized_gold_standard.csv`
- Cross-platform test set (n=160): `/data/anonymized_telegram_test_set.csv`
- Annotation guidelines: `/annotation_guidelines/`
- Classification prompts: `/prompts/generate_prompt.py`

## Analysis Pipeline
1. Data Collection & Preprocessing:
   - YouTube comments extraction
   - Data cleaning (removal of comments <15 chars)
   - Anonymization process (scripts provided in `/scripts/`)

2. Model Training Parameters:
   - BERT models fine-tuning:
     - Learning rate: 2e-5
     - Batch size: 32
     - Maximum epochs: 6
     - Early stopping on validation loss
   - Traditional ML:
     - Training/Test split: 80/20
     - Balanced class distribution
     - Cross-validation: 5-fold

3. Evaluation Process:
   - Gold standard validation
   - Cross-platform testing
   - Inter-annotator agreement metrics:
     - Gwet's AC1: 0.891
     - PABAK: 0.804
     - Observed Agreement: 90.2%

All code, data, and documentation are available at: https://github.com/erikbranmarino/PRCT-Detection-Dataset
