# Generate exact-path overrides of vanilla 1.13.11 west/east Europe building
# history, bumping only existing AUS/PRU/FRA 1836 industry levels.
# Does not rewrite 01_south_europe.txt (I-03 TUR override).

from pathlib import Path

VANILLA = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game")
MOD = Path(__file__).resolve().parents[1]
BOM = "\ufeff"

FILES = [
    "common/history/buildings/00_west_europe.txt",
    "common/history/buildings/02_east_europe.txt",
]

# Each patch is (relative_file, unique_old, new). old must occur once.
PATCHES = [
    (
        "common/history/buildings/00_west_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_tooling_workshop"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_tooling_workshop"
\t\t\t\t\t\tcountry="c:AUS"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_BOHEMIA"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_tooling_workshop"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_tooling_workshop"
\t\t\t\t\t\tcountry="c:AUS"
\t\t\t\t\t\tlevels=4
\t\t\t\t\t\tregion="STATE_BOHEMIA"
""",
    ),
    (
        "common/history/buildings/00_west_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_iron_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_iron_mine"
\t\t\t\t\t\tcountry="c:AUS"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_STYRIA"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_iron_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_iron_mine"
\t\t\t\t\t\tcountry="c:AUS"
\t\t\t\t\t\tlevels=4
\t\t\t\t\t\tregion="STATE_STYRIA"
""",
    ),
    (
        "common/history/buildings/00_west_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_coal_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_coal_mine"
\t\t\t\t\t\tcountry="c:AUS"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_MORAVIA"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_coal_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_coal_mine"
\t\t\t\t\t\tcountry="c:AUS"
\t\t\t\t\t\tlevels=3
\t\t\t\t\t\tregion="STATE_MORAVIA"
""",
    ),
    (
        "common/history/buildings/00_west_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_tooling_workshop"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_tooling_workshop"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=3
\t\t\t\t\t\tregion="STATE_RHINELAND"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_tooling_workshop"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_tooling_workshop"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=5
\t\t\t\t\t\tregion="STATE_RHINELAND"
""",
    ),
    (
        "common/history/buildings/00_west_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_coal_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_RUHR"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_coal_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=5
\t\t\t\t\t\tregion="STATE_RUHR"
""",
    ),
    (
        "common/history/buildings/00_west_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_iron_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_RUHR"
\t\t\t\t\t}
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_BRANDENBURG"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_iron_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=4
\t\t\t\t\t\tregion="STATE_RUHR"
\t\t\t\t\t}
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_BRANDENBURG"
""",
    ),
    (
        "common/history/buildings/00_west_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_tooling_workshop"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_tooling_workshop"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_BURGUNDY"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_tooling_workshop"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_tooling_workshop"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=4
\t\t\t\t\t\tregion="STATE_BURGUNDY"
""",
    ),
    (
        "common/history/buildings/00_west_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_iron_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_ALSACE_LORRAINE"
\t\t\t\t\t}
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_ILE_DE_FRANCE"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_iron_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=4
\t\t\t\t\t\tregion="STATE_ALSACE_LORRAINE"
\t\t\t\t\t}
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_financial_district"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_ILE_DE_FRANCE"
""",
    ),
    (
        "common/history/buildings/00_west_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_coal_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_coal_mine"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=1
\t\t\t\t\t\tregion="STATE_RHONE"
\t\t\t\t\t}
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_coal_mine"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=1
\t\t\t\t\t\tregion="STATE_RHONE"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_coal_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_coal_mine"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_RHONE"
\t\t\t\t\t}
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_coal_mine"
\t\t\t\t\t\tcountry="c:FRA"
\t\t\t\t\t\tlevels=1
\t\t\t\t\t\tregion="STATE_RHONE"
""",
    ),
    (
        "common/history/buildings/02_east_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_coal_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_coal_mine"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=2
\t\t\t\t\t\tregion="STATE_UPPER_SILESIA"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_coal_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_coal_mine"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=4
\t\t\t\t\t\tregion="STATE_UPPER_SILESIA"
""",
    ),
    (
        "common/history/buildings/02_east_europe.txt",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_iron_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_iron_mine"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=1
\t\t\t\t\t\tregion="STATE_UPPER_SILESIA"
""",
        """\t\t\tcreate_building={
\t\t\t\tbuilding="building_iron_mine"
\t\t\t\tadd_ownership={
\t\t\t\t\tbuilding={
\t\t\t\t\t\ttype="building_iron_mine"
\t\t\t\t\t\tcountry="c:PRU"
\t\t\t\t\t\tlevels=3
\t\t\t\t\t\tregion="STATE_UPPER_SILESIA"
""",
    ),
]


def read_vanilla(relative: str) -> str:
    raw = (VANILLA / relative).read_bytes()
    text = raw.decode("utf-8-sig")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def main() -> None:
    texts = {rel: read_vanilla(rel) for rel in FILES}
    for rel, old, new in PATCHES:
        old_n = old.replace("\r\n", "\n")
        new_n = new.replace("\r\n", "\n")
        n = texts[rel].count(old_n)
        if n != 1:
            raise SystemExit(f"{rel}: patch hit {n} times (want 1)\n---\n{old_n[:200]}")
        texts[rel] = texts[rel].replace(old_n, new_n, 1)

    for rel, text in texts.items():
        dest = MOD / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes((BOM + text.replace("\n", "\r\n")).encode("utf-8"))
        print(f"wrote {rel}")
    print(f"applied {len(PATCHES)} level bumps")


if __name__ == "__main__":
    main()
