from app.models.package import Package


def score_package(
    package: Package,
    extraction: dict
):
    score = 0

    destination = (
        extraction.get(
            "destination",
            ""
        )
        .lower()
    )

    if "kerala" in destination:
        score += 40

    budget = extraction.get(
        "budget"
    )

    if budget:
        score += 30

    nights = extraction.get(
        "nights"
    )

    if nights:
        score += 20

    must_have = (
        extraction.get(
            "must_have",
            ""
        )
        .lower()
    )

    if "houseboat" in must_have:
        score += 10

    return score


def get_best_packages(
    packages,
    extraction
):
    scored_packages = []

    for package in packages:

        score = score_package(
            package,
            extraction
        )

        scored_packages.append(
            {
                "id": package.id,
                "title": package.title,
                "slug": package.slug,
                "score": score
            }
        )

    scored_packages.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_packages[:3]