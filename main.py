"""Make the AI Judge Laugh: Developer Excuses entry.

Writes one original funny single-line excuse a developer gives when
code breaks in production to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output``). Python 3.13 standard library only; no network,
no randomness, no time or environment dependence -- the output is a
fixed string, so repeated runs are byte-identical.
"""

import os

LINE = "The server didn't crash, it finally read the TODO I'd been ignoring since 2023."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
