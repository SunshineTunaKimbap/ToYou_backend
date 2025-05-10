def to_abbr(name: str) -> str:
    """
    Convert a name to its abbreviation (extract the first consonant of each syllable in Korean).
    """
    if not name:
        return ""

    # Define the list of Korean initial consonants (초성)
    CHO_SUNG = [
        'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'
    ]

    abbr = ""
    for char in name:
        # Check if the character is a Hangul syllable
        if '가' <= char <= '힣':
            # Calculate the Unicode offset and extract the 초성 index
            char_code = ord(char) - ord('가')
            cho_index = char_code // 588  # 초성은 588개의 글자 단위로 반복됨
            abbr += CHO_SUNG[cho_index]
        else:
            # Raise an exception if a non-Korean character is found
            raise ValueError(f"Invalid character '{char}' in input. Only Korean characters are allowed.")

    return abbr