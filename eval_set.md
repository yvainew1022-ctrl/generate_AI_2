# Evaluation Set

This evaluation set is designed to evaluate the workflow of converting raw meeting notes into structured action items. The goal is not to build a large benchmark, but to create a small, stable, and reusable set of test cases for fair comparison across prompt revisions.

---

## Case 1: Normal case

**Input**

```text
Meeting: Q2 Planning - April 5
Attendees: Sarah (PM), Tom (Dev), Lisa (Design)

Sarah will finalize the project roadmap by April 10.
Tom needs to fix the login bug before next Friday.
Lisa is working on new homepage mockups, due April 15.
Everyone should review the budget proposal before next meeting.
```

**What a good output should do**

* Extract all clear action items
* Correctly identify Sarah, Tom, and Lisa as owners
* Preserve deadlines when mentioned
* Include the team review item even though the owner is a group rather than one individual

---

## Case 2: Edge case - very short notes

**Input**

```text
Quick sync. John to call client. No deadline set.
```

**What a good output should do**

* Extract one clear action item
* Identify John as the owner
* Mark the deadline as not specified
* Keep the output concise

---

## Case 3: Edge case - no clear owners

**Input**

```text
We talked about the new product launch.
Someone should write the press release.
Marketing deck needs updating.
Website changes also discussed.
```

**What a good output should do**

* Extract only the items that are clearly actionable
* Avoid inventing names or deadlines
* Mark the owner as not specified when missing
* Treat vague discussion carefully instead of turning every sentence into a confident action item

---

## Case 4: Likely to fail or require human review - mixed languages

**Input**

```text
今天开会讨论了项目进度。
Zhang Wei needs to submit the report by Friday.
Also discussed: 预算还没有确认，需要跟进。
```

**What a good output should do**

* Correctly extract the report submission task
* Capture the budget follow-up as a possible action item if supported by the text
* Handle the mixed Chinese-English notes as accurately as possible
* Avoid hallucinating extra details not stated in the notes
* Preserve uncertainty if the owner of the budget follow-up is not clear

---

## Case 5: Edge case - long and messy notes

**Input**

```text
OK so we started the meeting at 2pm and there was some small talk first.
Then we got into the main topics. Revenue is down 10% which is concerning.
Mike said he would look into why the numbers dropped and report back,
maybe by end of next week or something like that if possible.
Also the new hire Sarah starts Monday and someone - probably HR or Tom -
needs to set up her laptop and accounts. We also need to update the
employee handbook but nobody was assigned and no date was given.
Oh and the office party is being planned by Lisa for sometime in May.
Meeting ended around 3:30pm.
```

**What a good output should do**

* Ignore irrelevant meeting chatter and background details
* Extract the real follow-up tasks only
* Preserve uncertainty where ownership is unclear
* Avoid inventing precise deadlines from vague phrases
* Separate business follow-up items from lower-priority or social planning items when appropriate

---

## Summary

This evaluation set includes:

* one normal case
* multiple edge cases
* one case likely to require human review

It is designed to test whether the system can reliably extract action items, avoid hallucination, and handle ambiguity in a realistic business workflow.
