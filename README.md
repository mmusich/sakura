# SAKURA 🌸 

Repository for Task 3.4 of the CMS-NGT-HLT project (**S**peedy **A**lignment & **C**alibration **U**pgrade for **R**eal-time **A**lgorithms)

## References

1. **CMS Collaboration**, *Next Generation Triggers Demonstrator: Time Variation of the Calibrations and System Monitoring*, CMS Detector Performance Note CMS-DP-2025/082 (17 Nov 2025). [CDS](https://cds.cern.ch/record/2950076)

2. **CMS Collaboration**, *Profiling the CMS reconstruction options within the Calibration Loop*, CMS Detector Performance Note CMS-DP-2025/087 (8 Dec 2025). [CDS](https://cds.cern.ch/record/2951246)

3. **CMS Collaboration**, *Physics Performance Assessment of the Run 3 Optimal Calibrations Next Generation Triggers Demonstrator*, CMS Detector Performance Note CMS-DP-2026/028 (18 May 2026). [CDS](https://cds.cern.ch/record/2961610)

4. **CMS Collaboration**, *Physics Performance Assessment of the Run 3 Optimal Calibrations Next Generation Triggers Demonstrator (Addendum)*, CMS Detector Performance Note CMS-DP-2026/119 (6 Aug 2026). [CDS](https://cds.cern.ch/record/2968109)

5. **Glines, C.** et al. *Calibration Profiling & Database solutions for optimal NGT-CMS-HLT Calibrations*, Zenodo (2026). [DOI](https://doi.org/10.5281/zenodo.22255567).

## Public Presentations

- **Musich, M.** et al. (2025) *Task 3.4: Optimal Calibrations for the CMS High-Level Trigger*. Next Generation Triggers 2nd Technical Workshop, CERN, 21 November 2025. [DOI](https://doi.org/10.17181/gzvw9-t3379).

- **Zarucki, M.** (2026). *Demonstrating the Processing Chain for the Next Generation Triggers in the CMS Experiment*. 28th Conference on Computing in High Energy and Nuclear Physics (CHEP 2026), CMS, CERN. [DOI](https://doi.org/10.17181/txk7r-fsd29).

- **Prendi, J.** (2026). *Conceptual Design and Operation of the Calibration Loop for the Next Generation Triggers in the CMS Experiment*. 28th Conference on Computing in High Energy and Nuclear Physics (CHEP 2026), CERN, 28 May 2026. [DOI](https://doi.org/10.17181/rv6ad-zpy87).

## Conceptual Design for Phase 2

NGT Scouting concept for Phase 2, underlining all the NGT-HLT ($R^3$) tasks:

![NGT Scouting](images/NGT-HLT_Scouting_Phase2_Workflow.png)

Conceptual design of the NGT Optimal Calibrations Workflow:

![NGT Optimal Calibrations (SAKURA) Workflow](images/NGT_OptimalCalibrations-SAKURA_Phase2.png)

## NGT Optimal Calibrations Demonstrator (Run 3) Workflow

![NGT Optimal Calibrations (SAKURA) Demonstrator Workflow](images/NGT_OptimalCalibrations-SAKURA_NERD.png)

Detailed data-flow (between SSDs and ramdisks) of the NGT demonstrator:

![NGT Optimal Calibrations (SAKURA) Demonstrator SSDs Data Flow](images/NGT_OptimalCalibrations-SAKURA_NERD_DataFlow.png)

## Continuous integration

Two workflows run on every push:

- **Pylint** (`.github/workflows/pylint.yml`)
  - *Errors*: `pylint --enable=E` over every tracked Python file, so genuine
    mistakes (undefined names, wrong calls) are caught repository-wide.
  - *Strict*: pylint (score ≥ 9.9), `isort` and `flake8` on the paths listed
    in [.github/linted-paths.txt](.github/linted-paths.txt). Add a directory
    to that list once its scripts are clean.
- **Tests** (`.github/workflows/tests.yml`): `pytest tests` (every tracked
  Python file compiles, every shell script parses, every JSON/YAML file is
  valid, plotting requirements stay pinned) plus `shellcheck`.

To reproduce them locally:

```bash
pip install pylint flake8 isort pytest pyyaml

# errors only, whole repository (same invocation as the CI)
pylint --disable=all --enable=E --disable=E0401,E1123,E1130 --score=n $(git ls-files '*.py')

# full standard, on the paths under the strict gate
pylint --fail-under=9.9 $(git ls-files 'Calibrations/NGTCalibrationLoop/*.py')

pytest tests -q
shellcheck -S error -e SC2148 $(git ls-files '*.sh')
```

The shared pylint settings live in [.pylintrc](.pylintrc), so a plain
`pylint <file>` reproduces what the CI does.
