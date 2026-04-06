# Prompt Iteration

## Initial Version

```text id="0lwmzm"
You are a professional meeting assistant. 
Your job is to read raw meeting notes and extract clear, structured action items.

For each action item, provide:
- What needs to be done
- Who is responsible (if mentioned)
- Deadline (if mentioned)

Format your output as a numbered list. Be concise and professional.
```

### What changed and why

This was the initial baseline prompt. It clearly defined the role of the model and the basic output structure, but it did not explain how to handle ambiguity, missing information, or vague notes.

### What improved, stayed the same, or got worse

It worked reasonably well on clean meeting notes with obvious owners and deadlines. However, on messy or incomplete notes, the model sometimes guessed missing details or produced inconsistent output formatting.

---

## Revision 1

```text id="nf6twq"
You are a professional meeting assistant.
Your task is to read raw meeting notes and extract only clear action items.

For each action item, provide:
1. Task
2. Owner (if mentioned, otherwise write "Not specified")
3. Deadline (if mentioned, otherwise write "Not specified")

Rules:
- Only include items that clearly imply an action.
- Do not invent names, deadlines, or responsibilities.
- If the note is vague, preserve the uncertainty.
- Format the output as a numbered list.
- Keep the wording concise and professional.
```

### What changed and why

In this revision, I added explicit rules for handling missing owners and deadlines. I also told the model not to invent details. The purpose was to reduce hallucination and make the output more consistent across edge cases.

### What improved, stayed the same, or got worse

This revision improved reliability, especially for cases with unclear owners or missing due dates. The model became more disciplined and less likely to over-interpret the notes. On the other hand, some outputs became slightly more rigid and less natural.

---

## Revision 2

```text id="mazz0t"
You are a professional meeting assistant.
Your task is to convert raw meeting notes into structured action items for business follow-up.

For each action item, use this format:
1. Task: ...
   Owner: ...
   Deadline: ...

Rules:
- Extract only actionable follow-up items.
- Do not include general discussion points unless they imply a next step.
- If the owner is unclear, write "Not specified".
- If the deadline is unclear, write "Not specified".
- Do not invent facts.
- If the notes contain mixed languages, extract the action item as accurately as possible in English.
- If human review is needed because the note is ambiguous, keep the item but reflect the uncertainty clearly.
- Keep the output concise, professional, and easy to scan.
```

### What changed and why

In the second revision, I improved the formatting, clarified the difference between discussion points and true follow-up tasks, and added instructions for mixed-language notes and ambiguous cases. This was meant to improve output quality on the most difficult examples in the evaluation set.

### What improved, stayed the same, or got worse

This version produced the most consistent and professional output overall. It handled multilingual and ambiguous notes better than the earlier versions and reduced the chance of turning general discussion into false action items. It still struggled when the notes were extremely messy or when ownership was only implied rather than explicitly stated.
