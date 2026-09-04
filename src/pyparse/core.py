def normalize_space(text: str) -> str:
    return " ".join(text.split())


def parse_pairs(text: str, separator: str = ",") -> dict[str, str]:
    if not separator:
        raise ValueError("separator must not be empty")
    result: dict[str, str] = {}
    for field in text.split(separator):
        field = field.strip()
        if not field:
            continue
        if "=" not in field:
            raise ValueError(f"invalid field: {field!r}")
        key, value = field.split("=", 1)
        key = key.strip()
        if not key:
            raise ValueError("pair key must not be empty")
        result[key] = value.strip()
    return result
