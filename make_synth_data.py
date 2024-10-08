import json
import asyncio
from typing import List
import logging
from pydantic import BaseModel
import instructor
from openai import AsyncAzureOpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up AsyncAzureOpenAI client
async_azure_client = AsyncAzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

# Patch the AsyncAzureOpenAI client with instructor
async_client = instructor.patch(async_azure_client)

class WorkersCompClaim(BaseModel):
    incident_description: str
    chain_of_thought: str
    injury_source: str

async def generate_claims(
    injury_source: str, 
    num_entries: int, 
    semaphore: asyncio.Semaphore
) -> List[WorkersCompClaim]:
    async with semaphore:
        prompt = f"""
        Generate {num_entries} workers compensation claims related to the injury source: "{injury_source}".
        Each claim should include:
        1. An incident description written as if by the injured worker. Vary in detail, clarity, and style. Include complex scenarios with multiple objects/actions.
        2. Concise expert reasoning (20+ years experience) towards determining the InjurySource. Use nuanced, domain-specific knowledge and claim coding standards. Keep it brief and in third-person perspective.
        3. The determined injury source, using only the name without any codes.

    Guidelines:
    - Treat the provided injury source as a single category, even if it contains multiple words or commas.
    - Ensure incident descriptions genuinely resemble reports written by workers, not professionals.
    - Vary vocabulary, phrases, and linguistic patterns significantly.
    - Use indirect indicators that allow inference of the injury source.
    - Include diverse locations and situations.
    - Make incident descriptions lengthier and more challenging over time.
    - Ensure expert-level complexity in the reasoning, but keep it concise.

    Example:
    For the injury source "Nails, brads, tacks":
    InjurySource: Nails, brads, tacks

    Do not use placeholder text or repeat the same claim multiple times.
    """

        try:
            claims = await async_client.chat.completions.create(
                model="gpt4o-mini",  # Replace with your actual deployment name
                response_model=List[WorkersCompClaim],
                messages=[{"role": "user", "content": prompt}],
            )
            await asyncio.sleep(1)  # Add a 1-second delay after each API call
            return claims
        except Exception as e:
            logger.error(f"Error generating claims for {injury_source}: {str(e)}")
            return []


async def create_synthetic_claims(
    injury_sources: List[str], 
    num_entries: int, 
    max_concurrency: int = 20
) -> List[WorkersCompClaim]:
    semaphore = asyncio.Semaphore(max_concurrency)
    tasks = [generate_claims(source, num_entries, semaphore) for source in injury_sources]
    results = await asyncio.gather(*tasks)
    return [claim for sublist in results for claim in sublist]

async def main():
    injury_sources = [
        "Bags, sacks, totes",
        "Street, road",
        "anks, bins, vats",
        "Vehicle and mobile equipment parts, uns. OR n.e.c.",
        "Student",
        "Nails, brads, tacks",
        "Stairs, steps -- indoors",
        "Dogs",
        "Bars, rods, reinforcing bar (rebar)",
        "Buckets, baskets, pails",
        "Hammers",
        "Tables, worktables",
        "Trailers",
        "Pots, pans, trays",
        "Bus"       
    ]
    num_entries = 2

    claims = await create_synthetic_claims(injury_sources, num_entries)

    # Save the dataset
    with open("synthetic_workers_comp_claims.json", "w", encoding="utf-8") as f:
        json.dump([claim.dict() for claim in claims], f, indent=2, ensure_ascii=False)

    logger.info(
        f"Generated {len(claims)} WorkersCompClaims across {len(injury_sources)} injury sources."
    )
    logger.info("Dataset saved as 'synthetic_workers_comp_claims.json'")

if __name__ == "__main__":
    asyncio.run(main())
