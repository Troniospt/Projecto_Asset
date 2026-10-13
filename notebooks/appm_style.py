"""
appm_style.py - the colour scheme and the look of EVERY chart and table of the project.

All the notebooks (02, 03, 04 and 05) import this file, so a colour changed here changes it everywhere:

    1. edit a colour below (any matplotlib colour name or hex code, e.g. '#0d366b');
    2. run the notebooks again (or the "Run notebooks" button on GitHub).

How to use it in a notebook:

    from appm_style import apply_style, PORTFOLIO_COLOURS, COLOURS
    apply_style()                                   # once, at the top of the notebook
    plt.plot(x, y, color=PORTFOLIO_COLOURS['EW'])   # one fixed colour per portfolio

Scheme "B - navy accents": 8 colour-blind-safe hues for the 8 strategies (checked with a colour-vision-deficiency
simulation), the group's own portfolio in navy, the benchmark (SPY) in grey, white background, hairline grid,
tables with a navy header.
"""
import math
import textwrap

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


# =====================================================================================================
# 1. GENERAL COLOURS (background, text, grid, tables)
# =====================================================================================================
COLOURS = {
    'background':        '#ffffff',   # background of charts and tables
    'text':              '#1b1b1b',   # titles and main text
    'text_secondary':    '#52514e',   # axis labels, tick labels, legends
    'muted':             '#898781',   # notes, reference lines
    'grid':              '#e6e6e6',   # gridlines (thin and solid)
    'axis':              '#c3c2b7',   # axis lines
    'reference':         '#52514e',   # reference lines (zero, 50%, beta = 1, ...)
    'accent':            '#0d366b',   # navy: highlights and table headers
    'single_series':     '#2a78d6',   # colour of a chart that shows only one series (e.g. WMT returns)
    'second_series':     '#eb6834',   # second colour when a chart compares two things (e.g. data vs normal curve)
    'table_header':      '#0d366b',   # header row of the tables (navy)
    'table_header_text': '#ffffff',
    'table_stripe':      '#f2f6fb',   # every second row of a table (very light blue)
    'table_highlight':   '#fff4d6',   # highlighted row (the Group pick) - light yellow
    'table_line':        '#d9dee7',   # thin lines between table rows
}

# =====================================================================================================
# 2. ONE FIXED COLOUR PER PORTFOLIO (the same colour in every chart of every notebook)
# =====================================================================================================
PORTFOLIO_COLOURS = {
    'EW':                     '#2a78d6',   # blue
    'Markowitz (λ=3)':        '#eb6834',   # orange
    'GMV':                    '#1baf7a',   # aqua
    'Max Sharpe':             '#eda100',   # yellow
    'Inverse vol':            '#e87ba4',   # magenta
    'Risk parity (ERC)':      '#008300',   # green
    'Most diversified':       '#6250d6',   # violet
    'Max decorrelation':      '#e34948',   # red
    'Group pick (23 stocks)': '#0d366b',   # navy - the group's own portfolio
    'SPY (buy & hold)':       '#898781',   # grey - the market benchmark
}

# Other names that appear in the charts (variants of the portfolios above, the indices and WMT)
OTHER_COLOURS = {
    'Markowitz (λ=1)':     '#f4a582',   # lighter / darker orange: the risk-aversion sensitivity
    'Markowitz (λ=5)':     '#a8431a',
    'SPY (total return)':  '#898781',   # grey, like SPY in the backtest
    '^GSPC (price index)': '#c3c2b7',   # light grey (drawn dashed)
    'SPY':                 '#898781',
    '^GSPC':               '#c3c2b7',
    'WMT':                 '#2a78d6',   # Walmart = the "single series" blue
    'Normal':              '#eb6834',   # reference normal distribution (orange)
    'Student-t':           '#008300',   # reference Student-t distribution (green)
    'Daily':               '#2a78d6',   # the three frequencies
    'Weekly':              '#eb6834',
    'Monthly':             '#1baf7a',
}

