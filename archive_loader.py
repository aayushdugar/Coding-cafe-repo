import json
import re
from pathlib import Path


def load_ytd(path):
    """Return the data stored in one archive .js file."""
    text = Path(path).read_text(encoding="utf-8")
    _, separator, payload = text.partition("=")
    if not separator:
        raise ValueError(f"{path!s} does not contain an archive assignment")

    payload = payload.lstrip()
    data, end = json.JSONDecoder().raw_decode(payload)
    trailing = payload[end:].strip()
    if trailing not in ("", ";"):
        raise ValueError(f"{path!s} contains unexpected content after its JSON data")
    if not isinstance(data, (list, dict)):
        raise ValueError(f"{path!s} must contain a JSON list or object")
    return data


def load_dataset(data_dir, name):
    """Combine name.js and numerically ordered name-partN.js files."""
    data_dir = Path(data_dir)
    base = data_dir / f"{name}.js"
    part_pattern = re.compile(rf"^{re.escape(name)}-part(\d+)\.js$")
    parts = []

    for path in data_dir.glob(f"{name}-part*.js"):
        match = part_pattern.fullmatch(path.name)
        if match:
            parts.append((int(match.group(1)), path))

    paths = ([base] if base.is_file() else []) + [
        path for _, path in sorted(parts, key=lambda item: (item[0], item[1].name))
    ]
    dataset = []
    for path in paths:
        data = load_ytd(path)
        if not isinstance(data, list):
            raise TypeError(f"{path!s} must contain a list of records")
        dataset.extend(data)
    return dataset
