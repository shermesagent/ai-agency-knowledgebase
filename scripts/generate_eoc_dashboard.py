#!/usr/bin/env python3
"""
Parse the STAAR EOC comparison CSV and generate an interactive HTML dashboard.
The CSV is comma-delimited with quoted fields (standard CSV).
"""
import csv
import json
import re
import os

CSV_PATH = "/home/writingtired/.hermes/cache/documents/doc_d8f08a52e851_report.csv"
OUTPUT_PATH = os.path.expanduser("~/www/eoc-comparison/index.html")

SUBJECTS = ["Algebra I", "Biology", "English I", "English II", "U.S. History"]

# Column structure: Org, ID/CDC, Admin, then 5 subjects x 10 metrics each
# Per subject: Tests Taken, Avg Scale Score, Did Not Meet Count, Did Not Meet %,
#   Approaches+ Count, Approaches+ %, Meets+ Count, Meets+ %, Masters Count, Masters %
METRIC_KEYS = [
    "Tests Taken",
    "Average Scale Score",
    "Did Not Meet Count",
    "Did Not Meet Percentage",
    "Approaches and Above Count",
    "Approaches and Above Percentage",
    "Meets and Above Count",
    "Meets and Above Percentage",
    "Masters Count",
    "Masters Percentage",
]

METRIC_LABELS = [
    "Tests Taken",
    "Avg Scale Score",
    "Did Not Meet (Count)",
    "Did Not Meet (%)",
    "Approaches+ (Count)",
    "Approaches+ (%)",
    "Meets+ (Count)",
    "Meets+ (%)",
    "Masters (Count)",
    "Masters (%)",
]


def parse_value(v):
    v = v.strip().strip('"')
    if not v or v == '-':
        return None
    try:
        return int(v)
    except ValueError:
        try:
            return float(v)
        except ValueError:
            return v


