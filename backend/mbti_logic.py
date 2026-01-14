import random
from data import RESULTS

def calculate_result(answers: list[str]):
    key = "".join(answers)

    result = RESULTS.get(
        key,
        {
            "type": "무난한 직장인",
            "menus": ["백반", "제육볶음"]
        }
    )

    return {
        "mbti": key,
        "type": result["type"],
        "menu": random.choice(result["menus"])
    }