# Colours for charts whose bars are METRICS, not portfolios (e.g. "% of experiments that beat EW" on Sharpe, return, ...):
# shades of navy/blue and grey, so they are not confused with the portfolio colours above
METRIC_COLOURS = {
    'Sharpe':             '#0d366b',
    'Return':             '#3987e5',
    'Drawdown (smaller)': '#9ec5f4',
    'Volatility (lower)': '#5f86c4',
    'Sterling':           '#898781',
}

# Colours for charts with several unnamed series, used in this order (the order keeps neighbours distinct)
SERIES_COLOURS = ['#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#e87ba4', '#008300', '#6250d6', '#e34948']

# Colours for the 23 stocks in the stacked-bar charts (23 different colours are needed there; see the heatmap
# version of the same charts, which needs only one colour)
STOCK_COLOURS = ['#2a78d6', '#9ec5f4', '#eb6834', '#f6b392', '#1baf7a', '#8fd9bd', '#eda100', '#f7d27a',
                 '#e87ba4', '#f3bdd2', '#008300', '#7fc17f', '#6250d6', '#b0a7eb', '#e34948', '#f1a4a3',
                 '#0d366b', '#5f86c4', '#898781', '#c3c2b7', '#8c564b', '#c49c94', '#3b3b3b']

# One-colour scale for magnitudes (heatmaps of weights, correlations of size): white -> navy
SEQUENTIAL = ['#ffffff', '#cde2fb', '#9ec5f4', '#6da7ec', '#3987e5', '#256abf', '#184f95', '#0d366b']

# Two-colour scale with a grey middle (e.g. win rates around 50%, correlations around 0):
# low values -> orange-red, middle -> light grey, high values -> blue
DIVERGING = ['#d95926', '#f0efec', '#256abf']


# =====================================================================================================
# 3. FUNCTIONS
# =====================================================================================================
def apply_style():
    """Sets the look of every matplotlib chart drawn after it (call it once at the top of a notebook)."""
    plt.style.use('default')                                   # start from matplotlib's defaults (same on every computer)
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',                          # installed with matplotlib -> identical on every computer
        'font.size': 10,
        'figure.facecolor': COLOURS['background'],
        'axes.facecolor': COLOURS['background'],
        'savefig.facecolor': COLOURS['background'],
        'axes.edgecolor': COLOURS['axis'],
        'axes.labelcolor': COLOURS['text_secondary'],
        'axes.titlecolor': COLOURS['text'],
        'axes.titlesize': 11,
        'axes.titleweight': 'bold',
        'axes.spines.top': False,                              # no box around the plot: only the left and bottom axes
        'axes.spines.right': False,
        'axes.grid': True,
        'axes.axisbelow': True,                                # gridlines behind the data
        'grid.color': COLOURS['grid'],
        'grid.linestyle': '-',                                 # solid hairlines (dashed grids look noisy)
        'grid.linewidth': 0.8,
        'xtick.color': COLOURS['text_secondary'],
        'ytick.color': COLOURS['text_secondary'],
        'legend.frameon': False,
        'legend.labelcolor': COLOURS['text_secondary'],
        'text.color': COLOURS['text'],                         # default colour of ax.text and annotations
        'lines.linewidth': 1.6,
        'axes.prop_cycle': plt.cycler(color=SERIES_COLOURS),  # default colours when none is given
        'image.cmap': 'appm_sequential',
        'savefig.dpi': 150,
    })


def colour(name):
    """The colour of a portfolio, index or series by its name (grey if the name is unknown)."""
    if name in PORTFOLIO_COLOURS:
        return PORTFOLIO_COLOURS[name]
    if name in OTHER_COLOURS:
        return OTHER_COLOURS[name]
    return COLOURS['muted']


def sequential_cmap():
    """White -> navy colour scale (for magnitudes, e.g. portfolio weights)."""
    return LinearSegmentedColormap.from_list('appm_sequential', SEQUENTIAL)


