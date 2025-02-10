# Population Replacement Conspiracy Theory (PRCT) Detection Dataset

This repository contains resources for detecting Population Replacement Conspiracy Theories (PRCTs) in social media content, including a manually annotated gold standard dataset, annotation guidelines, and associated scripts.

## Dataset Description

The gold standard dataset consists of 500 manually annotated YouTube comments related to immigration discussions. Each comment has been labeled for the presence of Population Replacement Conspiracy Theory content, with an inter-annotator agreement of 0.891 (Gwet's AC1).

### Data Format

The anonymized gold standard dataset includes the following fields:
- `CommentID`: Unique identifier for each comment
- `CommentText`: The text content of the comment
- `Model_Classification`: Model's prediction
- `Annotation`: Manual annotation (0: Non-PRCT, 1: PRCT)
- `NumberOfLikes`: Number of likes received
- `IsReply`: Whether the comment is a reply
- `Level`: Depth level in the comment thread
- `ParentCommentText`: Text of the parent comment (if applicable)
- `Timestamp`: Month and year of the comment

## Repository Structure
```
.
├── LICENSE
├── README.md
├── technical_setup.md          # Hardware and software specifications
├── requirements.txt           # Project dependencies
├── data/
│   ├── anonymized_gold_standard.csv    # YouTube dataset
│   └── anonymized_telegram_test_set.csv # Telegram test set
├── annotation_guidelines/
│   ├── youtube-guidelines.md   # Guidelines for YouTube
│   └── telegram-guidelines.md  # Guidelines for Telegram
├── prompts/
│   └── generate_prompt.py     # LLM classification prompts
└── scripts/
    ├── gold_standard_anonimization.py
    └── telegram_anonimyzation.py
```

## Usage

### Data Access
The anonymized gold standard dataset is available in the `data` directory. The dataset has been carefully preprocessed to remove any personally identifiable information while maintaining its utility for research purposes.

### Annotation Guidelines
Two sets of annotation guidelines are provided:
1. YouTube-specific guidelines for comment annotation
2. Telegram guidelines used for cross-platform validation

### Classification Prompt
The `generate_prompt.py` file contains the structured prompt template used for few-shot learning with Large Language Models (GPT-4 and DeepSeek).

### Technical Setup
For detailed information about hardware requirements, model versions, and analysis pipeline, please refer to `technical_setup.md`.

## Citation

If you use this dataset in your research, please cite:
```bibtex
@inproceedings{marino2025one,
  title={One Model to Detect Them All? Comparing LLMs, BERT and Traditional ML in Cross-Platform Conspiracy Detection},
  author={Marino, Erik Bran and Vieira, Renata and Bassi, Davide and Ribeiro, Ana Sofia and Baleato, Suso},
  booktitle={Proceedings of the ACL 2025 Conference},
  year={2025}
}
```

## License

This dataset is released under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). This license allows reuse and adaptation for non-commercial purposes, as long as appropriate credit is given and adaptations are shared under the same terms.

## Contact

For questions about the dataset or research, please contact:
- Erik Bran Marino (erik.marino@uevora.pt)
- Renata Vieira (renatav@uevora.pt)

## Acknowledgments

This research was conducted at the Universidade de Évora and Universidade de Santiago de Compostela. We thank our annotators and reviewers for their valuable contributions to this work.
This research was assisted with LLMs: the python scripts were refined and better shaped with the help of Claude 3.5 Sonnet.
