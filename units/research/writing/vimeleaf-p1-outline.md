# ViMeLeaf Paper 1: Image Duplication Effects on DL-based Plant Recognition

**Journal**: Computers and Electronics in Agriculture  
**Deadline**: 2027-01-31  
**Status**: Outline — awaiting RES-40 paper details & RES-29 brief for final structure

---

## 1. Introduction

### 1.1 Background & Motivation
- Medicinal plant recognition: clinical & agricultural importance
- Deep learning success in plant image classification (cite CEA papers from RES-40)
- Dataset quality issues: data leakage, train/test overlap, duplication artifacts
- Vietnamese medicinal plants: knowledge gap in public ML datasets

### 1.2 Problem Statement
- Published plant recognition studies often show inflated accuracy due to dataset design flaws
- Duplicate images in training/validation splits artificially boost metrics
- Lack of transparent, public medicinal plant dataset with known quality baseline

### 1.3 Main Contributions
1. **Quantify duplication impact**: Measure accuracy degradation when duplicate images injected into train/val splits (quantitative analysis from RES-28)
2. **ViMeLeaf dataset release**: First public Vietnamese medicinal plant image dataset with metadata, known quality profile, benchmark results
3. **Validation protocol**: Best-practice guidelines for image-based plant recognition dataset curation

---

## 2. Related Work

### 2.1 Plant Recognition Datasets & Benchmarks
- Key public datasets (cite RES-40 papers: CEA recent surveys)
- DL architectures for plant classification: CNNs, transfer learning, vision transformers
- Benchmark results on major datasets

### 2.2 Data Quality & Dataset Artifacts
- Duplicate image detection methods
- Train/test contamination in published studies
- Strategies to mitigate data leakage (cite RES-40)
- Vietnamese plant recognition: existing work (if any; note gaps)

### 2.3 Medicinal Plant Recognition
- Clinical relevance of automated identification
- Challenges: morphological similarity, lighting/angle variation, occlusion

---

## 3. Materials & Methods

### 3.1 ViMeLeaf Dataset
- **Source**: Field collection from [region/herbarium] (from RES-28 dataset details)
- **Species**: N = [X] medicinal plant species (from RES-28)
- **Images**: Total [Y] RGB images; resolution [H×W]; standardization pipeline
- **Metadata**: Species ID, collection date, location, acquisition conditions
- **Preprocessing**: Resizing, augmentation strategy, train/val/test splits (reference RES-28)
- **Availability**: Public release via [platform/DOI] — *[pending RES-29 brief]*

### 3.2 Duplication Injection Experiment (RES-28)
- **Baseline model**: ResNet-50 / EfficientNet-B[X] pretrained (from RES-28 setup)
- **Training hyperparameters**: Learning rate, batch size, epochs, optimizer (from RES-28)
- **Duplication protocol**: 
  - Create copies of randomly selected training images
  - Inject into training set at ratios: 0%, 5%, 10%, 20%, 50% duplication rates
  - Keep validation/test sets pristine (no duplication)
- **Metrics**: Accuracy, Precision, Recall, F1-score, AUC-ROC per species
- **Statistical analysis**: Error bars, significance tests (from RES-28)

### 3.3 Validation & Cross-Checks
- 5-fold cross-validation on clean dataset
- Duplicate detection using image hashing (phash, dhash) to verify injection

---

## 4. Results

### 4.1 Main Findings

#### Table 1: Accuracy Degradation vs. Duplication Ratio
| Duplication Ratio | Top-1 Accuracy (%) | Drop from Baseline | F1-Score | Precision |
|------|---------|---------|---------|---------|
| 0% (Clean) | [RES-28 value] | — | [RES-28 value] | [RES-28 value] |
| 5% | [RES-28 value] | X% | [RES-28 value] | [RES-28 value] |
| 10% | [RES-28 value] | X% | [RES-28 value] | [RES-28 value] |
| 20% | [RES-28 value] | X% | [RES-28 value] | [RES-28 value] |
| 50% | [RES-28 value] | X% | [RES-28 value] | [RES-28 value] |

