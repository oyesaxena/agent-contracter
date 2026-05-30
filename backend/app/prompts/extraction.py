EXTRACTION_PROMPT = """
You are an information extraction expert.

Extract:

- parties
- effective_date
- expiration_date
- contract_value
- obligations

Return valid JSON only.

Document:

{document}
"""