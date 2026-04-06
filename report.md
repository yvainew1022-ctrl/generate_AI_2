# Report: Meeting Notes to Action Items

## Business Use Case

This project focuses on a common business workflow: converting raw meeting notes into structured action items. In many teams, managers or meeting organizers have to manually review notes after each meeting and summarize who needs to do what by when. This process is repetitive, time-consuming, and often inconsistent. Important tasks can be missed, ownership may remain unclear, and follow-up quality depends on the person writing the summary. Automating a first draft of action items can save time and improve consistency, especially for project managers, team leads, and cross-functional teams.

## Model Choice and Rationale

I chose to use a local large language model through Ollama. The default model used in the prototype is `llama3`, with `mistral` available as an alternative. I chose this setup because it is easy to run locally, avoids API cost, and makes the prototype reproducible without relying on paid external services. In informal testing, the model handled straightforward meeting notes well and produced usable structured outputs. However, performance became less reliable when the notes were messy, multilingual, or incomplete.

## Baseline vs. Final Design

The baseline system used a simple prompt asking the model to extract action items, owners, and deadlines. This worked reasonably well for clean notes, but the model sometimes guessed information when ownership or deadlines were unclear. It also tended to treat some discussion points as action items even when no next step was explicitly stated.

After the first revision, I added rules telling the model not to invent missing details and to label unclear owners or deadlines as “Not specified.” This improved consistency and reduced hallucination. After the second revision, I added stricter formatting rules, clearer instructions to exclude non-actionable discussion, and support for mixed-language notes. The final design produced cleaner, more structured outputs and handled ambiguity more honestly.

Overall, prompt iteration improved the reliability of the system more than the raw fluency of the output. The biggest improvement was not that the model became smarter, but that it became more disciplined.

## Where the Prototype Still Fails

The prototype still struggles in several situations. First, if ownership is only implied rather than directly stated, the model may still produce an uncertain or incomplete output. Second, very messy notes may contain half-formed ideas that are difficult to distinguish from real commitments. Third, multilingual inputs can be partially understood, but nuanced details may still be missed. Finally, vague deadlines such as “soon” or “next week maybe” require judgment that the model cannot always resolve correctly.

Because of these issues, the system still requires human review before action items are shared or relied on in real business settings.

## Deployment Recommendation

I would recommend deploying this workflow only as a first-draft assistant, not as a fully autonomous system. It is valuable for saving time and giving users a structured starting point, but it should not be trusted to make final decisions about ownership or deadlines without review. The safest deployment condition would be a human-in-the-loop workflow where a manager or meeting organizer checks and edits the generated action items before distribution. Under those conditions, the prototype could provide real value while keeping the risk of errors manageable.