def main():
    rows = []
    with open(CSV_PATH, newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for i, row in enumerate(reader):
            if i == 0:
                continue  # skip header
            if len(row) < 4:
                continue

            org = row[0].strip()
            cdc = row[1].strip()
            admin = row[2].strip()
            year_match = re.search(r'(\d{4})', admin)
            year = year_match.group(1) if year_match else admin

            row_data = {
                "Organization": org,
                "ID/CDC": cdc,
                "Administration": admin,
                "Year": year
            }

            for s_idx, subject in enumerate(SUBJECTS):
                base = 3 + s_idx * 10
                for m_idx in range(10):
                    col = base + m_idx
                    if col < len(row):
                        val = parse_value(row[col])
                    else:
                        val = None
                    key = subject + "|" + METRIC_KEYS[m_idx]
                    row_data[key] = val

            rows.append(row_data)

    print(f"Parsed {len(rows)} rows")

    # Build the dashboard HTML
    html_template = HTML_TEMPLATE
    html = html_template.replace("__DATA_JSON__", json.dumps(rows))
    html = html.replace("__ORGS_JSON__", json.dumps(sorted(set(r["Organization"] for r in rows))))
    html = html.replace("__SUBJECTS_JSON__", json.dumps(SUBJECTS))
    html = html.replace("__METRIC_LABELS_JSON__", json.dumps(METRIC_LABELS))
    html = html.replace("__METRIC_KEYS_JSON__", json.dumps(METRIC_KEYS))

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        f.write(html)

    print(f"Dashboard written to {OUTPUT_PATH}")
    print(f"File size: {os.path.getsize(OUTPUT_PATH):,} bytes")


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>STAAR EOC Comparison Dashboard</title>
<style>
  :root {
    --bg: #0f1117;
    --surface: #1a1d27;
    --surface-2: #242736;
    --border: #2a2d3a;
    --text: #e4e6ed;
    --text-dim: #8b8fa3;
    --accent: #c89b3c;
    --accent-hover: #d4a94a;
    --up: #22c55e;
    --down: #ef4444;
    --neutral: #8b8fa3;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
  }
  .header {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 1.25rem 2rem;
    position: sticky;
    top: 0;
    z-index: 100;
  }
  .header-inner {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
  }
  .header h1 {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--accent);
  }
  .header .subtitle {
    color: var(--text-dim);
    font-size: 0.85rem;
  }
  .controls {
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
  }
  .controls label {
    font-size: 0.85rem;
    color: var(--text-dim);
  }
  .controls select {
    background: var(--surface-2);
    color: var(--text);
    border: 1px solid var(--border);
    padding: 0.4rem 0.75rem;
    border-radius: 6px;
    font-size: 0.85rem;
    cursor: pointer;
  }
  .controls select:focus {
    outline: none;
    border-color: var(--accent);
  }
  .search-box {
    background: var(--surface-2);
    color: var(--text);
    border: 1px solid var(--border);
    padding: 0.4rem 0.75rem;
    border-radius: 6px;
    font-size: 0.85rem;
    width: 200px;
  }
  .search-box:focus {
    outline: none;
    border-color: var(--accent);
  }
  .main {
    max-width: 1400px;
    margin: 0 auto;
    padding: 1.5rem 2rem;
  }
  .summary-bar {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    margin-bottom: 1.5rem;
  }
  .summary-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
    text-align: center;
  }
  .summary-card .value {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--accent);
  }
  .summary-card .label {
    font-size: 0.8rem;
    color: var(--text-dim);
    margin-top: 0.25rem;
  }
  .table-container {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    overflow: hidden;
  }
  .table-scroll {
    overflow-x: auto;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.85rem;
    white-space: nowrap;
  }
  thead {
    position: sticky;
    top: 0;
  }
  th {
    background: var(--surface-2);
    color: var(--text-dim);
    font-weight: 500;
    text-align: left;
    padding: 0.65rem 0.75rem;
    border-bottom: 1px solid var(--border);
    cursor: pointer;
    user-select: none;
    position: relative;
    font-size: 0.8rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
  }
  th:hover {
    color: var(--accent);
  }
  th .sort-icon {
    margin-left: 4px;
    opacity: 0.3;
  }
  th.sorted .sort-icon {
    opacity: 1;
    color: var(--accent);
  }
  td {
    padding: 0.55rem 0.75rem;
    border-bottom: 1px solid var(--border);
  }
  tr:hover td {
    background: rgba(200, 155, 60, 0.04);
  }
  .org-name {
    font-weight: 500;
  }
  .org-farmersville td {
    background: rgba(200, 155, 60, 0.06);
  }
  .num {
    text-align: right;
    font-variant-numeric: tabular-nums;
  }
  .pct {
    text-align: right;
    font-variant-numeric: tabular-nums;
  }
  .change-down { color: var(--down); }
  .change-up { color: var(--up); }
  .change-neutral { color: var(--neutral); }
  .year-col {
    font-size: 0.8rem;
    color: var(--text-dim);
    font-weight: 500;
  }
  .footer {
    text-align: center;
    padding: 1.5rem;
    color: var(--text-dim);
    font-size: 0.8rem;
  }
  .no-data {
    text-align: center;
    padding: 3rem;
    color: var(--text-dim);
  }
  .tag {
    display: inline-block;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 500;
  }
  .tag-state { background: #1e3a5f; color: #60a5fa; }
  .tag-region { background: #3b2f1e; color: var(--accent); }
  .tag-district { background: #1a2e1a; color: #4ade80; }
  @media (max-width: 768px) {
    .header { padding: 1rem; }
    .header-inner { flex-direction: column; align-items: flex-start; }
    .main { padding: 1rem; }
    .controls { width: 100%; }
    .search-box { width: 100%; }
    .summary-bar { grid-template-columns: repeat(2, 1fr); }
    table { font-size: 0.75rem; }
    th, td { padding: 0.4rem 0.5rem; }
  }
</style>
</head>
<body>

<div class="header">
  <div class="header-inner">
    <div>
      <h1>STAAR EOC Comparison Dashboard</h1>
      <div class="subtitle">Region 10 Districts &middot; Spring 2025 &amp; 2026</div>
    </div>
    <div class="controls">
      <div>
        <label for="subject-select">Subject</label>
        <select id="subject-select"></select>
      </div>
      <div>
        <label for="metric-select">Metric</label>
        <select id="metric-select"></select>
      </div>
      <div>
        <label for="search-box">Search district</label>
        <input type="text" class="search-box" id="search-box" placeholder="e.g. Farmersville">
      </div>
    </div>
  </div>
</div>

<div class="main">
  <div class="summary-bar" id="summary-bar"></div>
  <div class="table-container">
    <div class="table-scroll" id="table-wrapper">
      <table id="data-table">
        <thead id="table-head"></thead>
        <tbody id="table-body"></tbody>
      </table>
    </div>
  </div>
  <div class="footer">
    Data source: Texas Education Agency STAAR EOC files &middot; Farmersville ISD Curriculum &amp; Instruction
  </div>
</div>

<script>
// === DATA (injected by generator) ===
const ALL_DATA = __DATA_JSON__;
const ORGS = __ORGS_JSON__;
const SUBJECTS = __SUBJECTS_JSON__;
const METRIC_LABELS = __METRIC_LABELS_JSON__;
const METRIC_KEYS = __METRIC_KEYS_JSON__;

// === STATE ===
let state = {
  subject: "All Subjects",
  metricIdx: 5,
  sortCol: 1,
  sortDir: 'desc',
  search: ''
};

const YEARS = [...new Set(ALL_DATA.map(function(r) { return r.Year; }))].sort();

function getOrgType(org) {
  if (org === "STATE") return "state";
  if (org.indexOf("REG") === 0) return "region";
  return "district";
}

// Build simple column model for "All Subjects" view
function buildOverviewData() {
  const map = {};
  for (var i = 0; i < ALL_DATA.length; i++) {
    var r = ALL_DATA[i];
    var key = r.Organization + "|" + r.Year;
    if (!map[key]) {
      map[key] = {
        Organization: r.Organization,
        Year: r.Year,
        subjects: {}
      };
    }
    for (var s = 0; s < SUBJECTS.length; s++) {
      var subj = SUBJECTS[s];
      map[key].subjects[subj] = {
        "Tests Taken": r[subj + "|Tests Taken"],
        "Average Scale Score": r[subj + "|Average Scale Score"],
        "Did Not Meet Count": r[subj + "|Did Not Meet Count"],
        "Did Not Meet Percentage": r[subj + "|Did Not Meet Percentage"],
        "Approaches and Above Count": r[subj + "|Approaches and Above Count"],
        "Approaches and Above Percentage": r[subj + "|Approaches and Above Percentage"],
        "Meets and Above Count": r[subj + "|Meets and Above Count"],
        "Meets and Above Percentage": r[subj + "|Meets and Above Percentage"],
        "Masters Count": r[subj + "|Masters Count"],
        "Masters Percentage": r[subj + "|Masters Percentage"]
      };
    }
  }
  return Object.keys(map).sort().map(function(k) { return map[k]; });
}

function getMetricKey(idx) {
  return METRIC_KEYS[idx];
}

// === RENDER ===
function render() {
  var subject = state.subject;
  var search = state.search.toLowerCase();

  if (subject === "All Subjects") {
    renderOverview(search);
  } else {
    renderSingle(subject, search);
  }

  updateSummaryBar();
  updateSortIndicators();
}

function renderOverview(search) {
  var data = buildOverviewData();
  var filtered = [];
  for (var i = 0; i < data.length; i++) {
    if (data[i].Organization.toLowerCase().indexOf(search) >= 0) {
      filtered.push(data[i]);
    }
  }

  var metricIdx = state.metricIdx;
  var metricKey = METRIC_KEYS[metricIdx];
  var metricLabel = METRIC_LABELS[metricIdx];
  var isPct = metricKey.indexOf("Percentage") >= 0;

  // Columns: Org, Year, then each subject's relevant metric
  var columns = [
    { key: 'Organization', label: 'District', type: 'text' },
    { key: 'Year', label: 'Year', type: 'text' }
  ];
  for (var s = 0; s < SUBJECTS.length; s++) {
    columns.push({
      key: SUBJECTS[s],
      label: SUBJECTS[s] + ' ' + (isPct ? metricLabel.replace(/\([^)]*\)/, '').trim() : metricLabel),
      type: isPct ? 'pct' : 'num',
      subj: SUBJECTS[s],
      metricKey: metricKey
    });
  }

  doSort(filtered, columns);

  // Render header
  var thead = document.getElementById('table-head');
  var hhtml = '<tr>';
  for (var i = 0; i < columns.length; i++) {
    var isSorted = state.sortCol === i;
    hhtml += '<th data-col="' + i + '" class="' + (isSorted ? 'sorted' : '') + '">';
    hhtml += columns[i].label;
    hhtml += '<span class="sort-icon">' + (isSorted ? (state.sortDir === 'asc' ? '\u25B2' : '\u25BC') : '\u21C5') + '</span>';
    hhtml += '</th>';
  }
  hhtml += '</tr>';
  thead.innerHTML = hhtml;
  thead._columns = columns;

  // Render body
  var tbody = document.getElementById('table-body');
  if (filtered.length === 0) {
    tbody.innerHTML = '<tr><td colspan="' + columns.length + '" class="no-data">No districts match your search</td></tr>';
    return;
  }

  var bhtml = '';
  for (var i = 0; i < filtered.length; i++) {
    var row = filtered[i];
    var orgType = getOrgType(row.Organization);
    var isFarm = row.Organization === 'FARMERSVILLE ISD';
    bhtml += '<tr class="' + (isFarm ? 'org-farmersville' : '') + '">';
    bhtml += '<td class="org-name"><span class="tag tag-' + orgType + '">' + orgType + '</span> ' + row.Organization + '</td>';
    bhtml += '<td class="year-col">' + row.Year + '</td>';

    for (var c = 2; c < columns.length; c++) {
      var col = columns[c];
      var subj = col.subj;
      var sd = row.subjects && row.subjects[subj];
      var val = sd ? sd[col.metricKey] : null;
      var display = '\u2014';
      if (val !== null && val !== undefined) {
        if (isPct) display = val + '%';
        else display = typeof val === 'number' ? val.toLocaleString() : val;
      }
      bhtml += '<td class="' + col.type + '">' + display + '</td>';
    }
    bhtml += '</tr>';
  }
  tbody.innerHTML = bhtml;
}

function renderSingle(subject, search) {
  var filtered = [];
  for (var i = 0; i < ALL_DATA.length; i++) {
    if (ALL_DATA[i].Organization.toLowerCase().indexOf(search) >= 0) {
      filtered.push(ALL_DATA[i]);
    }
  }

  var columns = [
    { key: 'Organization', label: 'District', type: 'text' },
    { key: 'Year', label: 'Year', type: 'text' },
    { key: subject + '|Tests Taken', label: 'Tests Taken', type: 'num' },
    { key: subject + '|Average Scale Score', label: 'Avg Score', type: 'num' },
    { key: subject + '|Did Not Meet Count', label: 'Did Not Meet', type: 'num' },
    { key: subject + '|Did Not Meet Percentage', label: 'DNM %', type: 'pct' },
    { key: subject + '|Approaches and Above Count', label: 'Approaches+', type: 'num' },
    { key: subject + '|Approaches and Above Percentage', label: 'Appr+ %', type: 'pct' },
    { key: subject + '|Meets and Above Count', label: 'Meets+', type: 'num' },
    { key: subject + '|Meets and Above Percentage', label: 'Meets+ %', type: 'pct' },
    { key: subject + '|Masters Count', label: 'Masters', type: 'num' },
    { key: subject + '|Masters Percentage', label: 'Masters %', type: 'pct' }
  ];

  doSort(filtered, columns);

  var thead = document.getElementById('table-head');
  var hhtml = '<tr>';
  for (var i = 0; i < columns.length; i++) {
    var isSorted = state.sortCol === i;
    hhtml += '<th data-col="' + i + '" class="' + (isSorted ? 'sorted' : '') + '">';
    hhtml += columns[i].label;
    hhtml += '<span class="sort-icon">' + (isSorted ? (state.sortDir === 'asc' ? '\u25B2' : '\u25BC') : '\u21C5') + '</span>';
    hhtml += '</th>';
  }
  hhtml += '</tr>';
  thead.innerHTML = hhtml;
  thead._columns = columns;

  var tbody = document.getElementById('table-body');
  if (filtered.length === 0) {
    tbody.innerHTML = '<tr><td colspan="' + columns.length + '" class="no-data">No districts match your search</td></tr>';
    return;
  }

  var bhtml = '';
  for (var i = 0; i < filtered.length; i++) {
    var row = filtered[i];
    var orgType = getOrgType(row.Organization);
    var isFarm = row.Organization === 'FARMERSVILLE ISD';
    bhtml += '<tr class="' + (isFarm ? 'org-farmersville' : '') + '">';
    bhtml += '<td class="org-name"><span class="tag tag-' + orgType + '">' + orgType + '</span> ' + row.Organization + '</td>';
    bhtml += '<td class="year-col">' + row.Year + '</td>';

    for (var c = 2; c < columns.length; c++) {
      var key = columns[c].key;
      var val = row[key];
      var isPct = columns[c].type === 'pct';
      var display = '\u2014';
      if (val !== null && val !== undefined) {
        if (isPct) display = val + '%';
        else display = typeof val === 'number' ? val.toLocaleString() : val;
      }
      bhtml += '<td class="' + columns[c].type + '">' + display + '</td>';
    }
    bhtml += '</tr>';
  }
  tbody.innerHTML = bhtml;
}

function updateSummaryBar() {
  var bar = document.getElementById('summary-bar');
  var subject = state.subject;

  var currentYear = '2026';
  var prevYear = '2025';

  var qts = [];

  if (subject === "All Subjects") {
    var currRows = ALL_DATA.filter(function(r) { return r.Year === currentYear; });
    var totalTests = 0;
    for (var i = 0; i < currRows.length; i++) {
      for (var s = 0; s < SUBJECTS.length; s++) {
        var t = currRows[i][SUBJECTS[s] + "|Tests Taken"];
        if (t) totalTests += t;
      }
    }
    var districtCount = ORGS.filter(function(o) { return o !== 'STATE' && o.indexOf('REG') !== 0; }).length;
    qts = [
      { label: 'Total Tests (' + currentYear + ')', value: totalTests.toLocaleString() },
      { label: 'Districts Tracked', value: String(districtCount) },
      { label: 'Subjects', value: String(SUBJECTS.length) },
      { label: 'Years Compared', value: String(YEARS.length) }
    ];
  } else {
    var curr = null;
    var prev = null;
    for (var i = 0; i < ALL_DATA.length; i++) {
      var r = ALL_DATA[i];
      if (r.Organization === 'FARMERSVILLE ISD') {
        if (r.Year === currentYear) curr = r;
        if (r.Year === prevYear) prev = r;
      }
    }
    if (curr) {
      var currScore = curr[subject + "|Average Scale Score"];
      var currAppr = curr[subject + "|Approaches and Above Percentage"];
      var currMeets = curr[subject + "|Meets and Above Percentage"];
      var currTests = curr[subject + "|Tests Taken"];

      qts = [
        { label: 'Farmersville Avg Score ' + currentYear, value: String(currScore || '\u2014') },
        { label: 'Farmersville Appr+ ' + currentYear, value: (currAppr || 0) + '%' },
        { label: 'Farmersville Meets+ ' + currentYear, value: (currMeets || 0) + '%' },
        { label: 'Tests Taken (' + currentYear + ')', value: (currTests || 0).toLocaleString() }
      ];
    }
  }

  bar.innerHTML = qts.map(function(q) {
    return '<div class="summary-card"><div class="value">' + q.value + '</div><div class="label">' + q.label + '</div></div>';
  }).join('');
}

function doSort(data, columns) {
  if (state.sortCol === null) return;
  var col = columns[state.sortCol];
  var key = col.key;
  var dir = state.sortDir === 'asc' ? 1 : -1;

  data.sort(function(a, b) {
    var va, vb;
    if (col.subj && col.metricKey) {
      // Overview mode: need to extract from subjects map
      var sa = a.subjects && a.subjects[col.subj];
      var sb = b.subjects && b.subjects[col.subj];
      var mk = col.metricKey;
      va = sa ? sa[mk] : null;
      vb = sb ? sb[mk] : null;
    } else if (key === 'Organization') {
      va = a['Organization'];
      vb = b['Organization'];
    } else if (key === 'Year') {
      va = a['Year'];
      vb = b['Year'];
    } else {
      va = a[key];
      vb = b[key];
    }

    if (va === null || va === undefined) return 1;
    if (vb === null || vb === undefined) return -1;
    if (typeof va === 'string') return va.localeCompare(vb) * dir;
    return (va - vb) * dir;
  });
}

function updateSortIndicators() {
  var ths = document.querySelectorAll('th');
  for (var i = 0; i < ths.length; i++) {
    var th = ths[i];
    var col = parseInt(th.dataset.col);
    th.classList.toggle('sorted', col === state.sortCol);
  }
}

// === EVENT BINDING ===
document.addEventListener('DOMContentLoaded', function() {
  var subjectSelect = document.getElementById('subject-select');
  var opts = '<option value="All Subjects">All Subjects</option>';
  for (var i = 0; i < SUBJECTS.length; i++) {
    opts += '<option value="' + SUBJECTS[i] + '">' + SUBJECTS[i] + '</option>';
  }
  subjectSelect.innerHTML = opts;
  subjectSelect.value = 'All Subjects';

  var metricSelect = document.getElementById('metric-select');
  var mopts = '';
  for (var i = 0; i < METRIC_LABELS.length; i++) {
    mopts += '<option value="' + i + '">' + METRIC_LABELS[i] + '</option>';
  }
  metricSelect.innerHTML = mopts;
  metricSelect.value = '5';

  subjectSelect.addEventListener('change', function() {
    state.subject = this.value;
    state.sortCol = 1;
    state.sortDir = 'desc';
    render();
  });

  metricSelect.addEventListener('change', function() {
    state.metricIdx = parseInt(this.value);
    render();
  });

  document.getElementById('search-box').addEventListener('input', function() {
    state.search = this.value;
    state.sortCol = null;
    render();
  });

  document.getElementById('table-head').addEventListener('click', function(e) {
    var th = e.target.closest('th');
    if (!th) return;
    var colIdx = parseInt(th.dataset.col);
    if (state.sortCol === colIdx) {
      state.sortDir = state.sortDir === 'asc' ? 'desc' : 'asc';
    } else {
      state.sortCol = colIdx;
      state.sortDir = 'desc';
    }
    render();
  });

  // Initial render
  state.sortCol = 1;
  state.sortDir = 'desc';
  render();
});
</script>
</body>
</html>"""


if __name__ == '__main__':
    main()
