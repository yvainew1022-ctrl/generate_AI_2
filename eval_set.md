# Evaluation Set

This evaluation set is designed to test the workflow of converting raw meeting notes into structured action items. It is intentionally small so results are easy to compare fairly across prompt revisions.

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
* Identify Sarah, Tom, and Lisa correctly
* Preserve deadlines when mentioned
* Include the group review item even though the owner is collective

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

* Extract only clearly actionable items
* Avoid inventing owners
* Mark missing owners and deadlines clearly
* Avoid turning vague discussion into overly confident tasks

---

## Case 4: Likely to fail - mixed languages

**Input**

```text
今天开会讨论了项目进度。
Zhang Wei needs to submit the report by Friday.
Also discussed: 预算还没有确认，需要跟进。
```

**What a good output should do**

* Correctly extract the report submission task
* Capture the budget follow-up as an action item if possible
* Avoid hallucinating extra details
* Handle the mixed Chinese-English input appropriately

---

## Case 5: Edge case - very long and messy notes

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

* Ignore irrelevant meeting chatter
* Extract clear action items only
* Preserve uncertainty where ownership is unclear
* Avoid turning every discussion point into a task
* Reflect approximate deadlines carefully without inventing precision

---

## Summary

This evaluation set includes:

* 1 normal case
* multiple edge cases
* 1 case likely to require human review

The purpose is to evaluate whether prompt revisions improve consistency, reduce hallucination, and better handle ambiguity.

