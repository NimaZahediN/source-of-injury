

def generate_workers_comp_claims(injury_source, num_entries):
    prompt = f"""
Generate a synthetic dataset of {num_entries} workers compensation claims related to the injury source: "{injury_source}". Each entry should include:

1. "IncidentDescription": Written as if by the injured worker. Vary in detail, clarity, and style. Include complex scenarios with multiple objects/actions. The injury source may need to be inferred. Resemble authentic, real-world submissions with natural language and potential inconsistencies.

2. "ChainOfThought": Expert reasoning (20+ years experience) towards determining the InjurySource. Use nuanced, domain-specific knowledge and claim coding standards.

3. "InjurySource": The determined source, using predefined AWCBC codes.

Guidelines:
- Ensure incident descriptions genuinely resemble reports written by workers, not professionals.
- Vary vocabulary, phrases, and linguistic patterns significantly.
- Use indirect indicators that allow inference of the injury source.
- Include diverse locations and situations.
- Make incident descriptions lengthier and more challenging over time.
- Ensure expert-level complexity in the reasoning.

Respond with a JSON array of {num_entries} entries, each containing the three keys mentioned above. No additional text.

Example structure:
[
    {
        "IncidentDescription": "I was adjusting the load on a dolly when it tipped over unexpectedly, and I had to catch it quickly, resulting in a shoulder strain.",
        "Chain of Thought": "The injury occurred while handling a dolly and dealing with its instability, pointing to the dolly as the main source of the injury.",
        "InjurySource": "Cart, dolly, handtruck"
    },
  ...
]
"""
    return prompt

# Usage
injury_source = "Metal chips, particles"
num_entries = 75
optimized_prompt = generate_workers_comp_claims(injury_source, num_entries)