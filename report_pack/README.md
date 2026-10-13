# report_pack — everything for the group report in one folder

| File / folder | What it is | Made by |
|---|---|---|
| `REPORT_NOTES.md` | **Start here.** Section-by-section guide to the report: key findings with the numbers, the text for data / methods / assumptions, limitations, recommendation, references, reproducibility appendix, corrections to the current draft and the link to the course labs | written by hand from the results |
| `INDEX.md` | List of every figure and table: number, caption, report section, notebook that made it, main text or appendix | `notebooks/05_report_pack.ipynb` |
| `figures/` | 40 figures numbered in the order of the report: `F01`–`F28` for the main text, `FA01`–`FA12` for the appendix (FA11 and FA12 show the two 23-stock charts in their other form: F13 as a heatmap, FA10 as bars) | `notebooks/05_report_pack.ipynb` (copies of `figures/`) |
| `tables/report_tables.xlsx` | 48 tables (`T01`–`T37` main text, `TA01`–`TA11` appendix), rounded and formatted (%, 2 decimals, p-values), one sheet each with a title and a note; first sheet = index. **Copy tables into Word from here** | `notebooks/05_report_pack.ipynb` |
| `tables/T..._*.csv`, `tables/TA..._*.csv` | The same tables as CSV (values already formatted as text) | `notebooks/05_report_pack.ipynb` |
| `tables/all_tables.md` | All the tables in one Markdown file (easy to read on GitHub) | `notebooks/05_report_pack.ipynb` |
| `tables/png/` | **Every table as an image** (48 PNG files, same colour scheme as the charts, with title and note): insert them in Word like a figure | `notebooks/05_report_pack.ipynb` |

**How to use it**

1. Read `REPORT_NOTES.md` (section 9 lists what to fix in the current draft).
2. Pick the figures and tables from `INDEX.md`; insert the PNG files from `figures/` and copy the tables from `tables/report_tables.xlsx`.
3. Use the captions in `INDEX.md` as a starting point and number them as in your report.

**Colours:** every chart and table image takes its colours from one file, `notebooks/appm_style.py`
(scheme "B - navy accents": one fixed colour per portfolio, the Group pick in navy, SPY in grey). To change a colour, edit it
there and run the notebooks again (or the "Run notebooks" button on GitHub).

**Do not edit the files in `figures/` and `tables/` by hand**: they are recreated every time `notebooks/05_report_pack.ipynb` runs
(locally, or with the "Run notebooks" button on GitHub → Actions). `REPORT_NOTES.md` and this README are not overwritten.

All numbers come from the frozen data in `notebooks/data/` and are reproducible (seed 2026, pinned library versions — see the main README).
