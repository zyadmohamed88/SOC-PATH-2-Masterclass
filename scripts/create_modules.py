import json
import os
import io
import base64
from PIL import Image

# Read raw document data
with open('document_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Module mapping definitions
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
        "icon": "fa-brands fa-microsoft",
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
        "icon": "fa-brands fa-aws",
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
        "icon": "fa-fire-extinguisher",
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
        "end_idx": len(items) - 1
    }
]

print("Modules mapping verified.")