def diverging_cmap():
    """Orange-red -> grey -> blue colour scale (for values above / below a middle point, e.g. 50% or 0)."""
    return LinearSegmentedColormap.from_list('appm_diverging', DIVERGING)


def reference_line(ax, y=None, x=None, label=None, zorder=1):
    """A thin reference line (horizontal at y, or vertical at x), e.g. zero, 50% or beta = 1.
    zorder=1 draws it behind bars and lines; use a larger zorder (e.g. 3) to draw it on top."""
    if y is not None:
        ax.axhline(y, color=COLOURS['reference'], linewidth=1, label=label, zorder=zorder)
    if x is not None:
        ax.axvline(x, color=COLOURS['reference'], linewidth=1, label=label, zorder=zorder)


def text_colour_on(fill_colour):
    """Black or white text, whichever is easier to read on a coloured cell (used in heatmaps)."""
    red, green, blue = plt.matplotlib.colors.to_rgb(fill_colour)
    brightness = 0.299 * red + 0.587 * green + 0.114 * blue
    return COLOURS['text'] if brightness > 0.55 else '#ffffff'


# Register the two colour scales under a name, so they can also be used as cmap='appm_sequential' / 'appm_diverging'
for _cmap in [sequential_cmap(), diverging_cmap()]:
    try:
        plt.colormaps.register(_cmap)
    except ValueError:                     # already registered (the file was imported twice)
        pass


# =====================================================================================================
# 4. TABLES AS PNG IMAGES
# =====================================================================================================
def _looks_like_number(text):
    # '35.6%', '-0.12', '<0.001', '12' -> True; 'EW', 'Supported' -> False
    cleaned = str(text).replace('%', '').replace('<', '').replace('−', '-').replace(',', '').strip()
    if cleaned == '':
        return False
    try:
        float(cleaned)
        return True
    except ValueError:
        return False


