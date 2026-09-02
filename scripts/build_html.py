import json
import os
import sys

print("Building SOC PATH 2 Masterclass HTML Web Application...")

# Load raw items
with open('document_raw.json', 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Module definitions with index ranges
MODULES = [
    {
        "id": "mod-1",
        "num": "01",
        "title": "Log Analysis & Operations",
        "category": "SIEM & Logs",
        "icon": "fa-file-lines",
        "color": "#3b82f6",
        "desc": "Foundational log collection architecture, syslog configuration, rsyslog log processing, and log parsing operations.",
        "start_idx": 1,
        "end_idx": 57
    },
    {
        "id": "mod-2",
        "num": "02",
        "title": "Advanced Splunk Masterclass",
        "category": "SIEM & Logs",
        "icon": "fa-chart-pie",
        "color": "#ec4899",
        "desc": "Exploring SPL query optimization, SOC lab setup, dashboards, automated alerting, and Splunk data manipulation.",
        "start_idx": 58,
        "end_idx": 154
    },
    {
        "id": "mod-3",
        "num": "03",
        "title": "Advanced ELK Stack & Wazuh Integration",
        "category": "SIEM & Logs",
        "icon": "fa-database",
        "color": "#8b5cf6",
        "desc": "Logstash ingestion pipelines, custom Wazuh alert rule engineering, and Elastic Query Languages (KQL/EQL).",
        "start_idx": 155,
        "end_idx": 262
    },
    {
        "id": "mod-4",
        "num": "04",
        "title": "Detection Engineering & Threat Intelligence",
        "category": "Detection",
        "icon": "fa-shield-halved",
        "color": "#10b981",
        "desc": "Tactical detection methodologies, Threat Intelligence integration, Sigma rules deployment, and foothold hunting.",
        "start_idx": 263,
        "end_idx": 356
    },
    {
        "id": "mod-5",
        "num": "05",
        "title": "Threat Emulation & Red Teaming",
        "category": "Threat Hunting",
        "icon": "fa-crosshairs",
        "color": "#f59e0b",
        "desc": "Adversary emulation frameworks, threat modeling methodologies, and hands-on Atomic Red Team test scenarios.",
        "start_idx": 357,
        "end_idx": 393
    },
    {
        "id": "mod-6",
        "num": "06",
        "title": "Microsoft 365 Security Operations",
        "category": "Cloud",
        "icon": "fa-cloud-shield",
        "color": "#06b6d4",
        "desc": "M365 cloud monitoring, Entra ID (Azure AD) identity tracking, Exchange Online, SharePoint, and Intune compliance audit logs.",
        "start_idx": 394,
        "end_idx": 463
    },
    {
        "id": "mod-7",
        "num": "07",
        "title": "Cloud Security for SOC (AWS)",
        "category": "Cloud",
        "icon": "fa-cloud",
        "color": "#ff9900",
        "desc": "AWS security logging, CloudTrail, VPC Flow Logs, GuardDuty, AWS login monitoring, and cloud workload security.",
        "start_idx": 464,
        "end_idx": 578
    },
    {
        "id": "mod-8",
        "num": "08",
        "title": "Next-Gen Detection Engineering & AI",
        "category": "Detection",
        "icon": "fa-robot",
        "color": "#6366f1",
        "desc": "Modern detection rule lifecycle, Sigma rule syntax mastery, and AI-driven automation in SOC detection pipelines.",
        "start_idx": 579,
        "end_idx": 619
    },
    {
        "id": "mod-9",
        "num": "09",
        "title": "Threat Hunting Fundamentals",
        "category": "Threat Hunting",
        "icon": "fa-magnifying-glass",
        "color": "#14b8a6",
        "desc": "Hypothesis-driven threat hunting, endpoint artifacts, and proactive detection strategies.",
        "start_idx": 620,
        "end_idx": 623
    },
    {
        "id": "mod-10",
        "num": "10",
        "title": "Incident Response Life Cycle (NIST/SANS)",
        "category": "Incident Response",
        "icon": "fa-triangle-exclamation",
        "color": "#ef4444",
        "desc": "NIST IR framework: Preparation, Detection & Analysis, Containment, Eradication, and Post-Incident Root Cause Analysis.",
        "start_idx": 624,
        "end_idx": 643
    },
    {
        "id": "mod-11",
        "num": "11",
        "title": "Cyber Threat Intelligence (CTI)",
        "category": "Intelligence",
        "icon": "fa-brain",
        "color": "#a855f7",
        "desc": "CTI for SOC alert triage, MISP threat sharing platform integration, and OpenCTI knowledge graph analysis.",
        "start_idx": 644,
        "end_idx": 697
    },
    {
        "id": "mod-12",
        "num": "12",
        "title": "Advanced Traffic & Network Analysis",
        "category": "Network",
        "icon": "fa-network-wired",
        "color": "#0284c7",
        "desc": "Network traffic pitfalls, Snort IDS/IPS detection rules, Zeek NSM logs, Zui/Brim threat hunting, and Wireshark PCAP analysis.",
        "start_idx": 698,
        "end_idx": 746
    },
    {
        "id": "mod-13",
        "num": "13",
        "title": "Static Malware Analysis",
        "category": "Malware Analysis",
        "icon": "fa-bug",
        "color": "#d97706",
        "desc": "PE static analysis, PEStudio headers, script analysis (PowerShell/VBS), MalDoc macros, oletools, and CyberChef deobfuscation.",
        "start_idx": 747,
        "end_idx": 891
    },
    {
        "id": "mod-14",
        "num": "14",
        "title": "Wazuh for SOC & GRC Operations",
        "category": "SIEM & Logs",
        "icon": "fa-cubes",
        "color": "#10b981",
        "desc": "Wazuh manager architecture, custom XML decoders and rules, and endpoint visibility using Osquery SQL queries.",
        "start_idx": 892,
        "end_idx": len(raw_items) - 1
    }
]

# Helper to read base64 image from cache
def get_b64(img_file):
    cache_path = os.path.join('b64_cache', img_file + '.b64')
    if os.path.exists(cache_path):
        with open(cache_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

print("Building HTML template content...")

# Build HTML string
html_parts = []
html_parts.append('''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SOC PATH 2 | Enterprise Cyber Security & SOC Operations Blueprint</title>
  <meta name="description" content="Comprehensive Standalone Enterprise SOC Analyst & Detection Engineering Knowledge Base & Lab Manual.">
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    :root {
      --bg-slate: #07090e;
      --bg-surface: rgba(15, 22, 36, 0.7);
      --bg-surface-hover: rgba(26, 38, 61, 0.8);
      --bg-sidebar: #0b0f19;
      --border-color: rgba(255, 255, 255, 0.05);
      --accent-cyan: #00f2fe;
      --accent-blue: #3b82f6;
      --accent-purple: #a855f7;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --radius-xl: 20px;
      --radius-lg: 16px;
      --radius-md: 12px;
      --radius-sm: 8px;
      --shadow-glow: 0 10px 40px -10px rgba(0, 242, 254, 0.15);
      --shadow-card: 0 20px 40px rgba(0, 0, 0, 0.4);
      --glass-blur: blur(20px);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-slate);
      color: var(--text-main);
      overflow-x: hidden;
      line-height: 1.6;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(0, 242, 254, 0.04) 0%, transparent 40%),
        radial-gradient(circle at 85% 75%, rgba(168, 85, 247, 0.04) 0%, transparent 40%);
      background-attachment: fixed;
    }

    /* Scrollbar */
    ::-webkit-scrollbar {
      width: 8px;
      height: 8px;
    }
    ::-webkit-scrollbar-track {
      background: var(--bg-slate);
    }
    ::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.15);
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: rgba(0, 242, 254, 0.4);
    }

    /* App Layout */
    .app-container {
      display: flex;
      min-height: 100vh;
    }

    /* Sidebar */
    .sidebar {
      width: 320px;
      background-color: var(--bg-sidebar);
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      z-index: 100;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .sidebar-header {
      padding: 24px;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .logo-badge {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
      display: flex;
      align-items: center;
      justify-content: center;
      color: #000;
      font-size: 20px;
      font-weight: 800;
      box-shadow: 0 0 20px rgba(0, 242, 254, 0.4);
    }

    .logo-text h1 {
      font-size: 18px;
      font-weight: 800;
      letter-spacing: -0.5px;
      background: linear-gradient(90deg, #fff, var(--text-muted));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .logo-text p {
      font-size: 11px;
      color: var(--accent-cyan);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    /* Sidebar Search & Controls */
    .sidebar-controls {
      padding: 16px 20px;
      border-bottom: 1px solid var(--border-color);
    }

    .search-box {
      position: relative;
      width: 100%;
    }

    .search-box i {
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 14px;
    }

    .search-input {
      width: 100%;
      padding: 10px 14px 10px 38px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      color: #fff;
      font-size: 13px;
      outline: none;
      transition: all 0.2s;
    }

    .search-input:focus {
      background: rgba(255, 255, 255, 0.08);
      border-color: var(--accent-cyan);
      box-shadow: 0 0 15px rgba(0, 242, 254, 0.15);
    }

    /* Category Filter Tabs */
    .category-filters {
      display: flex;
      gap: 6px;
      overflow-x: auto;
      padding: 12px 20px 6px;
      scrollbar-width: none;
    }
    .category-filters::-webkit-scrollbar { display: none; }

    .filter-btn {
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 11px;
      font-weight: 600;
      background: rgba(255, 255, 255, 0.04);
      color: var(--text-muted);
      border: 1px solid transparent;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s;
    }

    .filter-btn.active, .filter-btn:hover {
      background: rgba(0, 242, 254, 0.1);
      color: var(--accent-cyan);
      border-color: rgba(0, 242, 254, 0.3);
    }

    /* Sidebar Navigation List */
    .sidebar-nav {
      flex: 1;
      overflow-y: auto;
      padding: 16px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .nav-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 14px;
      border-radius: var(--radius-md);
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      transition: all 0.2s;
      border: 1px solid transparent;
    }

    .nav-item:hover {
      background: var(--bg-surface-hover);
      color: #fff;
    }

    .nav-item.active {
      background: rgba(0, 242, 254, 0.08);
      color: #fff;
      border-color: rgba(0, 242, 254, 0.2);
    }

    .nav-item-left {
      display: flex;
      align-items: center;
      gap: 12px;
      min-width: 0;
    }

    .nav-num {
      font-size: 11px;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      opacity: 0.7;
      min-width: 20px;
    }

    .nav-title {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    .nav-count {
      font-size: 10px;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-dim);
    }

    /* Main Content Area */
    .main-content {
      margin-left: 320px;
      flex: 1;
      min-width: 0;
      padding: 40px;
      max-width: 1400px;
    }

    /* Hero Header */
    .hero-header {
      background: var(--bg-surface);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-xl);
      padding: 40px;
      margin-bottom: 40px;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-card);
    }

    .hero-header::before {
      content: '';
      position: absolute;
      top: 0;
      right: 0;
      width: 350px;
      height: 350px;
      background: radial-gradient(circle, rgba(0, 242, 254, 0.1) 0%, transparent 70%);
      pointer-events: none;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      border-radius: 20px;
      background: rgba(0, 242, 254, 0.1);
      border: 1px solid rgba(0, 242, 254, 0.3);
      color: var(--accent-cyan);
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 16px;
    }

    .hero-title {
      font-size: 36px;
      font-weight: 800;
      line-height: 1.2;
      letter-spacing: -1px;
      margin-bottom: 14px;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
      font-size: 15px;
      color: var(--text-muted);
      max-width: 850px;
      margin-bottom: 28px;
    }

    /* Stats Grid */
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
    }

    .stat-card {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-color);
      padding: 18px;
      border-radius: var(--radius-lg);
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .stat-icon {
      width: 46px;
      height: 46px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 20px;
    }

    .stat-val {
      font-size: 22px;
      font-weight: 800;
      color: #fff;
    }

    .stat-lbl {
      font-size: 12px;
      color: var(--text-muted);
    }

    /* Progress Tracker Bar */
    .progress-bar-container {
      margin-top: 24px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .progress-text {
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
      white-space: nowrap;
    }

    .progress-track {
      flex: 1;
      height: 8px;
      background: rgba(255, 255, 255, 0.06);
      border-radius: 4px;
      overflow: hidden;
      position: relative;
    }

    .progress-fill {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue));
      border-radius: 4px;
      transition: width 0.4s ease;
    }

    /* Module Section Styling */
    .module-section {
      margin-bottom: 50px;
      scroll-margin-top: 30px;
    }

    .module-card {
      background: var(--bg-surface);
      backdrop-filter: var(--glass-blur);
      -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-xl);
      padding: 36px;
      box-shadow: var(--shadow-card);
      transition: border-color 0.3s;
    }

    .module-card:hover {
      border-color: rgba(255, 255, 255, 0.1);
    }

    .module-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 20px;
      margin-bottom: 24px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--border-color);
    }

    .module-title-wrapper {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .module-icon-badge {
      width: 52px;
      height: 52px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
    }

    .module-meta-title {
      font-size: 24px;
      font-weight: 800;
      color: #fff;
      line-height: 1.3;
    }

    .module-cat-tag {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 4px;
    }

    .module-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .complete-checkbox {
      display: flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--border-color);
      padding: 8px 16px;
      border-radius: 20px;
      cursor: pointer;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      user-select: none;
      transition: all 0.2s;
    }

    .complete-checkbox:hover {
      background: rgba(16, 185, 129, 0.1);
      border-color: rgba(16, 185, 129, 0.3);
      color: var(--accent-emerald);
    }

    .complete-checkbox.checked {
      background: rgba(16, 185, 129, 0.15);
      border-color: var(--accent-emerald);
      color: var(--accent-emerald);
    }

    .module-description {
      font-size: 14px;
      color: var(--text-muted);
      margin-bottom: 28px;
      line-height: 1.7;
    }

    /* Subtopics */
    .subtopic-container {
      margin-top: 24px;
    }

    .subtopic-title {
      font-size: 16px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 16px;
      padding-left: 12px;
      border-left: 3px solid var(--accent-cyan);
    }

    /* Screenshot Image Gallery Grid */
    .image-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 20px;
      margin-bottom: 30px;
    }

    .image-card {
      background: rgba(10, 14, 23, 0.6);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      overflow: hidden;
      position: relative;
      group: relative;
      transition: all 0.3s ease;
    }

    .image-card:hover {
      transform: translateY(-4px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.6);
      border-color: rgba(0, 242, 254, 0.3);
    }

    .image-thumb-wrapper {
      position: relative;
      width: 100%;
      height: 200px;
      background: #000;
      overflow: hidden;
      cursor: pointer;
    }

    .image-thumb-wrapper img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top;
      transition: transform 0.4s ease;
    }

    .image-card:hover .image-thumb-wrapper img {
      transform: scale(1.05);
    }

    .image-overlay {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(7, 9, 14, 0.6);
      backdrop-filter: blur(4px);
      display: flex;
      align-items: center;
      justify-content: center;
      opacity: 0;
      transition: opacity 0.25s ease;
    }

    .image-card:hover .image-overlay {
      opacity: 1;
    }

    .zoom-btn {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent-cyan), var(--accent-blue));
      color: #000;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      cursor: pointer;
      box-shadow: 0 0 20px rgba(0, 242, 254, 0.5);
    }

    .image-card-caption {
      padding: 12px 16px;
      font-size: 12px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-color);
      background: rgba(15, 23, 42, 0.4);
    }

    .fig-num {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--accent-cyan);
    }

    /* Lightbox Modal */
    .lightbox-modal {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(4, 6, 10, 0.92);
      backdrop-filter: blur(25px);
      -webkit-backdrop-filter: blur(25px);
      z-index: 1000;
      display: flex;
      flex-direction: column;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }

    .lightbox-modal.active {
      opacity: 1;
      pointer-events: auto;
    }

    .lightbox-header {
      padding: 20px 30px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid var(--border-color);
      z-index: 10;
    }

    .lightbox-title {
      font-size: 15px;
      font-weight: 700;
      color: #fff;
    }

    .lightbox-controls {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .control-btn {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid var(--border-color);
      color: #fff;
      width: 38px;
      height: 38px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.2s;
    }

    .control-btn:hover {
      background: rgba(0, 242, 254, 0.15);
      border-color: var(--accent-cyan);
      color: var(--accent-cyan);
    }

    .lightbox-body {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      padding: 40px;
    }

    .lightbox-img {
      max-width: 90%;
      max-height: 85vh;
      object-fit: contain;
      border-radius: var(--radius-md);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.8);
      transition: transform 0.2s ease-out;
    }

    .lightbox-nav-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--border-color);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 18px;
      cursor: pointer;
      transition: all 0.2s;
    }

    .lightbox-nav-btn:hover {
      background: var(--accent-cyan);
      color: #000;
      box-shadow: 0 0 20px rgba(0, 242, 254, 0.6);
    }

    .lightbox-prev { left: 30px; }
    .lightbox-next { right: 30px; }

    /* Code Blocks */
    .code-block {
      background: #090d16;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      margin: 16px 0;
      overflow: hidden;
    }

    .code-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 16px;
      background: rgba(255, 255, 255, 0.02);
      border-bottom: 1px solid var(--border-color);
      font-size: 12px;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-dim);
    }

    .copy-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 12px;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: color 0.2s;
    }

    .copy-btn:hover { color: var(--accent-cyan); }

    pre {
      padding: 16px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      color: #e2e8f0;
      overflow-x: auto;
    }

    /* Back to Top Floating Button */
    .back-to-top {
      position: fixed;
      bottom: 30px;
      right: 30px;
      width: 46px;
      height: 46px;
      border-radius: 50%;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid var(--border-color);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
      opacity: 0;
      visibility: hidden;
      transition: all 0.3s;
      z-index: 90;
    }

    .back-to-top.show {
      opacity: 1;
      visibility: visible;
    }

    .back-to-top:hover {
      background: var(--accent-cyan);
      color: #000;
      box-shadow: 0 0 20px rgba(0, 242, 254, 0.5);
    }

    @media (max-width: 1024px) {
      .sidebar {
        transform: translateX(-100%);
      }
      .main-content {
        margin-left: 0;
        padding: 20px;
      }
      .sidebar.open {
        transform: translateX(0);
      }
    }
  </style>
</head>
<body>

<div class="app-container">
  
  <!-- Sidebar Navigation -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <div class="logo-badge"><i class="fa-solid fa-shield-virus"></i></div>
      <div class="logo-text">
        <h1>SOC PATH 2</h1>
        <p>Enterprise SOC Operations</p>
      </div>
    </div>

    <div class="sidebar-controls">
      <div class="search-box">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input type="text" id="searchInput" class="search-input" placeholder="Search modules, tools, logs...">
      </div>
    </div>

    <div class="category-filters">
      <button class="filter-btn active" onclick="filterCategory('All')">All</button>
      <button class="filter-btn" onclick="filterCategory('SIEM & Logs')">SIEM</button>
      <button class="filter-btn" onclick="filterCategory('Detection')">Detection</button>
      <button class="filter-btn" onclick="filterCategory('Cloud')">Cloud</button>
      <button class="filter-btn" onclick="filterCategory('Threat Hunting')">Hunting</button>
      <button class="filter-btn" onclick="filterCategory('Malware Analysis')">Malware</button>
    </div>

    <nav class="sidebar-nav" id="sidebarNav">
''')

# Populate Sidebar Items
for m in MODULES:
    sub_count = m["end_idx"] - m["start_idx"] + 1
    # Count images in module
    mod_imgs = sum(len(raw_items[idx]["imgs"]) for idx in range(m["start_idx"], m["end_idx"] + 1))
    html_parts.append(f'''
      <a href="#{m["id"]}" class="nav-item" data-category="{m["category"]}" onclick="setActiveNav(this)">
        <div class="nav-item-left">
          <span class="nav-num">{m["num"]}</span>
          <span class="nav-title">{m["title"]}</span>
        </div>
        <span class="nav-count">{mod_imgs} Imgs</span>
      </a>
    ''')

html_parts.append('''
    </nav>
  </aside>

  <!-- Main Content Viewport -->
  <main class="main-content">
    
    <!-- Hero Header -->
    <header class="hero-header">
      <div class="hero-badge">
        <i class="fa-solid fa-shield-halved"></i> Enterprise SOC & SIEM Blueprint
      </div>
      <h1 class="hero-title">SOC PATH 2 Masterclass Blueprint</h1>
      <p class="hero-subtitle">
        An interactive, high-fidelity SOC Operations and Detection Engineering technical reference handbook.
        Includes complete hands-on lab evidence, SIEM queries, incident response workflows, and static malware analysis.
      </p>

      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(59, 130, 246, 0.15); color: #3b82f6;">
            <i class="fa-solid fa-layer-group"></i>
          </div>
          <div>
            <div class="stat-val">14</div>
            <div class="stat-lbl">Core SOC Modules</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(16, 185, 129, 0.15); color: #10b981;">
            <i class="fa-solid fa-images"></i>
          </div>
          <div>
            <div class="stat-val">907</div>
            <div class="stat-lbl">Lab Evidence Screenshots</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(168, 85, 247, 0.15); color: #a855f7;">
            <i class="fa-solid fa-terminal"></i>
          </div>
          <div>
            <div class="stat-val">35+</div>
            <div class="stat-lbl">Hands-on Labs</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(245, 158, 11, 0.15); color: #f59e0b;">
            <i class="fa-solid fa-bolt"></i>
          </div>
          <div>
            <div class="stat-val">100%</div>
            <div class="stat-lbl">Standalone Portable</div>
          </div>
        </div>
      </div>

      <!-- Completion Progress Bar -->
      <div class="progress-bar-container">
        <span class="progress-text" id="progressText">0 of 14 Modules Completed (0%)</span>
        <div class="progress-track">
          <div class="progress-fill" id="progressFill"></div>
        </div>
      </div>
    </header>

    <!-- Modules Content Sections -->
''')

# Populate Module Cards & Image Galleries
fig_counter = 1

for m in MODULES:
    html_parts.append(f'''
    <section id="{m["id"]}" class="module-section" data-category="{m["category"]}">
      <div class="module-card">
        
        <div class="module-header">
          <div class="module-title-wrapper">
            <div class="module-icon-badge" style="background: {m["color"]}20; color: {m["color"]};">
              <i class="fa-solid {m["icon"]}"></i>
            </div>
            <div>
              <div class="module-meta-title">{m["num"]}. {m["title"]}</div>
              <span class="module-cat-tag" style="background: {m["color"]}20; color: {m["color"]};">
                {m["category"]}
              </span>
            </div>
          </div>

          <div class="module-actions">
            <label class="complete-checkbox" id="check-label-{m["id"]}">
              <input type="checkbox" onchange="toggleModuleComplete('{m["id"]}')" id="cb-{m["id"]}" style="display:none;">
              <i class="fa-regular fa-square" id="icon-cb-{m["id"]}"></i> Mark Complete
            </label>
          </div>
        </div>

        <p class="module-description">{m["desc"]}</p>
        
        <div class="subtopic-container">
    ''')

    # Extract subtopics and images within module range
    mod_items = raw_items[m["start_idx"]:m["end_idx"] + 1]
    
    current_sub = "Lab Overview & Evidence"
    sub_imgs = []

    for item in mod_items:
        txt = item["text"]
        imgs = item["imgs"]

        if txt:
            # If we had images collected for previous subtopic, render them first
            if sub_imgs:
                html_parts.append('<div class="image-grid">')
                for img_name in sub_imgs:
                    b64_data = get_b64(img_name)
                    html_parts.append(f'''
                      <div class="image-card">
                        <div class="image-thumb-wrapper" onclick="openLightbox('{b64_data}', 'Figure {fig_counter}: {m["title"]} Lab Evidence')">
                          <img src="{b64_data}" alt="Lab Evidence" loading="lazy">
                          <div class="image-overlay">
                            <button class="zoom-btn"><i class="fa-solid fa-expand"></i></button>
                          </div>
                        </div>
                        <div class="image-card-caption">
                          <span class="fig-num">FIG-{fig_counter:03d}</span>
                          <span>{m["num"]} Evidence</span>
                        </div>
                      </div>
                    ''')
                    fig_counter += 1
                html_parts.append('</div>')
                sub_imgs = []

            # Render Subtopic Title
            html_parts.append(f'<div class="subtopic-title"><i class="fa-solid fa-chevron-right" style="font-size:12px; color:{m["color"]};"></i> {txt}</div>')
            current_sub = txt

        for img_name in imgs:
            sub_imgs.append(img_name)

    # Render remaining images
    if sub_imgs:
        html_parts.append('<div class="image-grid">')
        for img_name in sub_imgs:
            b64_data = get_b64(img_name)
            html_parts.append(f'''
              <div class="image-card">
                <div class="image-thumb-wrapper" onclick="openLightbox('{b64_data}', 'Figure {fig_counter}: {m["title"]} Lab Evidence')">
                  <img src="{b64_data}" alt="Lab Evidence" loading="lazy">
                  <div class="image-overlay">
                    <button class="zoom-btn"><i class="fa-solid fa-expand"></i></button>
                  </div>
                </div>
                <div class="image-card-caption">
                  <span class="fig-num">FIG-{fig_counter:03d}</span>
                  <span>{m["num"]} Evidence</span>
                </div>
              </div>
            ''')
            fig_counter += 1
        html_parts.append('</div>')

    html_parts.append('''
        </div>
      </div>
    </section>
    ''')

# Close Main and add Lightbox & Scripts
html_parts.append('''
  </main>
</div>

<!-- Back to Top Button -->
<button class="back-to-top" id="backToTop" onclick="scrollToTop()">
  <i class="fa-solid fa-arrow-up"></i>
</button>

<!-- Lightbox Modal Viewer -->
<div class="lightbox-modal" id="lightboxModal">
  <div class="lightbox-header">
    <div class="lightbox-title" id="lightboxTitle">Lab Evidence Viewer</div>
    <div class="lightbox-controls">
      <button class="control-btn" onclick="zoomIn()"><i class="fa-solid fa-magnifying-glass-plus"></i></button>
      <button class="control-btn" onclick="zoomOut()"><i class="fa-solid fa-magnifying-glass-minus"></i></button>
      <button class="control-btn" onclick="resetZoom()"><i class="fa-solid fa-rotate-left"></i></button>
      <button class="control-btn" onclick="closeLightbox()"><i class="fa-solid fa-xmark"></i></button>
    </div>
  </div>
  <div class="lightbox-body">
    <button class="lightbox-nav-btn lightbox-prev" onclick="prevImage()"><i class="fa-solid fa-chevron-left"></i></button>
    <img id="lightboxImg" class="lightbox-img" src="" alt="Full Resolution Lab Screenshot">
    <button class="lightbox-nav-btn lightbox-next" onclick="nextImage()"><i class="fa-solid fa-chevron-right"></i></button>
  </div>
</div>

<script>
  let completedModules = new Set(JSON.parse(localStorage.getItem('completedModules') || '[]'));
  let currentZoom = 1;
  let allImages = [];
  let currentImageIdx = 0;

  // Initialize
  document.addEventListener('DOMContentLoaded', () => {
    updateProgress();
    collectAllImages();
    
    // Back to top scroll listener
    window.addEventListener('scroll', () => {
      const btt = document.getElementById('backToTop');
      if (window.scrollY > 400) {
        btt.classList.add('show');
      } else {
        btt.classList.remove('show');
      }
    });

    // Global Search listener
    document.getElementById('searchInput').addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const sections = document.querySelectorAll('.module-section');
      sections.forEach(sec => {
        const text = sec.innerText.toLowerCase();
        if (text.includes(q)) {
          sec.style.display = 'block';
        } else {
          sec.style.display = 'none';
        }
      });
    });

    // Keyboard navigation for Lightbox
    document.addEventListener('keydown', (e) => {
      const modal = document.getElementById('lightboxModal');
      if (modal.classList.contains('active')) {
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowRight') nextImage();
        if (e.key === 'ArrowLeft') prevImage();
      }
    });
  });

  function collectAllImages() {
    const thumbs = document.querySelectorAll('.image-thumb-wrapper img');
    allImages = Array.from(thumbs).map(img => img.src);
  }

  // Toggle Module Completion
  function toggleModuleComplete(modId) {
    const cb = document.getElementById('cb-' + modId);
    const label = document.getElementById('check-label-' + modId);
    const icon = document.getElementById('icon-cb-' + modId);

    if (cb.checked) {
      completedModules.add(modId);
      label.classList.add('checked');
      icon.className = 'fa-solid fa-square-check';
    } else {
      completedModules.delete(modId);
      label.classList.remove('checked');
      icon.className = 'fa-regular fa-square';
    }

    localStorage.setItem('completedModules', JSON.stringify(Array.from(completedModules)));
    updateProgress();
  }

  function updateProgress() {
    const total = 14;
    const count = completedModules.size;
    const pct = Math.round((count / total) * 100);

    // Apply checked state to elements
    completedModules.forEach(id => {
      const cb = document.getElementById('cb-' + id);
      const label = document.getElementById('check-label-' + id);
      const icon = document.getElementById('icon-cb-' + id);
      if (cb) {
        cb.checked = true;
        label.classList.add('checked');
        icon.className = 'fa-solid fa-square-check';
      }
    });

    document.getElementById('progressText').innerText = `${count} of ${total} Modules Completed (${pct}%)`;
    document.getElementById('progressFill').style.width = pct + '%';
  }

  // Category Filtering
  function filterCategory(cat) {
    document.querySelectorAll('.filter-btn').forEach(btn => {
      if (btn.innerText.trim() === cat) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });

    const sections = document.querySelectorAll('.module-section');
    const navItems = document.querySelectorAll('.nav-item');

    sections.forEach(sec => {
      const secCat = sec.getAttribute('data-category');
      if (cat === 'All' || secCat === cat) {
        sec.style.display = 'block';
      } else {
        sec.style.display = 'none';
      }
    });

    navItems.forEach(item => {
      const itemCat = item.getAttribute('data-category');
      if (cat === 'All' || itemCat === cat) {
        item.style.display = 'flex';
      } else {
        item.style.display = 'none';
      }
    });
  }

  function setActiveNav(el) {
    document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
    el.classList.add('active');
  }

  // Lightbox Modal Functions
  function openLightbox(src, title) {
    const modal = document.getElementById('lightboxModal');
    const img = document.getElementById('lightboxImg');
    const titleEl = document.getElementById('lightboxTitle');

    currentImageIdx = allImages.indexOf(src);
    img.src = src;
    titleEl.innerText = title || `Lab Evidence (${currentImageIdx + 1}/${allImages.length})`;
    currentZoom = 1;
    img.style.transform = `scale(${currentZoom})`;

    modal.classList.add('active');
  }

  function closeLightbox() {
    document.getElementById('lightboxModal').classList.remove('active');
  }

  function zoomIn() {
    currentZoom += 0.25;
    document.getElementById('lightboxImg').style.transform = `scale(${currentZoom})`;
  }

  function zoomOut() {
    if (currentZoom > 0.5) {
      currentZoom -= 0.25;
      document.getElementById('lightboxImg').style.transform = `scale(${currentZoom})`;
    }
  }

  function resetZoom() {
    currentZoom = 1;
    document.getElementById('lightboxImg').style.transform = `scale(${currentZoom})`;
  }

  function nextImage() {
    if (currentImageIdx < allImages.length - 1) {
      currentImageIdx++;
      openLightbox(allImages[currentImageIdx], `Lab Evidence (${currentImageIdx + 1}/${allImages.length})`);
    }
  }

  function prevImage() {
    if (currentImageIdx > 0) {
      currentImageIdx--;
      openLightbox(allImages[currentImageIdx], `Lab Evidence (${currentImageIdx + 1}/${allImages.length})`);
    }
  }

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }
</script>

</body>
</html>
''')

# Write complete standalone HTML file
output_html_path = 'SOC_PATH_2_Masterclass.html'
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(''.join(html_parts))

print(f"Successfully generated standalone HTML: {output_html_path}")

# Copy to index.html as well
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(''.join(html_parts))

print("Successfully updated index.html!")
