# Contributing

Thanks for helping improve **Awesome Embodied Trustworthy Execution**.

## Add a paper

Please open an Issue or PR and provide:

1. **Title / arXiv / venue**
2. **Primary layer**
   - `I. Malicious Attacks`
   - `II. Soft / Hardware Errors`
   - `III. Decision Anomalies`
   - `Survey / Framework`
3. **Source of non-trustworthiness** — what makes the embodied loop untrustworthy?
4. **Intervention stage** — training, pre-execution, generation-time, runtime monitoring, recovery, benchmark, etc.
5. **Runtime visibility** — action only, observation + action, hidden state, world model, dynamics model, privileged simulator state, etc.
6. **Three-sentence note**
   - **Problem**: what failure or gap does the work target?
   - **Core idea**: what is the main mechanism?
   - **Why it matters**: what does it change about trustworthy embodied execution?
7. **Representative figure** — preferably the method overview, key result, or taxonomy figure that best communicates the paper.

## Figure naming

Use:

```text
assets/figures/XX_short-paper-slug.png
```

Please keep figures readable at GitHub width, crop surrounding paper text when possible, and avoid screenshots containing unrelated pages.

## Classification rule

The **primary category is defined by the source of non-trustworthiness**, not by the algorithm name.

Examples:

- A *black-box adversarial attack* is still **Malicious Attacks** because an attacker intentionally creates the error.
- A detector that reads only action outputs is **Decision Assurance / Black-box Monitoring** if it detects naturally occurring policy failures.
- Quantization or pruning failures belong to **Soft / Hardware Errors & Robustness** when the degradation is introduced by deployment optimization rather than an attacker.

## Style

Keep descriptions concise, technical, and neutral. Prefer the paper's own terminology and avoid overstating guarantees.
