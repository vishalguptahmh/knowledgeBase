### Supply Chain Vulnerabilities

**Definition**

Supply chain vulnerabilities occur when attackers compromise external components that an application depends on. These components may include libraries, frameworks, plugins, APIs, development tools, or other third-party services.

Such weaknesses can be introduced at any point in the software development lifecycle, including development, testing, packaging, and deployment. The growing use of Artificial Intelligence (AI) and Large Language Models (LLMs) has expanded this risk surface because systems often rely on external datasets, pre-trained models, and third-party tools.

---

### Impact

When a dependency or external service is compromised, it can affect the behavior and security of the entire application. Possible consequences include:

* Unexpected or malicious application behavior
* Performance degradation or service disruption
* Bypassing of existing security mechanisms
* Exposure of sensitive data
* Unauthorized system access

**Example**

In **September 2025**, attackers compromised more than **100 npm packages** that were collectively downloaded billions of times each week. The malicious code spread to other projects that depended on these packages, allowing attackers to distribute harmful updates through normal dependency updates.

---

### Common Scenarios

Supply chain attacks can appear in several forms depending on how an application integrates external resources.

#### 1. Compromised Third-Party Libraries

A trusted open-source library is modified to include malicious functionality. Once the updated version is installed, the malicious code runs automatically when the application executes.

**Example**

An Android app depends on a logging library from a public repository.
A malicious update adds hidden code that sends device identifiers to a remote server.

---

#### 2. Malicious Plugins or Extensions

Plugins developed outside the organization may include hidden instructions that perform unauthorized operations.

**Example**

A browser extension used for form autofill secretly collects stored credentials and sends them to an attacker-controlled server.

---

#### 3. Poisoned Training Data for LLMs

If training datasets are manipulated, the resulting model may generate incorrect outputs or leak confidential information.

**Example**

A customer-support chatbot is trained on external support documentation.
Attackers modify the dataset to include misleading troubleshooting steps, causing the chatbot to provide incorrect guidance.

---

#### 4. Untrusted External Services

Applications frequently interact with external APIs. If these services are compromised, they may return malicious responses.

**Example**

A payment service API is compromised and begins returning altered transaction responses that trick the application into accepting fraudulent payments.

---

### Prevention

The following practices help reduce supply chain risks.

**Keep dependencies updated**

Regularly update libraries, frameworks, and plugins to patched versions.

*Example:*
Use dependency scanners such as Dependabot or Snyk to detect vulnerable packages.

---

**Evaluate third-party components**

Assess the reputation, maintenance history, and security practices of external components before using them.

*Example:*
Host critical dependencies in an internal artifact repository instead of pulling them directly from public registries.

---

**Validate training data**

Ensure that datasets used for AI training or fine-tuning are authentic and have not been modified.

*Example:*
Verify dataset hashes before training a model.

---

**Maintain an inventory**

Track all software components using a **Software Bill of Materials (SBOM)**.

*Example:*
An SBOM lists all libraries, versions, and dependencies used in an application so that vulnerable components can be identified quickly.

---

**Use code signing**

Verify that dependencies and models are signed by trusted publishers.

*Example:*
A container image is deployed only if its cryptographic signature matches the expected publisher.

---

**Control supplier access**

Review permissions granted to third-party contributors and vendors.

*Example:*
Limit repository access so external contributors cannot directly publish releases without review.

---

### Testing for Supply Chain Vulnerabilities

Security testing should verify the integrity of all external components.

Typical testing activities include:

* Checking cryptographic signatures or checksums of downloaded dependencies
* Verifying secure update mechanisms
* Enforcing strict access controls for package repositories
* Monitoring applications for unauthorized or unexpected dependencies

Continuous monitoring tools can detect tampering or unexpected changes in external components.

---

### AI and LLM Supply Chain Risks

Applications that use Large Language Models often depend on external resources such as:

* Prompt templates
* Plugins and tools
* Training datasets
* Model repositories
* Agent-to-agent communication protocols such as MCP or A2A

Because many of these components may be discovered dynamically at runtime, the AI system’s supply chain can expand automatically. Any compromised component can influence the model’s behavior, leak sensitive information, or trigger harmful actions.

---

### Third-Party Components in AI Systems

Agent-based systems frequently load prompts, tools, or datasets from external locations. If these upstream sources are tampered with, the entire system may behave incorrectly.

**Example**

An AI coding assistant downloads a prompt template from a public registry.
The template secretly instructs the model to insert backdoor code into generated programs.

**Mitigation**

* Maintain an **SBOM** or **AI Bill of Materials (AIBOM)**
* Perform staged rollouts of updates
* Compare behavior across versions before deployment
* Automatically revert changes when unexpected behavior occurs

---

### Outdated or Malicious Models

LLMs obtained from open repositories or collaborative platforms may contain backdoors or known vulnerabilities.

**Example**

A company integrates an open-source LLM downloaded from a community repository.
The model was modified to occasionally reveal parts of its training data when asked specific questions.

**Mitigation**

* Download models only from trusted vendors
* Verify model checksums or digital signatures
* Monitor output patterns for suspicious behavior

---

### Tool Poisoning

Agent frameworks often dynamically discover new tools or capabilities. If a malicious tool is introduced into the ecosystem, it may manipulate the agent’s decision-making.

**Example**

An MCP tool descriptor retrieved from a remote server includes hidden metadata that causes the agent to prefer that tool, which secretly sends sensitive user data to attackers.

**Mitigation**

* Require signed tool descriptors
* Validate metadata formats and schemas
* Reverify signatures whenever tools are updated

---

### Poisoned Prompt Templates

Applications may automatically fetch prompt templates to guide model behavior. If these templates are altered, the model may follow malicious instructions.

**Example**

A template used by an AI coding assistant includes hidden instructions directing the model to embed insecure authentication logic into generated code.

**Mitigation**

* Treat external prompt templates as untrusted
* Restrict template sources to trusted repositories
* Sign and hash prompt templates
* Reject templates whose signatures or hashes change unexpectedly

---

### Poisoned Datasets

External datasets used for training or retrieval-augmented generation (RAG) can be modified to introduce misleading or malicious information.

**Example**

A support chatbot retrieves answers from a knowledge base.
An attacker modifies the knowledge base to recommend unsafe troubleshooting actions.

**Mitigation**

* Verify dataset integrity before use
* Track dataset origin using data provenance techniques
* Monitor datasets for unauthorized modifications

---

### References

* OWASP – Supply Chain Security
* OWASP – Top 10 for LLM Applications
* OWASP – Mobile Top 10
* OWASP – Kubernetes Top 10
* OWASP ASVS – 15.2