def save_table_png(table, path, title=None, note=None, highlight=('Group pick',), font_size=9,
                   max_text_width=42, max_header_width=16, dpi=200):
    """
    Saves a table (pandas DataFrame) as a PNG image with the colours of section 1.

    table      : the table; numbers should already be formatted as text (e.g. '35.6%'), as in notebook 05.
                 The index is not drawn: put the row names in the first column.
    path       : where to save the image, e.g. '../report_pack/tables/png/T15_median_metrics.png'
    title, note: text above / below the table (optional)
    highlight  : rows whose first cell starts with one of these words get the highlight colour (the Group pick)
    """
    cells = table.astype(str).replace({'nan': '', 'None': ''}).values.tolist()
    headers = [str(column) for column in table.columns]
    n_columns = len(headers)

    # Numbers are right-aligned, text is left-aligned
    numeric = []
    for j in range(n_columns):
        values = [row[j] for row in cells if row[j] != '']
        numeric.append(len(values) > 0 and sum(_looks_like_number(v) for v in values) >= 0.8 * len(values))

    # Wrap long text (cells and headers) so that no column becomes too wide
    def wrap(text, width):
        # never break inside a word or at a hyphen ('ex-ante' stays together)
        return textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False) or ['']

    wrapped_cells = [[[cell] if numeric[j] else wrap(cell, max_text_width) for j, cell in enumerate(row)] for row in cells]
    widest_value = [max([len(line) for row in wrapped_cells for line in row[j]] + [1]) for j in range(n_columns)]
    longest_word = [max([len(word) for word in headers[j].split()] + [1]) for j in range(n_columns)]
    wrapped_headers = [wrap(headers[j], max(max_header_width, widest_value[j], longest_word[j])) for j in range(n_columns)]

    # Sizes in inches: a character is about 0.6 x the font size wide; 72 points = 1 inch
    char_width = font_size * 0.6 / 72
    line_height = font_size * 1.45 / 72
    padding = font_size * 0.8 / 72
    bold_char_width = font_size * 0.68 / 72              # bold header letters are a little wider
    # if a row is highlighted (written in bold), size the columns for bold text
    any_highlight = bool(highlight) and any(any(row[0].startswith(word) for word in highlight) for row in cells)
    body_char_width = bold_char_width if any_highlight else char_width
    column_widths = [max(widest_value[j] * body_char_width, max(len(line) for line in wrapped_headers[j]) * bold_char_width)
                     + 2.5 * padding for j in range(n_columns)]
    header_height = max(len(lines) for lines in wrapped_headers) * line_height + 1.2 * padding
    row_heights = [max(len(cell) for cell in row) * line_height + 0.9 * padding for row in wrapped_cells]
    # math.fsum instead of sum: Python 3.12+ adds floats slightly differently with sum(), which would move the image by a
    # fraction of a pixel; fsum gives exactly the same total on every Python version
    table_width = math.fsum(column_widths)

    title_lines = wrap(title, int(table_width / (char_width * 1.15))) if title else []
    note_lines = wrap(note, int(table_width / (char_width * 0.9))) if note else []
    title_height = len(title_lines) * line_height * 1.25 + (padding if title else 0)
    note_height = len(note_lines) * line_height * 0.95 + (padding if note else 0)
    total_height = title_height + header_height + math.fsum(row_heights) + note_height

    fig = plt.figure(figsize=(table_width, total_height))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, table_width)
    ax.set_ylim(total_height, 0)                      # y grows downwards, like reading a table
    ax.axis('off')
    fig.patch.set_facecolor(COLOURS['background'])

    y = 0
    for line in title_lines:                           # title
        ax.text(0, y + line_height * 0.6, line, fontsize=font_size * 1.15, fontweight='bold', color=COLOURS['text'], va='center')
        y += line_height * 1.25
    y += padding if title else 0

    # Header row
    ax.add_patch(plt.Rectangle((0, y), table_width, header_height, color=COLOURS['table_header'], linewidth=0))
    x = 0
    for j in range(n_columns):
        text_x = x + column_widths[j] - padding if numeric[j] else x + padding
        ax.text(text_x, y + header_height / 2, '\n'.join(wrapped_headers[j]), fontsize=font_size, fontweight='bold',
                color=COLOURS['table_header_text'], va='center', ha='right' if numeric[j] else 'left', linespacing=1.15)
        x += column_widths[j]
    y += header_height

    # Body rows
    for i, row in enumerate(wrapped_cells):
        first_cell = cells[i][0]
        is_highlight = any(first_cell.startswith(word) for word in highlight) if highlight else False
        if is_highlight:
            fill = COLOURS['table_highlight']
        elif i % 2 == 1:
            fill = COLOURS['table_stripe']
        else:
            fill = COLOURS['background']
        ax.add_patch(plt.Rectangle((0, y), table_width, row_heights[i], color=fill, linewidth=0))
        ax.plot([0, table_width], [y + row_heights[i]] * 2, color=COLOURS['table_line'], linewidth=0.5)
        x = 0
        for j, lines in enumerate(row):
            text_x = x + column_widths[j] - padding if numeric[j] else x + padding
            ax.text(text_x, y + row_heights[i] / 2, '\n'.join(lines), fontsize=font_size, color=COLOURS['text'],
                    va='center', ha='right' if numeric[j] else 'left', linespacing=1.15,
                    fontweight='bold' if is_highlight else 'normal')
            x += column_widths[j]
        y += row_heights[i]

    y += padding * 0.6 if note else 0
    for line in note_lines:                            # note below the table
        ax.text(0, y + line_height * 0.5, line, fontsize=font_size * 0.85, style='italic', color=COLOURS['muted'], va='center')
        y += line_height * 0.95

    fig.savefig(path, dpi=dpi, facecolor=COLOURS['background'], bbox_inches='tight', pad_inches=0.08)
    plt.close(fig)
