"""This is entrypoint function that creates a prompt for ChatGPT
and obtains a response (an exam question) from it for a given topic
"""

import os
from datetime import datetime

from utils.chatgpt_prompt_utils import get_exam_questions_as_list


openai.api_key = os.getenv("OPENAI_API_KEY", None)


def get_session_id():
    """Generates a unique session ID based on the current date and time.

    This function returns a string representation of the current date and time in the
    "YYYY-MM-DD_HHMMSS" format. This can be used as a unique identifier for individual
    sessions or events in a system, as it changes every second.

    Returns:
        str: A string representing the current date and time in the "YYYY-MM-DD_HHMMSS" format.

    Example:
        >>> get_session_id()
        '2023-07-24_142730'
    """

    return datetime.now().strftime("%Y-%m-%d_%H%M%S")

import openai

if __name__ == "__main__":
    course = "Computer Science"
    chapter = "Algorithms"
    topic = "Merge Sort"

    question_list = get_exam_questions_as_list(course, chapter, topic)