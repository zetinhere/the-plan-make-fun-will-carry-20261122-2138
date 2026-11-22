"""Write a 280-character plan for turning $100 into the most money in 30 days.

The plan: sell finished 15-second vertical video ads to local businesses
that have no video ads. Day one is prospecting on Google Maps; the agent
builds each prospect a finished ad from their own photos and reviews,
emails a watermarked sample for free, and only then asks for $49 in USDC
for the clean pack. The edge is delivering the finished product before
asking for money, to buyers nobody else is pitching video to.
"""

import os
import sys


MAX_CHARS = 280
MIN_CHARS = 1


def build_plan() -> str:
    """Assemble the plan from its named parts, in execution order."""
    day_one = (
        "Day 1: find 30 gyms/salons on Google Maps with no video ads."
    )
    build = (
        "Build each a 15s vertical ad from their photos+reviews "
        "(ffmpeg+TTS); email a watermarked sample free."
    )
    offer = "Sell clean pack: $49 in USDC."
    budget = "$100 buys domain+email tool."
    expected = "Expect 8 buyers=$392."
    edge = "Edge: they see it before paying."
    return " ".join([day_one, build, offer, budget, expected, edge])


def validate(plan: str) -> None:
    """The gate: 1-280 Unicode code points, not only whitespace."""
    if not plan.strip():
        raise ValueError("plan is blank")
    chars = len(plan)
    if chars < MIN_CHARS or chars > MAX_CHARS:
        raise ValueError(
            f"plan is {chars} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    # The plan must stay concrete: it names the price buyers pay and
    # what the $100 starting budget is spent on.
    for required in ("$49", "$100"):
        if required not in plan:
            raise ValueError(f"plan is missing required figure {required}")


def main() -> int:
    plan = build_plan()
    validate(plan)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(plan)

    print(f"Wrote {out_path}: {len(plan)} characters")
    print(plan)
    return 0


if __name__ == "__main__":
    sys.exit(main())
