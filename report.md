# Report: Meeting Notes to Action Items

## Business Use Case

This project focuses on a common business workflow: converting raw meeting notes into structured action items. In many organizations, meeting participants or managers must manually summarize notes after meetings and identify follow-up tasks. This process is time-consuming and often inconsistent. Important tasks may be missed, and ownership or deadlines may not be clearly captured. Automating this workflow can improve efficiency, consistency, and clarity in team communication.

## Model Choice and Rationale

This prototype uses a local large language model through Ollama, specifically the `llama3` model. The main reason for this choice is that it allows the system to run locally without requiring paid API access. This makes the project reproducible and easy to run for graders. The model performs well on structured text tasks such as extracting action items, although its performance varies depending on input quality.

## Baseline vs Final Design

The baseline system used a simple prompt asking the model to extract action items, owners, and deadlines. While it worked for clean and structured notes, it often produced inconsistent results when the input was ambiguous. In some cases, the model inferred missing information or treated discussion points as action items.

After the first prompt revision, explicit rules were added to prevent the model from inventing missing details and to label unknown owners or deadlines as "Not specified." This significantly improved consistency and reduced hallucination.

In the second revision, the prompt was further refined by improving formatting, clarifying what qualifies as an actionable task, and adding instructions for handling mixed-language inputs and ambiguity. The final design produced more structured, reliable, and professional outputs, especially on edge cases.

## Limitations and Failure Cases

Despite improvements, the system still has limitations. It struggles when ownership is implied but not explicitly stated. In messy or informal meeting notes, it can be difficult for the model to distinguish between actual commitments and general discussion. Mixed-language inputs are handled reasonably well, but subtle meaning can still be lost. Additionally, vague deadlines such as "soon" or "next week maybe" require human judgment that the model cannot reliably interpret.

Because of these limitations, the system cannot be fully trusted to produce final action items without review.

## Deployment Recommendation

I would recommend deploying this system as a decision-support tool rather than a fully automated solution. It is useful for generating a first draft of action items and saving time, but a human should review and edit the output before it is shared or used for decision-making. Under a human-in-the-loop setup, this tool can provide real value while minimizing the risk of errors.
