import json
import asyncio
from typing import List
import logging
from pydantic import BaseModel
import instructor
from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
from openai import AzureOpenAI


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



load_dotenv()

api_key = os.getenv("AZURE_OPENAI_API_KEY")
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")


azure_client = AzureOpenAI(
    api_key=api_key,
    api_version="2024-02-01",
    azure_endpoint=endpoint,
)

deployment_name = "WHI"

client = instructor.patch(azure_client)

class WorkersCompClaim(BaseModel):
    incident_description: str
    chain_of_thought: str
    injury_source: str

class ClaimGenerationError(Exception):
    pass


async def generate_claims(injury_source: str, num_entries: int) -> List[WorkersCompClaim]:
    prompt = f"""
    Generate {num_entries} workers compensation claims related to the injury source: "{injury_source}".
    
    Each claim should include:
    1. An incident description written as if by the injured worker. Vary in detail, clarity, and style. Include complex scenarios with multiple objects/actions.
    2. Expert reasoning (20+ years experience) towards determining the InjurySource. Use nuanced, domain-specific knowledge and claim coding standards.
    3. The determined injury source, using predefined AWCBC codes.

    Guidelines:
    - Ensure incident descriptions genuinely resemble reports written by workers, not professionals.
    - Vary vocabulary, phrases, and linguistic patterns significantly.
    - Use indirect indicators that allow inference of the injury source.
    - Include diverse locations and situations.
    - Make incident descriptions lengthier and more challenging over time.
    - Ensure expert-level complexity in the reasoning.

    Do not use placeholder text or repeat the same claim multiple times.
    """

    try:
        claims = client.chat.completions.create_iterable(
            model="gpt-4o",
            response_model=WorkersCompClaim,
            messages=[{"role": "user", "content": prompt}],
        )
        return [claim async for claim in claims]
    except Exception as e:
        logger.error(f"Error generating claims: {str(e)}")
        return []

async def create_synthetic_dataset(injury_source: str, num_entries: int) -> List[WorkersCompClaim]:
    try:
        return await generate_claims(injury_source, num_entries)
    except Exception as e:
        logger.error(f"Unexpected error creating dataset: {str(e)}")
        raise ClaimGenerationError("Failed to create synthetic dataset") from e

def save_dataset(dataset: List[WorkersCompClaim], filename: str):
    with open(filename, "w") as f:
        json.dump([claim.dict() for claim in dataset], f, indent=2)


async def main():
    injury_source = "Metal chips, particles"
    num_entries = 5

    try:
        synthetic_dataset = await create_synthetic_dataset(injury_source, num_entries)
        save_dataset(synthetic_dataset, "synthetic_workers_comp_claims.json")
        logger.info(f"Generated {len(synthetic_dataset)} WorkersCompClaims.")
        logger.info("Dataset saved as 'synthetic_workers_comp_claims.json'")
    except Exception as e:
        logger.error(f"An error occurred during dataset creation: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())