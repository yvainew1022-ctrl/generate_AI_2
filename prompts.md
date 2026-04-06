# Prompt Iteration

## Initial Version

```text
You are a professional meeting assistant. 
Your job is to read raw meeting notes and extract clear, structured action items.

For each action item, provide:
- What needs to be done
- Who is responsible (if mentioned)
- Deadline (if mentioned)

Format your output as a numbered list. Be concise and professional.
```

### What changed and why

This was the baseline prompt. It gave the model a clear role and basic output format, but it did not explain how to handle unclear ownership, missing deadlines, or ambiguous notes.

### What improved, stayed the same, or got worse

It worked well on simple and clean meeting notes. However, for messy or incomplete notes, the output could become inconsistent or too vague.

---

## Revision 1

```text
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

I added explicit rules for missing information and instructed the model not to invent details. This was meant to reduce hallucination and make outputs more consistent across edge cases.

### What improved, stayed the same, or got worse

This revision improved reliability, especially when owners or deadlines were missing. The model became less likely to guess. However, some outputs became a little more rigid and less natural.

---

## Revision 2

```text
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

I added stronger formatting, clarified that discussion points should not automatically become action items, and added instructions for mixed-language notes and ambiguity.

### What improved, stayed the same, or got worse

This version produced the most consistent and professional results. It handled multilingual and unclear notes better than the earlier versions. It still struggled when the notes were very messy or when ownership was only implied rather than stated.