**Caption**: Each row shows performance on the same validation set; duplication only affects training set.

#### Figure 1: Accuracy Degradation Curve
- X-axis: Duplication ratio (%)
- Y-axis: Top-1 accuracy (%)
- Multiple lines: per-species breakdown (top-5 species)
- **Finding**: [RES-28 qualitative result — e.g., ~1% accuracy loss per 10% duplication]

#### Figure 2: Per-Class Accuracy Impact
- Heatmap: Species (rows) vs. Duplication Ratio (cols)
- Cell value: Accuracy degradation (%)
- **Finding**: Some species more robust to duplication than others (imbalance in training data?)

#### Figure 3: Example ViMeLeaf Images
- Grid: 2–3 images per species (N=8 species) showing dataset diversity
- Captions: Species name, acquisition date, field location

### 4.2 Dataset Statistics
- **Class distribution**: [histogram or table from RES-28]
- **Image resolution range**: [min–max pixels]
- **Annotation consistency**: [inter-rater agreement if applicable]

---

## 5. Discussion

### 5.1 Interpretation of Duplication Effects
- Accuracy inflation magnitude aligns with dataset size bias (cite RES-40 on data leakage)
- Species-wise variation suggests morphological similarity matters (harder to confuse botanically distinct species even with duplicates)
- Practical implication: **Transparent metadata critical** for downstream users

### 5.2 ViMeLeaf Contributions to Field
- First public Vietnamese medicinal plant dataset → enables regional ML research
- Known quality baseline → reference for future studies
- Benchmark results on modern architectures (ViT, etc.) provided

### 5.3 Limitations & Future Work
- Geographic scope: Limited to [region]; future versions expand nationwide
- Species count: [X] species; rare medicinal plants underrepresented
- Image conditions: Mostly daylight field photos; lighting variation limited
- Future: Herbarium specimens, synthetic augmentation, cross-camera robustness studies

---

## 6. Conclusion

Duplicate images in training sets can inflate plant recognition accuracy by [RES-28 estimate]%, highlighting the importance of rigorous dataset curation in agricultural ML. ViMeLeaf provides a transparent, public benchmark for medicinal plant recognition research, with documented quality profile and reproducible train/val/test splits. This study emphasizes validation best practices for botany-focused datasets.

---

## 7. Data Availability & Reproducibility

**ViMeLeaf Dataset**: 
- **URL/DOI**: [From RES-29 release plan]
- **License**: [e.g., CC-BY-4.0]
- **Code repository**: [Github link from RES-28 or RES-29]
- **Reproducibility**: 
  - All hyperparameters: Appendix A
  - Random seeds for train/val/test splits: [seed value from RES-28]
  - Train script: [github.com/...]/train_duplication_exp.py

---

## Figures & Tables Summary

| Item | Description | Source | Status |
|------|-------------|--------|--------|
| Table 1 | Accuracy vs. Duplication % | RES-28 experiments | ⏳ awaiting data |
| Figure 1 | Degradation curve | RES-28 experiments | ⏳ awaiting data |
| Figure 2 | Per-class heatmap | RES-28 experiments | ⏳ awaiting data |
| Figure 3 | Sample images | RES-28 dataset | ⏳ awaiting data |
| Appendix A | Hyperparameters | RES-28 config | ⏳ awaiting data |
| Appendix B | Class distribution | RES-28 dataset | ⏳ awaiting data |

---

## References (To Fill)

*Pending RES-40 papers review. Expected structure:*
1. 2–3 recent CEA papers on plant recognition datasets
2. Seminal DL plant classification papers (ResNet, EfficientNet applications)
3. Data leakage/duplication detection literature
4. Vietnam botany/agriculture context (if applicable)
