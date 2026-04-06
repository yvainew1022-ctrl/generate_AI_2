import requests

# ── 可修改的提示词（Prompt） ──────────────────────────────
SYSTEM_PROMPT = """You are a professional meeting assistant.
Your job is to read raw meeting notes and extract clear, structured action items.

For each action item, provide:
- What needs to be done
- Who is responsible (if mentioned)
- Deadline (if mentioned)

Format your output as a numbered list. Be concise and professional."""

# ── Ollama 配置 ───────────────────────────────────────────
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "llama3"   # 也可以改成 "mistral"

# ── 测试用的会议记录 ──────────────────────────────────────
MEETING_NOTES = [
    {
        "id": 1,
        "label": "Normal case",
        "text": """
        Meeting: Q2 Planning - April 5
        Attendees: Sarah (PM), Tom (Dev), Lisa (Design)

        Sarah will finalize the project roadmap by April 10.
        Tom needs to fix the login bug before next Friday.
        Lisa is working on new homepage mockups, due April 15.
        Everyone should review the budget proposal before next meeting.
        """
    },
    {
        "id": 2,
        "label": "Edge case - very short notes",
        "text": "Quick sync. John to call client. No deadline set."
    },
    {
        "id": 3,
        "label": "Edge case - no clear owners",
        "text": """
        We talked about the new product launch.
        Someone should write the press release.
        Marketing deck needs updating.
        Website changes also discussed.
        """
    },
    {
        "id": 4,
        "label": "Likely to fail - mixed languages",
        "text": """
        今天开会讨论了项目进度。
        Zhang Wei needs to submit the report by Friday.
        Also discussed: 预算还没有确认，需要跟进。
        """
    },
    {
        "id": 5,
        "label": "Edge case - very long and messy notes",
        "text": """
        OK so we started the meeting at 2pm and there was some small talk first.
        Then we got into the main topics. Revenue is down 10% which is concerning.
        Mike said he would look into why the numbers dropped and report back,
        maybe by end of next week or something like that if possible.
        Also the new hire Sarah starts Monday and someone - probably HR or Tom -
        needs to set up her laptop and accounts. We also need to update the
        employee handbook but nobody was assigned and no date was given.
        Oh and the office party is being planned by Lisa for sometime in May.
        Meeting ended around 3:30pm.
        """
    }
]

def process_meeting(notes_text, label):
    """处理单个会议记录并提取 action items"""
    print(f"\n{'='*60}")
    print(f"Processing: {label}")
    print(f"{'='*60}")

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": f"Please extract action items from these meeting notes:\n\n{notes_text}"
            }
        ],
        "stream": False,
        "options": {
            "temperature": 0.3
        }
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
        data = response.json()

        result = data["message"]["content"]
        print(result)
        return result

    except requests.exceptions.ConnectionError:
        error_msg = (
            "Error: Could not connect to Ollama.\n"
            "Make sure Ollama is installed and running.\n"
            "You can test it with: ollama run llama3"
        )
        print(error_msg)
        return error_msg

    except requests.exceptions.HTTPError as e:
        error_msg = f"HTTP Error: {e}\nResponse: {response.text}"
        print(error_msg)
        return error_msg

    except Exception as e:
        error_msg = f"Unexpected Error: {e}"
        print(error_msg)
        return error_msg

def main():
    print(f"Using model: {MODEL_NAME}")
    print("Saving results to output.txt ...")

    output_lines = []

    for case in MEETING_NOTES:
        result = process_meeting(case["text"], case["label"])
        output_lines.append(f"\n## Case {case['id']}: {case['label']}\n")
        output_lines.append(result)
        output_lines.append("\n")

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("# Meeting Notes → Action Items Results\n")
        f.writelines(output_lines)

    print("\n✅ Done! Results saved to output.txt")

if __name__ == "__main__":
    main()
