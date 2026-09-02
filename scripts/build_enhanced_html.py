import json
import os
import sys

print("Building THE MOST ADVANCED AAA-GRADE CYBER SOC WEB APPLICATION (Zyad Elsheshtawy Signature)...")

# Load raw items
with open('scripts/document_raw.json', 'r', encoding='utf-8') as f:
    raw_items = json.load(f)

# Helper to load cached base64 WebP image
def get_b64(img_file):
    cache_path = os.path.join('b64_cache', img_file + '.b64')
    if os.path.exists(cache_path):
        with open(cache_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

MODULES = [
    {
        "id": "mod-1",
        "num": "01",
        "title": "Log Analysis & Operations",
        "category": "SIEM & Logs",
        "icon": "fa-file-lines",
        "color": "#00f2fe",
        "start_idx": 1,
        "end_idx": 57,
        "summary": "Foundational Log Analysis architecture, Syslog RFC 5424 protocol specifications, rsyslog log processing pipelines, and log parsing operations.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Syslog Architecture:</strong> Separation of message generation, transport, and storage under RFC 5424. Facilities (0-23) & Severities (0-7, Emergency to Debug).</li>
              <li><strong>rsyslog Pipeline:</strong> Linux daemon supporting high-performance inputs (imuxsock, imudp, imtcp), custom filters, and log templates.</li>
              <li><strong>Log Normalization:</strong> Converting unstructured log streams into standardized JSON key-value pairs for SIEM ingestion.</li>
              <li><strong>SOC Analyst SOP:</strong> Validate log source heartbeats, verify NTP time sync, and audit for daemon tampering or log drop gaps.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> rsyslog.conf Pipeline Configuration</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Forward auth logs to central SIEM via encrypted TCP
authpriv.* @@192.168.1.100:514

# Syntax check rsyslog config
rsyslogd -N1

# Filter auth.log for failed SSH login spikes
grep "Failed password" /var/log/auth.log | awk '{print $1,$2,$3,$9,$11}' | sort | uniq -c | sort -nr</pre>
          </div>
        """
    },
    {
        "id": "mod-2",
        "num": "02",
        "title": "Advanced Splunk Masterclass",
        "category": "SIEM & Logs",
        "icon": "fa-chart-pie",
        "color": "#ec4899",
        "start_idx": 58,
        "end_idx": 154,
        "summary": "Mastering Splunk Enterprise for security monitoring, Search Processing Language (SPL) optimization, SOC lab deployment, automated correlation alerting, and data transformation.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Indexing Pipeline:</strong> Parsing, indexing, and search processing. Event field extraction at index-time vs search-time.</li>
              <li><strong>SPL Mastery:</strong> Advanced use of <code>stats</code>, <code>eval</code>, <code>transaction</code>, <code>lookup</code>, <code>rex</code>, and <code>timechart</code>.</li>
              <li><strong>Alert Engineering:</strong> Defining trigger thresholds, suppressed duplicates, throttle logic, and webhook escalations.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> SPL Threat Detection Queries</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Detect Failed Login Spikes (EventCode 4625)
index=winlogbeat EventCode=4625
| stats count by TargetUserName, WorkstationName, src_ip
| where count > 10
| sort - count

# Extract PowerShell Encoded Commands
index=main sourcetype="XmlWinEventLog:Microsoft-Windows-PowerShell/Operational" EventCode=4104
| rex field=Message "-e(ncodedcommand)?\\s+(?<encoded_cmd>[A-Za-z0-9+/=]+)"
| stats count by Computer, User, encoded_cmd</pre>
          </div>
        """
    },
    {
        "id": "mod-3",
        "num": "03",
        "title": "Advanced ELK Stack & Wazuh Integration",
        "category": "SIEM & Logs",
        "icon": "fa-database",
        "color": "#a855f7",
        "start_idx": 155,
        "end_idx": 262,
        "summary": "Building enterprise open-source SIEM infrastructure with Elasticsearch, Logstash, Kibana, Beats, and custom Wazuh detection rules.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Logstash Ingestion Pipeline:</strong> Input -> Filter (grok, mutate, date, geoip) -> Output to Elasticsearch indices.</li>
              <li><strong>Wazuh Rule Engine:</strong> XML decoders extract raw log fields into normalized key-values; XML rules evaluate match logic and severity levels (1-15).</li>
              <li><strong>EQL (Event Query Language):</strong> Expressing event correlations across process creation, network connection, and file telemetry.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> Custom Wazuh Rule Definition (XML)</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre>&lt;group name="sysmon,powershell,"&gt;
  &lt;rule id="100050" level="12"&gt;
    &lt;if_sid&gt;61600&lt;/if_sid&gt;
    &lt;field name="scriptBlockText" regex="(?i)DownloadString|Invoke-Expression|IEX"&gt;scriptBlockText&lt;/field&gt;
    &lt;description&gt;Wazuh Alert: Suspicious In-Memory PowerShell Execution Detected&lt;/description&gt;
    &lt;mitre&gt;&lt;id&gt;T1059.001&lt;/id&gt;&lt;/mitre&gt;
  &lt;/rule&gt;
&lt;/group&gt;</pre>
          </div>
        """
    },
    {
        "id": "mod-4",
        "num": "04",
        "title": "Detection Engineering & Threat Intelligence",
        "category": "Detection",
        "icon": "fa-shield-halved",
        "color": "#10b981",
        "start_idx": 263,
        "end_idx": 356,
        "summary": "Proactive detection rule engineering, converting Threat Intelligence (IOCs/TTPs) into Sigma rules, and hunting for initial foothold mechanics.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Detection Lifecycle:</strong> Threat Model -> Hypothesis -> Telemetry Validation -> Rule Development -> Tuning.</li>
              <li><strong>Pyramid of Pain:</strong> Focus detections on TTPs (Top of Pyramid) rather than volatile IP addresses or File Hashes.</li>
              <li><strong>Sigma Standard:</strong> Vendor-agnostic detection format translating into SPL, KQL, Elastic EQL, and QRadar AQL.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> Sigma Rule Standard (YAML)</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre>title: Suspicious Certutil Download
id: e4b6d05f-7e2b-4d3a-b850-9c1234567890
status: test
description: Detects certutil.exe used to download files from remote servers
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith: '\\certutil.exe'
        CommandLine|contains:
            - '-urlcache'
            - '-f'
            - 'http'
    condition: selection
falsepositives: Unknown administrative scripts
level: high</pre>
          </div>
        """
    },
    {
        "id": "mod-5",
        "num": "05",
        "title": "Threat Emulation & Red Teaming",
        "category": "Threat Hunting",
        "icon": "fa-crosshairs",
        "color": "#f59e0b",
        "start_idx": 357,
        "end_idx": 393,
        "summary": "Validating SOC detection coverage through controlled adversary emulation, threat modeling, and Atomic Red Team test execution.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Adversary Emulation:</strong> Simulating real-world threat actor behaviors to test telemetry visibility and SOC alert triggers.</li>
              <li><strong>Atomic Red Team:</strong> Modular library of specific technique tests mapped directly to MITRE ATT&CK.</li>
              <li><strong>Purple Teaming:</strong> Collaborative execution where Red Team triggers atomic tests while Blue Team monitors telemetry streams.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> Invoke-AtomicTest Execution Commands</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Run Atomic Test T1053.005 (Scheduled Task Creation)
Invoke-AtomicTest T1053.005 -TestNumbers 1

# Check prerequisite dependencies before execution
Invoke-AtomicTest T1003.001 -CheckPrereqs

# Clean up atomic test artifacts after testing
Invoke-AtomicTest T1053.005 -Cleanup</pre>
          </div>
        """
    },
    {
        "id": "mod-6",
        "num": "06",
        "title": "Microsoft 365 Security Operations",
        "category": "Cloud",
        "icon": "fa-cloud-shield",
        "color": "#06b6d4",
        "start_idx": 394,
        "end_idx": 463,
        "summary": "Monitoring Microsoft 365 cloud ecosystems, Unified Audit Logs (UAL), Entra ID identity anomalies, Exchange Online email security, and Intune device telemetry.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Unified Audit Log (UAL):</strong> Centralized log repository recording actions across Azure AD, Exchange, SharePoint, OneDrive, and Teams.</li>
              <li><strong>Entra ID Identity Threats:</strong> Impossible travel sign-ins, password spray attacks, MFA exhaustion, service principal secret additions.</li>
              <li><strong>Exchange Online Threats:</strong> Malicious inbox forwarding rules (`New-InboxRule`), transport rule modifications, abnormal `MailItemsAccessed` events.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> EXO PowerShell Audit Commands</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Search Unified Audit Log for Inbox Forwarding Rule Creation
Search-UnifiedAuditLog -StartDate (Get-Date).AddDays(-7) -EndDate (Get-Date) -Operations "New-InboxRule","Set-InboxRule" | Format-Table UserIds, Operations, AuditData

# Inspect Entra ID Risky Users via Graph PowerShell
Get-MgRiskDetections -Filter "riskState eq 'atRisk'" | Select-Object UserPrincipalName, RiskEventType, RiskLevel, CreatedDateTime</pre>
          </div>
        """
    },
    {
        "id": "mod-7",
        "num": "07",
        "title": "Cloud Security for SOC (AWS)",
        "category": "Cloud",
        "icon": "fa-brands fa-aws",
        "color": "#ff9900",
        "start_idx": 464,
        "end_idx": 578,
        "summary": "AWS Cloud Security operations, CloudTrail API management, VPC Flow Log network telemetry, GuardDuty threat detection, and AWS login monitoring.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>AWS CloudTrail:</strong> Audits all API calls made in an AWS account. Critical fields: `eventName`, `userIdentity`, `sourceIPAddress`, `errorCode`.</li>
              <li><strong>VPC Flow Logs:</strong> Captures IP traffic flow to/from network interfaces. Key fields: `action` (ACCEPT/REJECT), `srcaddr`, `dstaddr`.</li>
              <li><strong>AWS Threat Indicators:</strong> `ConsoleLogin` without MFA, `CreateUser` / `AttachUserPolicy`, S3 bucket policy changes (`PutBucketPolicy`).</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> AWS CLI Security Investigation Queries</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Lookup CloudTrail events for IAM User creation
aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=CreateUser

# Query CloudWatch Logs via CloudWatch Insights for Failed AWS Console Logins
fields @timestamp, sourceIPAddress, errorMessage
| filter eventName = 'ConsoleLogin' and responseElements.ConsoleLogin = 'Failure'
| stats count() by sourceIPAddress, errorMessage</pre>
          </div>
        """
    },
    {
        "id": "mod-8",
        "num": "08",
        "title": "Next-Gen Detection Engineering & AI",
        "category": "Detection",
        "icon": "fa-robot",
        "color": "#6366f1",
        "start_idx": 579,
        "end_idx": 619,
        "summary": "Modern detection rule optimization, advanced Sigma language syntax, automated rule testing pipelines, and AI-assisted alert triage.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Detection as Code (DaC):</strong> Managing security rules in Git repositories with automated CI/CD testing and deployment to SIEM.</li>
              <li><strong>AI Alert Enrichment:</strong> Utilizing Large Language Models (LLMs) to generate initial alert summaries and extract IOCs automatically.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> Sigmac Rule Conversion CLI</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Convert Sigma rule to Splunk SPL
sigma convert -t splunk -p sysmon rule.yml

# Convert Sigma rule to Elastic Query Language (EQL)
sigma convert -t eql rule.yml</pre>
          </div>
        """
    },
    {
        "id": "mod-9",
        "num": "09",
        "title": "Threat Hunting Fundamentals",
        "category": "Threat Hunting",
        "icon": "fa-magnifying-glass",
        "color": "#14b8a6",
        "start_idx": 620,
        "end_idx": 623,
        "summary": "Proactive hypothesis-driven threat hunting methodologies to identify stealthy adversaries evading automated SIEM alerts.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Hunting Loop:</strong> Formulate Hypothesis -> Identify Telemetry -> Execute Analytical Queries -> Identify Anomalies -> Document Findings.</li>
              <li><strong>Baseline Analytics:</strong> Stacking frequencies (rare process names, unusual parent-child process pairs, uncommon user agents).</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> Frequency Stacking Query Example</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Find rare parent-child process combinations
index=sysmon EventCode=1
| stats count by ParentImage, Image
| sort + count
| head 20</pre>
          </div>
        """
    },
    {
        "id": "mod-10",
        "num": "10",
        "title": "Incident Response Life Cycle (NIST/SANS)",
        "category": "Incident Response",
        "icon": "fa-triangle-exclamation",
        "color": "#ef4444",
        "start_idx": 624,
        "end_idx": 643,
        "summary": "End-to-end Incident Response operations based on NIST SP 800-61 and SANS frameworks: Preparation, Detection, Containment, Eradication, Recovery, and Post-Incident RCA.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>1. Preparation:</strong> Tooling deployment, communication channels, SOC playbooks, access permissions.</li>
              <li><strong>2. Detection & Analysis:</strong> Triage alerts, determine attack scope, establish timeline of events.</li>
              <li><strong>3. Containment:</strong> Short-term isolation (disconnecting host from network) & long-term containment.</li>
              <li><strong>4. Eradication & Recovery:</strong> Removing malware artifacts, restoring systems from clean backups.</li>
              <li><strong>5. Post-Incident Activity:</strong> Formal Root Cause Analysis (RCA) report and updating SOC playbooks.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> Linux Host Emergency Containment Commands</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Isolate host at firewall layer while keeping loopback open
iptables -F
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A INPUT -s 192.168.1.50 -j ACCEPT # Allow SOC Analyst IP
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP</pre>
          </div>
        """
    },
    {
        "id": "mod-11",
        "num": "11",
        "title": "Cyber Threat Intelligence (CTI)",
        "category": "Intelligence",
        "icon": "fa-brain",
        "color": "#a855f7",
        "start_idx": 644,
        "end_idx": 697,
        "summary": "Operationalizing Cyber Threat Intelligence for alert triage, threat sharing with MISP, and adversary landscape modeling in OpenCTI.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>CTI Tiers:</strong> Strategic, Operational, Tactical, and Technical.</li>
              <li><strong>MISP:</strong> Open-source platform for sharing threat indicators, malware samples, and event attributes.</li>
              <li><strong>OpenCTI:</strong> Enterprise knowledge graph architecture utilizing STIX2 data models to visualize adversary infrastructure.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> MISP PyMISP Python API Automation</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre>from pymisp import PyMISP

misp = PyMISP('https://misp.local', 'YOUR_API_KEY', ssl=False)
result = misp.search(controller='attributes', value='192.168.50.100')
print(result)</pre>
          </div>
        """
    },
    {
        "id": "mod-12",
        "num": "12",
        "title": "Advanced Traffic & Network Analysis",
        "category": "Network",
        "icon": "fa-network-wired",
        "color": "#0284c7",
        "start_idx": 698,
        "end_idx": 746,
        "summary": "Deep Network Security Monitoring (NSM), authoring Snort IDS/IPS detection rules, analyzing Zeek transaction logs, Zui/Brim PCAP threat hunting, and Wireshark inspection.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Snort IDS Rules:</strong> Header and Option Body syntax.</li>
              <li><strong>Zeek NSM Logs:</strong> Structured behavioral network logs (`conn.log`, `dns.log`, `http.log`, `ssl.log`).</li>
              <li><strong>Wireshark & Zui:</strong> Following TCP Streams, inspecting TLS handshake SNI headers, extracting transferred HTTP binaries.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> Custom Snort IDS Rule & Zeek Queries</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Snort Rule: Detect Webshell HTTP POST Request
alert tcp $EXTERNAL_NET any -> $HOME_NET $HTTP_PORTS (msg:"SOC ALERT - Webshell Upload Command"; flow:established,to_server; content:"POST"; http_method; content:"cmd="; http_client_body; classtype:web-application-attack; sid:1000088; rev:1;)

# Zeek Cut: Extract Top Requested DNS Queries
zeek-cut query < dns.log | sort | uniq -c | sort -nr | head -15</pre>
          </div>
        """
    },
    {
        "id": "mod-13",
        "num": "13",
        "title": "Static Malware Analysis",
        "category": "Malware Analysis",
        "icon": "fa-bug",
        "color": "#d97706",
        "start_idx": 747,
        "end_idx": 891,
        "summary": "Triage & static analysis of suspicious executables, PEStudio headers, script deobfuscation (PowerShell/VBScript), MalDoc macros, oletools, and CyberChef recipe pipelines.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Basic Static Analysis:</strong> File Hashing (MD5, SHA256, SSDEEP), PE File Headers, PEStudio import inspections.</li>
              <li><strong>Script Static Analysis:</strong> Deobfuscating PowerShell `-EncodedCommand` base64 strings, VBScript `Execute`/`Eval`.</li>
              <li><strong>MalDoc Analysis:</strong> Inspecting Microsoft Office documents for auto-executing macros using `olevba` and `rtfobj`.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> Static Malware Triage CLI Tools</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre># Calculate Hashes & Fuzzy SSDEEP Hash
sha256sum sample.exe
ssdeep sample.exe > sample.ssdeep

# Analyze MalDoc VBA Macros with olevba
olevba --analyse malicious_doc.docm

# Extract embedded OLE objects & payloads
rtfobj -s all suspicious_file.rtf</pre>
          </div>
        """
    },
    {
        "id": "mod-14",
        "num": "14",
        "title": "Wazuh for SOC & GRC Operations",
        "category": "SIEM & Logs",
        "icon": "fa-cubes",
        "color": "#10b981",
        "start_idx": 892,
        "end_idx": len(raw_items) - 1,
        "summary": "Wazuh XDR/SIEM architecture, custom XML decoders, threat detection rules, regulatory GRC compliance auditing, and endpoint query visibility with Osquery.",
        "theory": """
          <div class="theory-box">
            <h4><i class="fa-solid fa-microchip"></i> Architectural Concepts & SOC Operations</h4>
            <ul>
              <li><strong>Wazuh Decoders:</strong> Extracting custom regex groups to map raw log strings into Wazuh event fields.</li>
              <li><strong>GRC Compliance Mapping:</strong> Wazuh automatically tags alerts against PCI-DSS, NIST 800-53, TSC, and CIS Benchmarks.</li>
              <li><strong>Osquery SQL Engine:</strong> Querying operating system state as a relational database to inspect processes and ports.</li>
            </ul>
          </div>
        """,
        "commands": """
          <div class="code-block">
            <div class="code-header">
              <div class="window-dots"><span class="dot red"></span><span class="dot yellow"></span><span class="dot green"></span></div>
              <span class="code-title"><i class="fa-solid fa-terminal"></i> Osquery SQL Queries & Wazuh CLI</span>
              <button class="copy-btn" onclick="copyCode(this)"><i class="fa-regular fa-copy"></i> Copy Code</button>
            </div>
            <pre>-- Osquery: Find processes listening on network ports without binary on disk
SELECT p.name, p.pid, p.path, l.port, l.protocol 
FROM listening_ports l 
JOIN processes p ON l.pid = p.pid 
WHERE p.on_disk = 0;

# Test custom Wazuh log parsing with wazuh-logtest
/var/ossec/bin/wazuh-logtest</pre>
          </div>
        """
    }
]

html_parts = []
html_parts.append('''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SOC PATH 2 | Zyad Elsheshtawy Blueprint</title>
  <meta name="description" content="Enterprise Cyber Security Operations Center (SOC) Masterclass & Interactive Lab Evidence Platform - Authored by Zyad Elsheshtawy.">
  
  <!-- Premium Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    :root {
      --bg-void: #020408;
      --bg-slate: #060912;
      --bg-card: rgba(10, 16, 28, 0.85);
      --bg-sidebar: #040710;
      
      --neon-cyan: #00f2fe;
      --neon-blue: #3b82f6;
      --neon-purple: #9d4edd;
      --neon-emerald: #10b981;
      --neon-amber: #f59e0b;
      --neon-rose: #ff0055;
      
      --text-glow: #ffffff;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #475569;
      
      --border-glow: rgba(0, 242, 254, 0.25);
      --border-subtle: rgba(255, 255, 255, 0.07);
      
      --radius-2xl: 24px;
      --radius-xl: 18px;
      --radius-lg: 14px;
      --radius-md: 10px;
      
      --shadow-cyber: 0 0 40px rgba(0, 242, 254, 0.18), 0 25px 60px rgba(0, 0, 0, 0.85);
      --glass-blur: blur(28px);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-void);
      color: var(--text-main);
      overflow-x: hidden;
      line-height: 1.6;
      position: relative;
    }

    /* Magnetic Interactive Cyber Canvas */
    #cyberCanvas {
      position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none; z-index: 0; opacity: 0.55;
    }

    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: var(--bg-void); }
    ::-webkit-scrollbar-thumb { background: rgba(0, 242, 254, 0.35); border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: var(--neon-cyan); box-shadow: 0 0 15px var(--neon-cyan); }

    .app-container { display: flex; min-height: 100vh; position: relative; z-index: 1; }

    /* Sidebar Navigation with Big Zyad Elsheshtawy Branding */
    .sidebar {
      width: 340px; background: var(--bg-sidebar); border-right: 1px solid var(--border-subtle);
      display: flex; flex-direction: column; position: fixed; top: 0; bottom: 0; left: 0; z-index: 100;
      box-shadow: 15px 0 45px rgba(0,0,0,0.85); transition: transform 0.3s;
    }

    .sidebar-header {
      padding: 30px 24px; border-bottom: 1px solid var(--border-subtle);
      display: flex; flex-direction: column; gap: 14px;
      background: linear-gradient(180deg, rgba(0, 242, 254, 0.06) 0%, transparent 100%);
    }

    .brand-author-card {
      display: flex; align-items: center; gap: 14px;
    }

    .brand-avatar {
      width: 52px; height: 52px; border-radius: 16px;
      background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
      display: flex; align-items: center; justify-content: center;
      color: #000; font-size: 24px; font-weight: 900;
      box-shadow: 0 0 30px rgba(0, 242, 254, 0.6);
    }

    .brand-info h1 {
      font-size: 19px; font-weight: 900; letter-spacing: -0.5px;
      background: linear-gradient(90deg, #ffffff, var(--neon-cyan), #ffffff);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      line-height: 1.2;
    }

    .brand-info p {
      font-size: 11px; color: var(--neon-cyan); font-weight: 800;
      text-transform: uppercase; letter-spacing: 1.5px; margin-top: 2px;
    }

    .sidebar-controls { padding: 18px 20px; border-bottom: 1px solid var(--border-subtle); }
    .search-box { position: relative; width: 100%; }
    .search-box i { position: absolute; left: 14px; top: 50%; transform: translateY(-50%); color: var(--text-dim); font-size: 14px; }
    .search-input {
      width: 100%; padding: 11px 14px 11px 40px;
      background: rgba(255, 255, 255, 0.03); border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md); color: #fff; font-size: 13px; outline: none;
      transition: all 0.3s;
    }
    .search-input:focus {
      background: rgba(0, 242, 254, 0.05); border-color: var(--neon-cyan);
      box-shadow: 0 0 20px rgba(0, 242, 254, 0.25);
    }

    .category-filters { display: flex; gap: 6px; overflow-x: auto; padding: 12px 20px 6px; scrollbar-width: none; }
    .category-filters::-webkit-scrollbar { display: none; }
    .filter-btn {
      padding: 6px 14px; border-radius: 20px; font-size: 11px; font-weight: 700;
      background: rgba(255, 255, 255, 0.03); color: var(--text-muted); border: 1px solid transparent;
      cursor: pointer; white-space: nowrap; transition: all 0.25s;
    }
    .filter-btn.active, .filter-btn:hover {
      background: rgba(0, 242, 254, 0.12); color: var(--neon-cyan); border-color: rgba(0, 242, 254, 0.4);
      box-shadow: 0 0 15px rgba(0, 242, 254, 0.2);
    }

    .sidebar-nav { flex: 1; overflow-y: auto; padding: 16px; display: flex; flex-direction: column; gap: 6px; }
    .nav-item {
      display: flex; align-items: center; justify-content: space-between;
      padding: 12px 14px; border-radius: var(--radius-md); color: var(--text-muted);
      text-decoration: none; font-size: 13.5px; font-weight: 600; transition: all 0.25s; border: 1px solid transparent;
    }
    .nav-item:hover { background: rgba(255, 255, 255, 0.04); color: #fff; transform: translateX(3px); }
    .nav-item.active { background: rgba(0, 242, 254, 0.08); color: #fff; border-color: rgba(0, 242, 254, 0.3); box-shadow: 0 0 15px rgba(0, 242, 254, 0.1); }
    .nav-item-left { display: flex; align-items: center; gap: 12px; min-width: 0; }
    .nav-num { font-size: 11px; font-weight: 800; font-family: 'JetBrains Mono', monospace; color: var(--neon-cyan); }
    .nav-title { white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
    .nav-count { font-size: 10px; font-weight: 800; padding: 2px 8px; border-radius: 10px; background: rgba(255, 255, 255, 0.05); color: var(--text-dim); }

    /* Main Viewport */
    .main-content {
      margin-left: 340px; flex: 1; min-width: 0; padding: 48px; max-width: 1280px;
    }

    /* Master Author Banner Hero Section */
    .hero-header {
      background: var(--bg-card); backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border-glow); border-radius: var(--radius-2xl);
      padding: 52px; margin-bottom: 48px; position: relative; overflow: hidden; box-shadow: var(--shadow-cyber);
    }
    .hero-header::after {
      content: ''; position: absolute; top: -50%; right: -20%; width: 600px; height: 600px;
      background: radial-gradient(circle, rgba(0, 242, 254, 0.15) 0%, rgba(157, 78, 221, 0.08) 50%, transparent 70%);
      pointer-events: none;
    }

    /* PROMINENT AUTHOR SIGNATURE BOX */
    .author-signature-hero {
      display: flex; align-items: center; gap: 20px; padding: 20px 26px;
      background: linear-gradient(135deg, rgba(0, 242, 254, 0.1) 0%, rgba(157, 78, 221, 0.08) 100%);
      border: 1px solid rgba(0, 242, 254, 0.4); border-radius: var(--radius-xl);
      margin-bottom: 30px; box-shadow: 0 0 30px rgba(0, 242, 254, 0.2);
    }
    .author-signature-avatar {
      width: 64px; height: 64px; border-radius: 18px;
      background: linear-gradient(135deg, var(--neon-cyan), var(--neon-purple));
      display: flex; align-items: center; justify-content: center;
      font-size: 28px; color: #000; font-weight: 900; box-shadow: 0 0 25px var(--neon-cyan);
    }
    .author-signature-text { display: flex; flex-direction: column; gap: 4px; }
    .author-signature-tag { font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 2px; color: var(--neon-cyan); }
    .author-signature-name { font-size: 28px; font-weight: 900; letter-spacing: -0.5px; color: #ffffff; text-shadow: 0 0 20px rgba(0, 242, 254, 0.5); }
    .author-signature-role { font-size: 13px; color: var(--text-muted); font-weight: 600; }

    .hero-title {
      font-size: 44px; font-weight: 900; line-height: 1.18; letter-spacing: -1px; margin-bottom: 18px;
      background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, var(--neon-cyan) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }

    .hero-subtitle { font-size: 16.5px; color: var(--text-muted); max-width: 900px; margin-bottom: 36px; line-height: 1.75; }

    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; }
    .stat-card {
      background: rgba(255, 255, 255, 0.02); border: 1px solid var(--border-subtle); padding: 24px;
      border-radius: var(--radius-xl); display: flex; align-items: center; gap: 20px; transition: all 0.3s ease;
    }
    .stat-card:hover { transform: translateY(-4px); border-color: rgba(0, 242, 254, 0.4); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5); }
    .stat-icon { width: 54px; height: 54px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 24px; }
    .stat-val { font-size: 26px; font-weight: 900; color: #fff; }
    .stat-lbl { font-size: 12.5px; color: var(--text-muted); font-weight: 600; }

    .progress-bar-container {
      margin-top: 32px; background: rgba(255, 255, 255, 0.02); border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg); padding: 20px 26px; display: flex; align-items: center; gap: 26px;
    }
    .progress-text { font-size: 14px; font-weight: 800; color: var(--text-main); white-space: nowrap; }
    .progress-track { flex: 1; height: 10px; background: rgba(255, 255, 255, 0.06); border-radius: 5px; overflow: hidden; }
    .progress-fill { height: 100%; width: 0%; background: linear-gradient(90deg, var(--neon-cyan), var(--neon-purple)); box-shadow: 0 0 20px var(--neon-cyan); transition: width 0.5s ease; }

    /* Module Section Styling */
    .module-section { margin-bottom: 48px; scroll-margin-top: 40px; }
    .module-card {
      background: var(--bg-card); backdrop-filter: var(--glass-blur); -webkit-backdrop-filter: var(--glass-blur);
      border: 1px solid var(--border-subtle); border-radius: var(--radius-2xl); padding: 38px;
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5); transition: all 0.3s;
    }
    .module-card:hover { border-color: rgba(0, 242, 254, 0.35); box-shadow: var(--shadow-cyber); }

    .module-header {
      display: flex; align-items: center; justify-content: space-between; gap: 20px;
      margin-bottom: 24px; padding-bottom: 22px; border-bottom: 1px solid var(--border-subtle);
      cursor: pointer; user-select: none;
    }
    .module-title-wrapper { display: flex; align-items: center; gap: 20px; }
    .module-icon-badge {
      width: 58px; height: 58px; border-radius: 18px; display: flex; align-items: center; justify-content: center;
      font-size: 26px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    .module-meta-title { font-size: 25px; font-weight: 800; color: #fff; }
    .module-cat-tag { display: inline-block; padding: 4px 12px; border-radius: 6px; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px; }

    .accordion-arrow {
      width: 42px; height: 42px; border-radius: 50%; background: rgba(255, 255, 255, 0.04);
      display: flex; align-items: center; justify-content: center; color: var(--text-muted);
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .module-card.collapsed .accordion-arrow { transform: rotate(-90deg); }
    .module-card.collapsed .module-body { display: none; }

    .module-summary { font-size: 15.5px; color: var(--text-muted); margin-bottom: 30px; line-height: 1.75; }

    /* Technical Theory Box */
    .theory-box {
      background: rgba(0, 242, 254, 0.02); border: 1px solid rgba(0, 242, 254, 0.18);
      border-left: 4px solid var(--neon-cyan); border-radius: var(--radius-lg); padding: 24px 28px; margin-bottom: 30px;
    }
    .theory-box h4 { font-size: 15px; font-weight: 800; color: var(--neon-cyan); margin-bottom: 14px; display: flex; align-items: center; gap: 10px; }
    .theory-box ul { list-style: none; display: flex; flex-direction: column; gap: 10px; }
    .theory-box li { font-size: 14px; color: var(--text-muted); line-height: 1.6; position: relative; padding-left: 22px; }
    .theory-box li::before { content: '⚡'; position: absolute; left: 0; color: var(--neon-cyan); font-size: 11px; }

    .subtopic-title {
      font-size: 18px; font-weight: 800; color: var(--text-main); display: flex; align-items: center; gap: 12px;
      margin: 38px 0 20px; padding-left: 16px; border-left: 4px solid var(--neon-cyan);
    }

    /* VERTICAL IMAGE FEED (STACKED SEQUENTIALLY, FULL NATURAL HEIGHT!) */
    .image-vertical-feed { display: flex; flex-direction: column; gap: 30px; margin-bottom: 38px; align-items: center; }

    .image-feed-card {
      background: rgba(5, 8, 15, 0.95); border: 1px solid var(--border-subtle);
      border-radius: var(--radius-xl); overflow: hidden; width: 100%; max-width: 1000px;
      box-shadow: 0 20px 45px rgba(0, 0, 0, 0.7); transition: all 0.35s ease; position: relative;
    }
    .image-feed-card:hover {
      border-color: rgba(0, 242, 254, 0.5);
      box-shadow: 0 0 40px rgba(0, 242, 254, 0.22), 0 25px 60px rgba(0, 0, 0, 0.85);
      transform: translateY(-4px);
    }

    /* FULL NATURAL DISPLAY (NEVER CROPS ANY PIXEL!) */
    .image-thumb-wrapper {
      position: relative; width: 100%; display: flex; align-items: center; justify-content: center;
      background: #020306; padding: 16px; cursor: pointer;
    }
    .image-thumb-wrapper img {
      max-width: 100%; height: auto; display: block; object-fit: contain;
      border-radius: var(--radius-md); transition: transform 0.3s ease;
    }
    .image-feed-card:hover .image-thumb-wrapper img { transform: scale(1.01); }

    .image-overlay {
      position: absolute; top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(4, 6, 10, 0.45); backdrop-filter: blur(4px);
      display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.25s ease;
    }
    .image-feed-card:hover .image-overlay { opacity: 1; }

    .zoom-btn {
      padding: 12px 24px; border-radius: 24px;
      background: linear-gradient(135deg, var(--neon-cyan), var(--neon-blue));
      color: #000; border: none; display: flex; align-items: center; gap: 10px;
      font-size: 13.5px; font-weight: 800; cursor: pointer; box-shadow: 0 0 25px rgba(0, 242, 254, 0.6);
    }

    .image-card-caption {
      padding: 16px 26px; font-size: 13px; color: var(--text-muted);
      display: flex; align-items: center; justify-content: space-between;
      border-top: 1px solid var(--border-subtle); background: rgba(8, 12, 22, 0.9);
    }
    .fig-num { font-family: 'JetBrains Mono', monospace; font-weight: 800; color: var(--neon-cyan); }

    /* Code Blocks */
    .code-block { background: #030509; border: 1px solid var(--border-subtle); border-radius: var(--radius-lg); margin: 26px 0; overflow: hidden; }
    .code-header {
      display: flex; align-items: center; justify-content: space-between; padding: 14px 22px;
      background: rgba(255, 255, 255, 0.02); border-bottom: 1px solid var(--border-subtle);
      font-size: 12.5px; font-family: 'JetBrains Mono', monospace; color: var(--text-dim);
    }
    .window-dots { display: flex; align-items: center; gap: 6px; }
    .window-dots .dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
    .window-dots .dot.red { background: #ff5f56; }
    .window-dots .dot.yellow { background: #ffbd2e; }
    .window-dots .dot.green { background: #27c93f; }
    .code-title { font-weight: 600; color: var(--text-muted); }

    .copy-btn {
      background: rgba(0, 242, 254, 0.08); border: 1px solid rgba(0, 242, 254, 0.2);
      color: var(--neon-cyan); padding: 6px 14px; border-radius: 8px; cursor: pointer;
      font-size: 12px; font-weight: 700; display: flex; align-items: center; gap: 6px; transition: all 0.2s;
    }
    .copy-btn:hover { background: var(--neon-cyan); color: #000; box-shadow: 0 0 15px rgba(0, 242, 254, 0.4); }
    pre { padding: 22px; font-family: 'JetBrains Mono', monospace; font-size: 13.5px; color: #e2e8f0; overflow-x: auto; }

    /* Lightbox Modal */
    .lightbox-modal {
      position: fixed; top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(2, 4, 7, 0.96); backdrop-filter: blur(30px); -webkit-backdrop-filter: blur(30px);
      z-index: 1000; display: flex; flex-direction: column; opacity: 0; pointer-events: none; transition: opacity 0.3s ease;
    }
    .lightbox-modal.active { opacity: 1; pointer-events: auto; }
    .lightbox-header { padding: 20px 40px; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border-subtle); }
    .lightbox-title { font-size: 15.5px; font-weight: 800; color: #fff; }
    .lightbox-controls { display: flex; align-items: center; gap: 12px; }
    .control-btn {
      background: rgba(255, 255, 255, 0.05); border: 1px solid var(--border-subtle); color: #fff;
      width: 42px; height: 42px; border-radius: 12px; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: all 0.2s;
    }
    .control-btn:hover { background: rgba(0, 242, 254, 0.2); border-color: var(--neon-cyan); color: var(--neon-cyan); }

    .lightbox-body { flex: 1; display: flex; align-items: center; justify-content: center; position: relative; overflow: auto; padding: 30px; }
    .lightbox-img { max-width: 95%; max-height: 88vh; object-fit: contain; border-radius: var(--radius-md); box-shadow: 0 30px 80px rgba(0, 0, 0, 0.95); transition: transform 0.2s ease-out; }
    .lightbox-nav-btn {
      position: absolute; top: 50%; transform: translateY(-50%); width: 54px; height: 54px; border-radius: 50%;
      background: rgba(12, 18, 30, 0.9); border: 1px solid var(--border-glow); color: #fff;
      display: flex; align-items: center; justify-content: center; font-size: 20px; cursor: pointer; transition: all 0.25s;
    }
    .lightbox-nav-btn:hover { background: var(--neon-cyan); color: #000; box-shadow: 0 0 25px rgba(0, 242, 254, 0.7); }
    .lightbox-prev { left: 30px; }
    .lightbox-next { right: 30px; }

    /* Toast Notification */
    .toast-notification {
      position: fixed; bottom: 30px; right: 90px;
      background: rgba(0, 242, 254, 0.15); border: 1px solid var(--neon-cyan); color: #fff;
      padding: 12px 24px; border-radius: 30px; font-size: 13.5px; font-weight: 700;
      backdrop-filter: blur(15px); display: flex; align-items: center; gap: 10px;
      box-shadow: 0 0 25px rgba(0, 242, 254, 0.3);
      opacity: 0; transform: translateY(20px); transition: all 0.3s ease; pointer-events: none; z-index: 100;
    }
    .toast-notification.show { opacity: 1; transform: translateY(0); }

    .back-to-top {
      position: fixed; bottom: 30px; right: 30px; width: 50px; height: 50px; border-radius: 50%;
      background: rgba(12, 18, 30, 0.9); border: 1px solid var(--border-glow); color: #fff;
      display: flex; align-items: center; justify-content: center; cursor: pointer; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
      opacity: 0; visibility: hidden; transition: all 0.3s; z-index: 90;
    }
    .back-to-top.show { opacity: 1; visibility: visible; }
    .back-to-top:hover { background: var(--neon-cyan); color: #000; box-shadow: 0 0 25px rgba(0, 242, 254, 0.6); }

    @media (max-width: 1024px) {
      .sidebar { transform: translateX(-100%); }
      .main-content { margin-left: 0; padding: 24px; }
      .sidebar.open { transform: translateX(0); }
    }
  </style>
</head>
<body>

<canvas id="cyberCanvas"></canvas>

<div class="app-container">
  
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <div class="brand-author-card">
        <div class="brand-avatar"><i class="fa-solid fa-user-shield"></i></div>
        <div class="brand-info">
          <h1>ZYAD ELSHESHTAWY</h1>
          <p>SOC ARCHITECT</p>
        </div>
      </div>
    </div>

    <div class="sidebar-controls">
      <div class="search-box">
        <i class="fa-solid fa-magnifying-glass"></i>
        <input type="text" id="searchInput" class="search-input" placeholder="Search modules, SPL, commands...">
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

for m in MODULES:
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

  <main class="main-content">
    
    <header class="hero-header">
      
      <!-- PROMINENT ZYAD ELSHESHTAWY SIGNATURE HERO CARD -->
      <div class="author-signature-hero">
        <div class="author-signature-avatar"><i class="fa-solid fa-user-shield"></i></div>
        <div class="author-signature-text">
          <span class="author-signature-tag">LEAD CYBER SECURITY ARCHITECT & AUTHOR</span>
          <h2 class="author-signature-name">ZYAD ELSHESHTAWY</h2>
          <span class="author-signature-role">Enterprise Threat Hunter & Detection Engineering Specialist</span>
        </div>
      </div>

      <h1 class="hero-title">SOC PATH 2 Masterclass & Lab Evidence</h1>
      <p class="hero-subtitle">
        An interactive, high-fidelity Enterprise SOC Operations & Threat Detection Engineering Master Handbook.
        Authored by <strong>Zyad Elsheshtawy</strong>. Featuring 907 full natural-height lab evidence screenshots arranged in a seamless vertical feed, operational theory, SIEM queries, and incident playbooks.
      </p>

      <div class="stats-grid">
        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(0, 242, 254, 0.12); color: var(--neon-cyan);">
            <i class="fa-solid fa-layer-group"></i>
          </div>
          <div>
            <div class="stat-val">14</div>
            <div class="stat-lbl">Core SOC Modules</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(16, 185, 129, 0.12); color: var(--neon-emerald);">
            <i class="fa-solid fa-images"></i>
          </div>
          <div>
            <div class="stat-val">907</div>
            <div class="stat-lbl">Full Lab Screenshots</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(157, 78, 221, 0.12); color: var(--neon-purple);">
            <i class="fa-solid fa-terminal"></i>
          </div>
          <div>
            <div class="stat-val">35+</div>
            <div class="stat-lbl">Hands-on Labs</div>
          </div>
        </div>

        <div class="stat-card">
          <div class="stat-icon" style="background: rgba(245, 158, 11, 0.12); color: var(--neon-amber);">
            <i class="fa-solid fa-bolt"></i>
          </div>
          <div>
            <div class="stat-val">100%</div>
            <div class="stat-lbl">Natural Aspect Ratio</div>
          </div>
        </div>
      </div>

      <div class="progress-bar-container">
        <span class="progress-text" id="progressText">0 of 14 Modules Completed (0%)</span>
        <div class="progress-track">
          <div class="progress-fill" id="progressFill"></div>
        </div>
      </div>
    </header>
''')

fig_counter = 1

for m in MODULES:
    html_parts.append(f'''
    <section id="{m["id"]}" class="module-section" data-category="{m["category"]}">
      <div class="module-card" id="card-mod-{m["id"]}">
        
        <div class="module-header" onclick="toggleAccordion('card-mod-{m["id"]}')">
          <div class="module-title-wrapper">
            <div class="module-icon-badge" style="background: {m["color"]}18; color: {m["color"]}; border: 1px solid {m["color"]}30;">
              <i class="fa-solid {m["icon"]}"></i>
            </div>
            <div>
              <div class="module-meta-title">{m["num"]}. {m["title"]}</div>
              <span class="module-cat-tag" style="background: {m["color"]}18; color: {m["color"]};">
                {m["category"]}
              </span>
            </div>
          </div>

          <div style="display:flex; align-items:center; gap:16px;">
            <label class="complete-checkbox" id="check-label-{m["id"]}" onclick="event.stopPropagation()">
              <input type="checkbox" onchange="toggleModuleComplete('{m["id"]}')" id="cb-{m["id"]}" style="display:none;">
              <i class="fa-regular fa-square" id="icon-cb-{m["id"]}"></i> Mark Complete
            </label>
            <div class="accordion-arrow"><i class="fa-solid fa-chevron-down"></i></div>
          </div>
        </div>

        <div class="module-body">
          <p class="module-summary">{m["summary"]}</p>
          
          {m["theory"]}
          {m["commands"]}
          
          <div class="subtopic-container">
    ''')

    mod_items = raw_items[m["start_idx"]:m["end_idx"] + 1]
    sub_imgs = []

    for item in mod_items:
        txt = item["text"]
        imgs = item["imgs"]

        if txt:
            if sub_imgs:
                html_parts.append('<div class="image-vertical-feed">')
                for img_name in sub_imgs:
                    b64_data = get_b64(img_name)
                    html_parts.append(f'''
                      <div class="image-feed-card">
                        <div class="image-thumb-wrapper" onclick="openLightbox('{b64_data}', 'Figure {fig_counter}: {m["title"]} Lab Evidence')">
                          <img src="{b64_data}" alt="Lab Evidence Screenshot" loading="lazy">
                          <div class="image-overlay">
                            <button class="zoom-btn"><i class="fa-solid fa-magnifying-glass-plus"></i> View Fullscreen</button>
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

            html_parts.append(f'<div class="subtopic-title"><i class="fa-solid fa-chevron-right" style="font-size:12px; color:{m["color"]};"></i> {txt}</div>')

        for img_name in imgs:
            sub_imgs.append(img_name)

    if sub_imgs:
        html_parts.append('<div class="image-vertical-feed">')
        for img_name in sub_imgs:
            b64_data = get_b64(img_name)
            html_parts.append(f'''
              <div class="image-feed-card">
                <div class="image-thumb-wrapper" onclick="openLightbox('{b64_data}', 'Figure {fig_counter}: {m["title"]} Lab Evidence')">
                  <img src="{b64_data}" alt="Lab Evidence Screenshot" loading="lazy">
                  <div class="image-overlay">
                    <button class="zoom-btn"><i class="fa-solid fa-magnifying-glass-plus"></i> View Fullscreen</button>
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
      </div>
    </section>
    ''')

html_parts.append('''
  </main>
</div>

<div class="toast-notification" id="toast"><i class="fa-solid fa-circle-check" style="color:var(--neon-cyan);"></i> Code copied to clipboard!</div>

<button class="back-to-top" id="backToTop" onclick="scrollToTop()">
  <i class="fa-solid fa-arrow-up"></i>
</button>

<div class="lightbox-modal" id="lightboxModal">
  <div class="lightbox-header">
    <div class="lightbox-title" id="lightboxTitle">Lab Screenshot Viewer</div>
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
  // Magnetic Cyber Particles Canvas
  const canvas = document.getElementById('cyberCanvas');
  const ctx = canvas.getContext('2d');
  let width, height, particles = [];
  let mouse = { x: null, y: null, radius: 150 };

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.x;
    mouse.y = e.y;
  });

  function resizeCanvas() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.vx = (Math.random() - 0.5) * 0.5;
      this.vy = (Math.random() - 0.5) * 0.5;
      this.size = Math.random() * 2 + 0.8;
    }
    update() {
      this.x += this.vx; this.y += this.vy;
      if (this.x < 0) this.x = width;
      if (this.x > width) this.x = 0;
      if (this.y < 0) this.y = height;
      if (this.y > height) this.y = 0;

      // Mouse attraction
      if (mouse.x && mouse.y) {
        let dx = mouse.x - this.x;
        let dy = mouse.y - this.y;
        let dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouse.radius) {
          this.x += dx * 0.02;
          this.y += dy * 0.02;
        }
      }
    }
    draw() {
      ctx.fillStyle = 'rgba(0, 242, 254, 0.6)';
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  for (let i = 0; i < 50; i++) particles.push(new Particle());

  function animateCanvas() {
    ctx.clearRect(0, 0, width, height);
    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
      particles[i].draw();
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 130) {
          ctx.strokeStyle = `rgba(0, 242, 254, ${0.18 * (1 - dist / 130)})`;
          ctx.lineWidth = 0.6;
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(animateCanvas);
  }
  animateCanvas();

  // Progress & Module Logic
  let completedModules = new Set(JSON.parse(localStorage.getItem('completedModules') || '[]'));
  let currentZoom = 1;
  let allImages = [];
  let currentImageIdx = 0;

  document.addEventListener('DOMContentLoaded', () => {
    updateProgress();
    collectAllImages();
    
    window.addEventListener('scroll', () => {
      const btt = document.getElementById('backToTop');
      if (window.scrollY > 400) {
        btt.classList.add('show');
      } else {
        btt.classList.remove('show');
      }
    });

    document.getElementById('searchInput').addEventListener('input', (e) => {
      const q = e.target.value.toLowerCase().trim();
      const sections = document.querySelectorAll('.module-section');
      sections.forEach(sec => {
        const text = sec.innerText.toLowerCase();
        sec.style.display = text.includes(q) ? 'block' : 'none';
      });
    });

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

  function toggleAccordion(cardId) {
    const card = document.getElementById(cardId);
    if (card) card.classList.toggle('collapsed');
  }

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

  function filterCategory(cat) {
    document.querySelectorAll('.filter-btn').forEach(btn => {
      btn.classList.toggle('active', btn.innerText.trim() === cat);
    });

    document.querySelectorAll('.module-section').forEach(sec => {
      const secCat = sec.getAttribute('data-category');
      sec.style.display = (cat === 'All' || secCat === cat) ? 'block' : 'none';
    });

    document.querySelectorAll('.nav-item').forEach(item => {
      const itemCat = item.getAttribute('data-category');
      item.style.display = (cat === 'All' || itemCat === cat) ? 'flex' : 'none';
    });
  }

  function setActiveNav(el) {
    document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
    el.classList.add('active');
  }

  function copyCode(btn) {
    const pre = btn.parentElement.nextElementSibling;
    if (pre) {
      navigator.clipboard.writeText(pre.innerText);
      showToast();
    }
  }

  function showToast() {
    const toast = document.getElementById('toast');
    toast.classList.add('show');
    setTimeout(() => { toast.classList.remove('show'); }, 2500);
  }

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

output_html_path = 'SOC_PATH_2_Masterclass.html'
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write(''.join(html_parts))

print(f"Successfully generated Ultimate Masterpiece HTML: {output_html_path}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(''.join(html_parts))

print("Successfully updated index.html!")
