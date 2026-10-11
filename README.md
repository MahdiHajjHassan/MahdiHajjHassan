# Mahdi Hajj Hassan | Data engineering & applied AI

> [!CAUTION]
> **Critical HR information, handled responsibly.** At Thales, I delivered pipelines and reporting for critical HR data covering tens of thousands of employees worldwide. Public showcases use independent examples, with no Thales implementation or data and no employer endorsement. Private application code stays private; diagrams explain project workflows.

I'm **Mahdi**, a **data engineer at Thales** in **Beirut, Lebanon**, and a **42 Beirut alumnus**. I delivered enterprise HR pipelines and reporting and supplied datasets for AI model training. I also shipped AI workflows and built a multi-agent system for a university that routes student and staff requests to the right people.

My work connects **data engineering, AI workflows, and the applications people use to get work done**.

[Email](mailto:mahdihajjhassan.business@gmail.com) · [LinkedIn](https://www.linkedin.com/in/mahdi-hajj-hassan-5b953b312/)

## Selected projects

- [**HR Data Platform**](https://github.com/MahdiHajjHassan/workforce-data-platform): enterprise HR reporting, controlled sharing, and datasets for AI model training.
- [**University Multi-Agent Ticket Routing**](https://github.com/MahdiHajjHassan/university-ticket-orchestration): university knowledge retrieval and agent coordination that connect a request to the department and person responsible.
- [**GCP Data Pipeline**](https://github.com/MahdiHajjHassan/MahdiHajjHassan/blob/main/projects/gcp-data-pipeline/README.md): scheduled ingestion, analytics, anomaly scoring, and AI interpretation.
- [**AgentCrew**](https://github.com/MahdiHajjHassan/ai-development-workflow): an AI software delivery workflow from feature request to code review and human approval.
- [**PolicyForge**](https://github.com/MahdiHajjHassan/policy-aware-data-generator): synthetic development datasets shaped by team, role, country, and field permissions.
- [**Doctoleb**](https://github.com/MahdiHajjHassan/doctoleb-showcase): appointments, patient records, and clinic administration in a multilingual application.
- [**Restaurant Websites**](https://github.com/MahdiHajjHassan/Restaurant-app): branded bilingual sites with menu management and separate owner/operator controls.

## 01 / HR Data Platform

**Reliable HR information for reporting, sharing, and AI training.** At Thales, I delivered ingestion, transformations, data models, and reporting for a global workforce. I also supplied HR datasets for AI model training. HR analysts, authorized business teams, and AI teams needed different outputs from the same underlying information.

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 540px)" srcset="assets/workforce-story-v4-mobile-dark.svg">
  <source media="(max-width: 540px)" srcset="assets/workforce-story-v4-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/workforce-story-v4-dark.svg">
  <img src="assets/workforce-story-v4-light.svg" alt="HR source inputs feed shared workforce, country, department, and job definitions. The model serves HR reporting, controlled sharing, and a training dataset that feeds AI model training." width="680">
</picture>

[HR project and engineering details →](https://github.com/MahdiHajjHassan/workforce-data-platform)

## 02 / University Multi-Agent Ticket Routing

**A university request should reach the person who can resolve it.** I built an orchestrator for a university that coordinated two specialist agents: one retrieved relevant university knowledge, and another analyzed the request and routed the ticket to the responsible department and person. Students and staff used the same entry point for different service needs.

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 520px)" srcset="assets/university-ticket-story-v2-mobile-dark.svg">
  <source media="(max-width: 520px)" srcset="assets/university-ticket-story-v2-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/university-ticket-story-v2-dark.svg">
  <img src="assets/university-ticket-story-v2-light.svg" alt="University ticket orchestration: students and staff submit a ticket, an orchestrator coordinates a university knowledge RAG agent and a workflow agent, and the ticket is routed to a department and responsible person." width="680">
</picture>

[University project: agents, retrieval, and routing →](https://github.com/MahdiHajjHassan/university-ticket-orchestration)

## 03 / GCP Data Pipeline

**From incoming data to an analyst's next question.** I built an ingestion-to-analytics pipeline with Dataflow, BigQuery, and Cloud Workflows. The traffic workflow below explains scheduled collection, consistent analytical tables, anomaly scoring, and AI commentary alongside the measured values.

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 520px)" srcset="assets/gcp-story-v4-mobile-dark.svg">
  <source media="(max-width: 520px)" srcset="assets/gcp-story-v4-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/gcp-story-v4-dark.svg">
  <img src="assets/gcp-story-v4-light.svg" alt="An hourly schedule starts Workflows. Ingestion feeds BigQuery staging, ODS, and warehouse layers, followed by anomaly scoring, Gemini interpretation, and Looker analysis." width="680">
</picture>

[GCP pipeline and AI analysis →](https://github.com/MahdiHajjHassan/MahdiHajjHassan/blob/main/projects/gcp-data-pipeline/README.md)

## 04 / AgentCrew: AI Software Delivery Workflow

**Turn a feature request into a change someone can review.** I designed an AI workflow with distinct planning, technical review, implementation, and quality review responsibilities. Each stage used the same requirements and decisions; the product owner reviewed the code changes and check results before approval.

<picture>
  <source media="(max-width: 540px) and (prefers-color-scheme: dark)" srcset="assets/ai-story-v4-mobile-dark.svg">
  <source media="(max-width: 540px)" srcset="assets/ai-story-v4-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/ai-story-v4-dark.svg">
  <img src="assets/ai-story-v4-light.svg" width="680" alt="Planning and technical review define the task. Implementation supplies code changes, quality review checks them, and a person approves the change or requests revision.">
</picture>

[AgentCrew workflow and task examples →](https://github.com/MahdiHajjHassan/ai-development-workflow)

## 05 / PolicyForge: Permission-Aware Development Data

**Give each team development data that matches its access.** I developed a configurable synthetic-data generator that shaped datasets for different recipients. Operations, finance, and partner teams could receive different fields, with country rules further narrowing what each dataset contained.

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 540px)" srcset="assets/policy-story-v3-mobile-dark.svg">
  <source media="(max-width: 540px)" srcset="assets/policy-story-v3-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/policy-story-v3-dark.svg">
  <img src="assets/policy-story-v3-light.svg" alt="Recipient and country permissions determine the output columns. Operations in Aster omit pay fields, Finance in Aster include them, and Finance in Boreal omit them." width="680">
</picture>

[PolicyForge design and example datasets →](https://github.com/MahdiHajjHassan/policy-aware-data-generator)

## 06 / Doctoleb: Clinic Management

**Appointments, patient records, and visit administration in one workflow.** I developed Doctoleb around receptionists, doctors, and clinic administrators. I designed English, Arabic, and French interfaces, staff access rules, and local browser operation with synchronization for interrupted connectivity.

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 520px)" srcset="assets/clinic-story-v4-mobile-dark.svg">
  <source media="(max-width: 520px)" srcset="assets/clinic-story-v4-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/clinic-story-v4-dark.svg">
  <img src="assets/clinic-story-v4-light.svg" alt="An appointment calendar connects to a patient-record folder and visit timeline. Staff and clinic setup support the connected clinic day." width="680">
</picture>

[Doctoleb product and architecture →](https://github.com/MahdiHajjHassan/doctoleb-showcase)

## 07 / Restaurant Websites

**A shared application, with each restaurant's own identity.** I developed bilingual restaurant sites, owner tools for menus and branding, and operator tools for onboarding. I connected restaurant domains, isolated business data, reusable themes, and photo processing in one codebase.

<picture>
  <source media="(prefers-color-scheme: dark) and (max-width: 520px)" srcset="assets/restaurant-story-v3-mobile-dark.svg">
  <source media="(max-width: 520px)" srcset="assets/restaurant-story-v3-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/restaurant-story-v3-dark.svg">
  <img src="assets/restaurant-story-v3-light.svg" alt="A branded restaurant website, bilingual guest menu on a phone, and owner controls for menus, photos, and branding share one restaurant identity." width="680">
</picture>

[Restaurant application and architecture →](https://github.com/MahdiHajjHassan/Restaurant-app)

## Technical background

<details>
<summary><strong>Enterprise delivery and systems foundations</strong></summary>

### Data engineering at Thales

I delivered SQL Server stored procedures and Talend ETL pipelines feeding HR operational and analytical systems. My work included data modeling, validation, Power BI reporting, deployment, and production troubleshooting. I supplied HR datasets for AI model training and worked with GCP Dataflow, BigQuery, and Cloud Workflows.

I clarified requirements with the product owner, discussed architecture with the technical lead, and coordinated delivery with engineers and interns.

### Software engineering at 42 Beirut

I'm a **42 Beirut alumnus**. C and C++ projects developed my experience with algorithms, data structures, Unix processes, filesystems, networking, debugging, testing, and peer review. My application work also covered Python APIs, web applications, and Electron desktop software.

<a href="https://www.thalesgroup.com/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MahdiHajjHassan/MahdiHajjHassan/main/assets/thales-dark.svg"><img src="https://raw.githubusercontent.com/MahdiHajjHassan/MahdiHajjHassan/main/assets/thales.svg" alt="Thales" width="100"></picture></a>&nbsp;&nbsp;&nbsp;
<a href="https://www.42beirut.com/"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MahdiHajjHassan/MahdiHajjHassan/main/assets/42-dark.svg"><img src="https://raw.githubusercontent.com/MahdiHajjHassan/MahdiHajjHassan/main/assets/42-light.svg" alt="42 Beirut alumni affiliation" width="32"></picture></a>

</details>

[Email](mailto:mahdihajjhassan.business@gmail.com) · [LinkedIn](https://www.linkedin.com/in/mahdi-hajj-hassan-5b953b312/)

<!-- SKILLS:START -->
## Languages, tools, and skills

### Languages

<p>
  <img src="assets/skill-badge-v1-python.svg" alt="Python" width="70" height="34">
  <img src="assets/skill-badge-v1-c.svg" alt="C" width="52" height="34">
  <img src="assets/skill-badge-v1-cpp.svg" alt="C++" width="52" height="34">
  <img src="assets/skill-badge-v1-javascript.svg" alt="JavaScript" width="91" height="34">
  <img src="assets/skill-badge-v1-typescript.svg" alt="TypeScript" width="93" height="34">
  <img src="assets/skill-badge-v1-java.svg" alt="Java" width="54" height="34">
  <img src="assets/skill-badge-v1-sql.svg" alt="SQL" width="53" height="34">
  <img src="assets/skill-badge-v1-t-sql.svg" alt="T-SQL" width="65" height="34">
  <img src="assets/skill-badge-v1-bash.svg" alt="Bash" width="57" height="34">
</p>

### Frameworks and applications

<p>
  <img src="assets/skill-badge-v1-react.svg" alt="React" width="60" height="34">
  <img src="assets/skill-badge-v1-next-js.svg" alt="Next.js" width="68" height="34">
  <img src="assets/skill-badge-v1-nestjs.svg" alt="NestJS" width="69" height="34">
  <img src="assets/skill-badge-v1-node-js.svg" alt="Node.js" width="73" height="34">
  <img src="assets/skill-badge-v1-fastapi.svg" alt="FastAPI" width="74" height="34">
  <img src="assets/skill-badge-v1-electron.svg" alt="Electron" width="78" height="34">
  <img src="assets/skill-badge-v1-electron-vite.svg" alt="electron-vite" width="102" height="34">
  <img src="assets/skill-badge-v1-full-stack-development.svg" alt="Full-stack development" width="170" height="34">
  <img src="assets/skill-badge-v1-cross-platform-desktop-apps.svg" alt="Cross-platform desktop apps" width="205" height="34">
</p>

### Data platforms and analytics

<p>
  <img src="assets/skill-badge-v1-sql-server.svg" alt="SQL Server" width="97" height="34">
  <img src="assets/skill-badge-v1-postgresql.svg" alt="PostgreSQL" width="101" height="34">
  <img src="assets/skill-badge-v1-talend-etl.svg" alt="Talend ETL" width="97" height="34">
  <img src="assets/skill-badge-v1-ssis.svg" alt="SSIS" width="57" height="34">
  <img src="assets/skill-badge-v1-ssms.svg" alt="SSMS" width="64" height="34">
  <img src="assets/skill-badge-v1-power-bi.svg" alt="Power BI" width="82" height="34">
  <img src="assets/skill-badge-v1-dax.svg" alt="DAX" width="53" height="34">
  <img src="assets/skill-badge-v1-ssas.svg" alt="SSAS" width="62" height="34">
  <img src="assets/skill-badge-v1-looker.svg" alt="Looker" width="69" height="34">
  <img src="assets/skill-badge-v1-indexeddb.svg" alt="IndexedDB" width="93" height="34">
  <img src="assets/skill-badge-v1-drizzle-orm.svg" alt="Drizzle ORM" width="103" height="34">
</p>

### Cloud

<p>
  <img src="assets/skill-badge-v1-google-cloud-platform.svg" alt="Google Cloud Platform" width="169" height="34">
  <img src="assets/skill-badge-v1-dataflow.svg" alt="Dataflow" width="79" height="34">
  <img src="assets/skill-badge-v1-bigquery.svg" alt="BigQuery" width="84" height="34">
  <img src="assets/skill-badge-v1-cloud-workflows.svg" alt="Cloud Workflows" width="132" height="34">
</p>

### APIs and access

<p>
  <img src="assets/skill-badge-v1-sqlalchemy.svg" alt="SQLAlchemy" width="107" height="34">
  <img src="assets/skill-badge-v1-pydantic.svg" alt="Pydantic" width="80" height="34">
  <img src="assets/skill-badge-v1-openapi.svg" alt="OpenAPI" width="81" height="34">
  <img src="assets/skill-badge-v1-jwt-authentication.svg" alt="JWT authentication" width="145" height="34">
  <img src="assets/skill-badge-v1-role-based-access.svg" alt="Role-based access" width="141" height="34">
</p>

### AI workflows

<p>
  <img src="assets/skill-badge-v1-multi-agent-orchestration.svg" alt="Multi-agent orchestration" width="182" height="34">
  <img src="assets/skill-badge-v1-retrieval-augmented-generation-rag.svg" alt="Retrieval-augmented generation (RAG)" width="263" height="34">
  <img src="assets/skill-badge-v1-request-analysis.svg" alt="Request analysis" width="131" height="34">
  <img src="assets/skill-badge-v1-ticket-routing.svg" alt="Ticket routing" width="112" height="34">
  <img src="assets/skill-badge-v1-ai-software-workflows.svg" alt="AI software workflows" width="162" height="34">
</p>

### Systems

<p>
  <img src="assets/skill-badge-v1-linux.svg" alt="Linux" width="61" height="34">
  <img src="assets/skill-badge-v1-unix.svg" alt="Unix" width="54" height="34">
  <img src="assets/skill-badge-v1-processes.svg" alt="Processes" width="90" height="34">
  <img src="assets/skill-badge-v1-filesystems.svg" alt="Filesystems" width="100" height="34">
  <img src="assets/skill-badge-v1-networking.svg" alt="Networking" width="97" height="34">
  <img src="assets/skill-badge-v1-system-administration.svg" alt="System administration" width="166" height="34">
</p>

### Data engineering

<p>
  <img src="assets/skill-badge-v1-etl.svg" alt="ETL" width="52" height="34">
  <img src="assets/skill-badge-v1-stored-procedures.svg" alt="Stored procedures" width="141" height="34">
  <img src="assets/skill-badge-v1-data-modeling.svg" alt="Data modeling" width="116" height="34">
  <img src="assets/skill-badge-v1-operational-data-stores.svg" alt="Operational data stores" width="170" height="34">
  <img src="assets/skill-badge-v1-data-warehouses.svg" alt="Data warehouses" width="131" height="34">
  <img src="assets/skill-badge-v1-full-loads.svg" alt="Full loads" width="88" height="34">
  <img src="assets/skill-badge-v1-delta-loads.svg" alt="Delta loads" width="95" height="34">
  <img src="assets/skill-badge-v1-data-conversion.svg" alt="Data conversion" width="126" height="34">
  <img src="assets/skill-badge-v1-data-validation.svg" alt="Data validation" width="118" height="34">
  <img src="assets/skill-badge-v1-ai-training-datasets.svg" alt="AI training datasets" width="146" height="34">
  <img src="assets/skill-badge-v1-production-troubleshooting.svg" alt="Production troubleshooting" width="198" height="34">
  <img src="assets/skill-badge-v1-web-scraping.svg" alt="Web scraping" width="111" height="34">
</p>

### Software engineering and testing

<p>
  <img src="assets/skill-badge-v1-pytest.svg" alt="pytest" width="64" height="34">
  <img src="assets/skill-badge-v1-object-oriented-programming.svg" alt="Object-oriented programming" width="210" height="34">
  <img src="assets/skill-badge-v1-algorithms.svg" alt="Algorithms" width="95" height="34">
  <img src="assets/skill-badge-v1-data-structures.svg" alt="Data structures" width="119" height="34">
  <img src="assets/skill-badge-v1-debugging.svg" alt="Debugging" width="94" height="34">
  <img src="assets/skill-badge-v1-secure-coding.svg" alt="Secure coding" width="116" height="34">
  <img src="assets/skill-badge-v1-api-testing.svg" alt="API testing" width="94" height="34">
  <img src="assets/skill-badge-v1-unit-testing.svg" alt="Unit testing" width="97" height="34">
  <img src="assets/skill-badge-v1-integration-testing.svg" alt="Integration testing" width="140" height="34">
</p>

### Delivery

<p>
  <img src="assets/skill-badge-v1-docker.svg" alt="Docker" width="69" height="34">
  <img src="assets/skill-badge-v1-git.svg" alt="Git" width="52" height="34">
  <img src="assets/skill-badge-v1-github.svg" alt="GitHub" width="69" height="34">
  <img src="assets/skill-badge-v1-gitlab.svg" alt="GitLab" width="67" height="34">
  <img src="assets/skill-badge-v1-gitlab-ci-cd.svg" alt="GitLab CI/CD" width="106" height="34">
  <img src="assets/skill-badge-v1-code-review.svg" alt="Code review" width="102" height="34">
  <img src="assets/skill-badge-v1-release-management.svg" alt="Release management" width="158" height="34">
  <img src="assets/skill-badge-v1-deployments.svg" alt="Deployments" width="107" height="34">
  <img src="assets/skill-badge-v1-artifact-versioning.svg" alt="Artifact versioning" width="140" height="34">
  <img src="assets/skill-badge-v1-build-tooling.svg" alt="Build tooling" width="107" height="34">
  <img src="assets/skill-badge-v1-software-integration.svg" alt="Software integration" width="151" height="34">
</p>

### Collaboration and design

<p>
  <img src="assets/skill-badge-v1-agile.svg" alt="Agile" width="58" height="34">
  <img src="assets/skill-badge-v1-scrum.svg" alt="Scrum" width="67" height="34">
  <img src="assets/skill-badge-v1-jira.svg" alt="Jira" width="52" height="34">
  <img src="assets/skill-badge-v1-miro.svg" alt="Miro" width="54" height="34">
  <img src="assets/skill-badge-v1-microsoft-teams.svg" alt="Microsoft Teams" width="129" height="34">
  <img src="assets/skill-badge-v1-technical-documentation.svg" alt="Technical documentation" width="183" height="34">
  <img src="assets/skill-badge-v1-peer-evaluation.svg" alt="Peer evaluation" width="122" height="34">
  <img src="assets/skill-badge-v1-peer-feedback.svg" alt="Peer feedback" width="113" height="34">
  <img src="assets/skill-badge-v1-requirements-analysis.svg" alt="Requirements analysis" width="167" height="34">
  <img src="assets/skill-badge-v1-architecture-design.svg" alt="Architecture design" width="147" height="34">
  <img src="assets/skill-badge-v1-knowledge-sharing.svg" alt="Knowledge sharing" width="146" height="34">
</p>

<!-- SKILLS:END -->
