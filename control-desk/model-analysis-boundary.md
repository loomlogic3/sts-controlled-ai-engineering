# Model Analysis Boundary

The repository observer produces facts. A model may interpret those facts, but the interpretation is never authoritative by itself.

## Deterministic facts

These come from Git, the registry, validators, and command exit codes:

- repository path and project ID;
- branch and HEAD commit;
- dirty or clean state;
- changed paths;
- commit IDs, timestamps, and subjects;
- source hashes and observation hashes;
- command, tool version, exit code, and captured output hash.

The same repository state and same observer version should produce the same fact set and state hash. Observation time is metadata and is excluded from the state hash.

## Probabilistic model fields

A local or cloud model may propose:

- likely affected milestone;
- change classification;
- concise summary;
- possible risks;
- missing evidence;
- candidate next action;
- confidence and uncertainty notes.

These fields must be stored separately from facts and labeled `model_proposed`. They require human review before becoming authoritative Markdown records.

## Required model provenance

Every model analysis should record:

- provider and model name;
- model version or runtime identifier;
- temperature and seed when supported;
- prompt-template version;
- input observation hash;
- output hash;
- schema-validation result;
- retry count;
- human review status.

The local STS AI Gateway is a suitable future adapter because it is already loopback-only and fixed to the local llama.cpp server. The adapter must not expose gateway credentials to the browser or allow a model to write repository records directly.

## Where models are weak

- They can infer the wrong milestone from an ambiguous commit.
- They can confuse a changed file with a verified behavior.
- They may miss uncommitted, ignored, generated, or runtime-only state.
- They may summarize incomplete diffs as completed work.
- They can produce different classifications across providers or runs.
- They cannot establish human approval, production readiness, or real-world recovery.
- They may leak sensitive content if given more source material than required.

## Determinism controls

- Use structured JSON schemas and reject invalid output.
- Use temperature `0` where supported, while recognizing this does not guarantee identical output across runtimes.
- Use a fixed prompt template and record its version.
- Provide only the observation bundle and explicitly scoped evidence.
- Hash inputs and outputs.
- Set bounded token, time, and retry limits.
- Compare multiple runs when a model proposal affects risk or state.
- Keep model proposals separate until a human accepts them.
- Prefer deterministic rules for state transitions and gate eligibility.
