EMOJI_DICTIONARY = {
    "a": "🙂",
    "b": "😊",
    "c": "😃",
    "d": "😉",
    "e": "😍",
    "f": "😘",
    "g": "😚",
    "h": "😜",
    "i": "😝",
    "j": "😎",
    "k": "😏",
    "l": "😒",
    "m": "😞",
    "n": "😔",
    "o": "😟",
    "p": "😕",
    "q": "😣",
    "r": "😖",
    "s": "😫",
    "t": "😩",
    "u": "😤",
    "v": "😠",
    "w": "😡",
    "x": "😶",
    "y": "😐",
    "z": "😑",
    "0": "😯",
    "1": "😲",
    "2": "😳",
    "3": "😵",
    "4": "😱",
    "5": "😨",
    "6": "😰",
    "7": "😢",
    "8": "😭",
    "9": "😦",
    "!": "😮",
    "@": "😴",
    "#": "😪",
    "$": "😷",
    "%": "😈",
    "^": "👿",
    "&": "😇",
    "*": "🙏",
    "(": "👽",
    ")": "👾",
    "-": "🙈",
    "\n": "\n"
}


def convert_to_emoji(text):
    """
    Convert text to emoji
    """
    return "".join([EMOJI_DICTIONARY.get(c, "🙂") for c in text])


def convert_obj_to_emoji(obj):
    """
    Convert object to emoji
    """
    if isinstance(obj, str):
        return convert_to_emoji(obj.lower())
    elif isinstance(obj, list):
        return [convert_obj_to_emoji(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: convert_obj_to_emoji(value) for key, value in obj.items()}
    else:
        return obj
