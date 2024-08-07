i have created the following prompt that has three sections: A,B,C. The idea behind this partition is to have a prompt that will firt output a smalll amount of text, then output a large amount of text, while improved then output another large amount of text, improved. Becasue of this structure, the process of generating synthetic data is manual and requires a lot of human intervention. Typically, I would paste this prompt in chat gpt and then manually copy the output into a new file. However, I would want to stop doing this manually and instead generate an optimal prompt, desing for an API call to GPT4o. Could you please generate this prompt for me? optimal prompt specs: It has to have all the requirments across A,B,C while avoiding overloading the prompt with too many words.

# A

``` txt
prompt = f"""

    Workers Compensation Board of Manitoba manages claims by reviewing incident descriptions submitted by workers. Claim coders review the incident description and populate a database with certain values based on predefined codes by AWCBC. One of the fields in the database is InjurySource, which identifies the source of the injury described in the incident.

  

    Here is the specification for the database fields related to InjurySource:

  

    DATABASE SPEC:

    Sometimes the InjurySource is composed of multiple terms, such as "Truck, uns.". They are actually one single code as long as inside a double quotation mark.

"IncidentDescription": "A description of the incident provided by the worker.",

    "Chain of Thought": "A reasoning towards determining the InjurySource.",

    "InjurySource": "The source of the injury inferred from the incident description." Examples of predefined codes include Grates, Tools, Machinery, Chemicals, Cart, dolly, handtruck, etc."

  

    Determining the InjurySource involves analyzing the context, identifying key objects or actions described, and logically inferring the most relevant predefined code. Consider the specific details provided, such as the type of objects involved, the actions taken, and the resulting injury. Look for hints or cues, tools, substances, or equipment that could logically be linked to the injury source.
    Here are some examples of how incident descriptions are mapped to InjurySource, with logical reasoning from an expert claim coder:

  

    IncidentDescription: "I was walking across the factory floor when I slipped on a wet patch, falling and hitting my head on the concrete. My colleague helped me up, and I was taken to the emergency room for a check-up."

    Chain of Thought: The mention of the factory floor and the act of slipping suggests that the injury source is related to the floor itself. The description provides clues about the environment and the cause of the injury.

    InjurySource: "Floor of building"
    IncidentDescription: "During my shift, I was moving several large crates into the storage area. One of the crates slipped from my grasp and landed on my foot, causing severe pain and swelling. I reported the incident and went to the clinic for an X-ray."

    Chain of Thought: The involvement of crates being moved and the subsequent injury from one falling highlights "Boxes, crates, cartons" as the injury source. The scenario indicates handling of these items as the direct cause.

    InjurySource: "Boxes, crates, cartons"

  

    IncidentDescription: "While attempting to lift a heavy box from a high shelf, I twisted my body awkwardly, resulting in a sharp pain in my back. I immediately stopped working and informed my supervisor. I sought medical attention shortly after."
   Chain of Thought: The description of bodily motion, specifically the twisting movement while lifting, indicates that the injury source is related to the worker's motion or position. This scenario emphasizes physical exertion leading to injury.

        InjurySource: "Bodily motion or position of injured, ill worker"

  

    IncidentDescription: "After cleaning a patient’s room who had a viral infection, I began to feel unwell myself. A few days later, I was diagnosed with the same viral infection and had to take sick leave."

    Chain of Thought: The context of working with a patient who has a viral infection and the subsequent illness indicates that the source of the injury is biological, specifically "Viruses". This inference is based on the transmission scenario described.

    InjurySource: "Viruses"
    --------

  

    You are given an injury source, and your goal is to generate a synthetic dataset that resembles a real-world representation of the incident data. The incident descriptions MUST:

    1. Vary SIGNIFICANTLY in detail, clarity, and language style from other previous synthetic data to reflect the diversity of real-world submissions.

    2. Include scenarios where the injury source must be inferred from the context, even if not explicitly stated.

    3. Present complex situations involving multiple objects or actions, requiring nuanced inference to identify the correct injury source.

Your response should be a JSON array with {num_entries} entries, each containing the keys "IncidentDescription", "Chain of Thought", and "InjurySource". The injury source in "Chain of Thought" should be selected from predefined codes.

  

    Respond with only the JSON array and nothing else.

    InjurySource: {injury_source}

    """

injury_source = "Cart, dolly, handtruck"

num_entries = 10
```


# B  

``` txt 
Generate 35 more, but remember this time to avoid using the same words and vocabularies or other linguistic patterns. Rather, use a wider, more diverse, and high variance vocabs and phrases with synonyms and other INDIRECT indicators such that one would INFER that InjurySource is =="Metal chips, particles"==. The most important thing, howeever, is that you should generate these data such that it won't be confused with "Cart, dolly, handtruck"

```

# C

``` txt
Generate 30 more, but remember this time to also use varying situations. avoid using always the same locations. IMPORTANT: Make the chain of thought reasoning more nuanced, grounded in experience, domain specific knowledge and standards of claim coding. Act as an experience claim coder with over 2 decades of experience. The reasoning MUST have the high complexity of an experience claim coder with over 2 decades of experience. Also important: Make the incident descriptions lengthier and more challenging.
```
