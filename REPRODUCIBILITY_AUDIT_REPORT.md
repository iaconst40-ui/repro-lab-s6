# REPRODUCIBILITY AUDIT REPORT (DELIVERABLE BLOCK 5)
**Institution:** Universidad Nacional Mayor de San Marcos (UNMSM)
**Course:** Doctoral Program in Deep Technologies - Session 6
**Auditor:** Cesar Villar (iaconst4.0@gmail.com)
**Project Target:** Internal Forces Forecast ("mu22" Bending Moment) in RC Circular Reservoirs

---

## 1. PAPER & PROJECT METADATA
* **Project Name:** DATOS FINALES_PONENCIA_SAN_MARCOS
* **Domain Context:** Structural Engineering / Civil Artificial Intelligence
* **Target Architecture:** Multilayer Perceptron (MLP) Deep Neural Network (TensorFlow)
* **Dataset Fingerprint (MD5):** a5e69e1569c908b166ee96b6526ba4b1

---

## 2. EXPERIMENTAL SETUP & COMPUTE RECOVERY
* **Hardware Profile:** Executed and validated on standard CPU/GPU initialization layers (TensorFlow platform drivers verified).
* **Environment Isolation:** Pinned dependencies successfully mapped into virtual definitions (`requirements.txt` generated with explicit NumPy, Pandas, Scikit-Learn, TensorFlow, and MLflow versions).
* **Pipeline Traceability:** Managed completely through Git history layers with active version tracking.

---

## 3. LEAKAGE AUDIT & SIGNAL INTEGRITY CHECK
* **Data Splitting Strategy:** Fixed random split (80% Training / 20% Evaluation Test Subset).
* **Pre-processing Sandbox:** **CLEAN.** Feature and target standardizations (`MinMaxScaler`) utilize `fit_transform` solely within the training workspace. Test subset boundaries remain completely sealed during feature extraction, guaranteeing zero information contamination.

---

## 4. STATISTICAL RIGOR & MULTI-SEED VARIATION ANALYSIS
* **Randomness Control:** Seed-lottery phenomena evaluated by scaling the experiment over five isolated deterministic runs.
* **Empirical Performance Boundary (mu22 Bending Moment):** **0.9378 ± 0.0235** (\(R^2\) Score across 5 seeds evaluation loop).
* **Observation:** While the prediction network demonstrates robust stability, the pipeline currently locks performance reports onto standalone cross-validation steps without utilizing statistical significance tests.

---

## 5. REPRODUCIBILITY SCORECARD SUMMARY TABLE
The execution matrix was audited automatedly item-by-item according to the Session 6 Reproducibility Scorecard parameters:

| Checklist Item / Criterion | Status | Audit Evidence Summary / Justification |
| :--- | :---: | :--- |
| Seeds reported, many runs? | ✅ YES | Evaluated across 5 deterministic seeds. Result: 0.9378 ± 0.0235 |
| Splits described? | ✅ YES | Explicit 80/20 train/test partition setup configured in the training pipeline blueprint. |
| Leakage checked? | ✅ YES | Feature and target scalers fit strictly on training subsets. No validation/test data leaks. |
| Tuning separated? | ⚠️ PARTIAL | Validation split (0.1) used inside training loop, but lacks a full nested CV grid search. |
| Statistical test named? | ❌ NO | Models evaluated via R2 score metrics. No pair-wise statistical significance tests implemented. |
| Effect size and CI? | ❌ NO | Only mean and standard deviation are reported. True statistical effect sizes and CIs are missing. |
| External validation? | ❌ NO | Tested exclusively on internal random splits. No testing on an independent site or time period. |
| Compute documented? | ✅ YES | Pinned library versions generated in requirements.txt. Hardware initialization logged via TensorFlow. |
| Code and data available? | ✅ YES | Repository fully initialized. Data tracking secure via physical CSV files. MD5: a5e69e1569c908b166ee96b6526ba4b1 |

---

## 6. MISSING INFORMATION PROFILE & METHODOLOGICAL GAPS
1. **Statistical Significance Testing:** The testing architecture compares cross-seed variations but lacks paired hypothesis verification models (e.g., Corrected Resampled t-test or Dietterich's 5x2cv).
2. **True Effect Assessment:** Performance claims are constrained to absolute regression error limits (\(R^2\), MAE), failing to capture standard normalized effect sizes or bootstrap-derived 95% Confidence Intervals.
3. **External Generalization Boundary:** Model predictive limits have not been stress-tested against independent external population matrix zones (e.g., reservoirs with structural data changes outside the \(Z=0.45\) or \(f'c=280\) configuration baselines).

---

## 7. OVERALL COMPLIANCE JUDGMENT & SCORE
* **Quantitative Score:** **61.1 / 100.0**
* **Qualitative Audit Rating:** **MEDIUM REPRODUCIBILITY / VULNERABLE TO NOISE (B)**
* **Justification:** The project fulfills all critical core technical prerequisites for code, environment, and data reproducibility. Information leakage is strictly blocked. However, the score is penalized because it lacks robust inferential statistical tools (significance tests and confidence intervals) and external cohort validation profiles.

---

## 8. ACTIONABLE RECOMMENDATIONS (TOP 3 METHODOLOGICAL FIXES)
1. **Integrate Inferential Significance Frameworks:** Implement pair-wise statistical significance testing layers (such as a Corrected Resampled t-test) to prove that architectural upgrades outpace structural training noise.
2. **Transition from Standalone Metrics to Confidence Intervals:** Implement Bootstrap resampling wrappers over the final performance evaluations to report true 95% Confidence Intervals instead of basic Standard Deviations.
3. **Establish External Validation Thresholds:** Secure structural analytical configurations from a separate seismic sector dataset zone to test and document generalization limits before publishing clinical or structural deployment blueprints.
