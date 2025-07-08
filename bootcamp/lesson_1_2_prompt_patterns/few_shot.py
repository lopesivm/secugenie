import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from langchain.prompts import FewShotPromptTemplate, PromptTemplate

from bootcamp.lesson_1_1_langchain_core.ask_llm import ask_llm

examples = [
    {"cve": "CVE-2023-1234", "summary": "Apps crash via malformed libfoo input."},
    {"cve": "CVE-2024-5678", "summary": "SQL injection leaks data in WebAppX."},
    {
        "cve": "CVE-2022-22965",
        "summary": "Spring apps allow remote code execution via crafted HTTP requests.",
    },
    {
        "cve": "CVE-2021-44228",
        "summary": "Attackers can execute code via malicious input in Log4j logs.",
    },
    {
        "cve": "CVE-2020-1472",
        "summary": "Domain takeover via Netlogon flaw allowing unauthenticated access.",
    },
    {
        "cve": "CVE-2017-5638",
        "summary": "Attackers exploit Content-Type header to run code on"
        "Struts servers.",
    },
]

prompt_template = PromptTemplate.from_template("CVE: {cve}\n→Summary: {summary}")

few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=prompt_template,
    suffix="CVE: {input}\n→Summary: ",
    input_variables=["input"],
)

prompt = few_shot_prompt_template.format(input="CVE-2021-45046")

response = ask_llm(
    model_name="mistral",
    message=prompt,
)
print(response)
