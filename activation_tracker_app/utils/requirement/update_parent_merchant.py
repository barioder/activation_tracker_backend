from django.db.models import Count, Q
def update_parent_merchant(instance ) -> None:

    merchant = instance.merchant
    reqs = merchant.requirements.all()

    counts = reqs.aggregate(
        pending=Count("requirement_id", filter=Q(status="PENDING")),
        uploaded=Count("requirement_id", filter=Q(status="UPLOADED")),
        approved=Count("requirement_id", filter=Q(status="APPROVED")),
        rejected=Count("requirement_id", filter=Q(status="REJECTED")),
        total=Count("requirement_id"),
    )

    # DEFINE STUCK LOGIC
    if counts["rejected"] > 0:
        merchant.is_stuck = True

        rejected_comments = reqs.filter(
            status="REJECTED"
        ).exclude(comment__isnull=True).exclude(comment="")

        reasons = [r.comment for r in rejected_comments]

        merchant.stuck_reason = (
            ", ".join(reasons)
            if reasons
            else "Documents rejected"
        )

    else:
        merchant.is_stuck = False
        merchant.stuck_reason = ""

    # DEFINE STATUS LOGIC
    if counts["approved"] == counts["total"] and counts["total"] > 0:
        merchant.onboarding_status = "ACTIVATED"

    elif counts["rejected"] > 0:
        merchant.onboarding_status = "REJECTED"

    elif counts["uploaded"] > 0 or counts["approved"] > 0:
        merchant.onboarding_status = "REVIEW"

    else:
        merchant.onboarding_status = "REQUEST"

    merchant.save(
        update_fields=[
            "is_stuck",
            "stuck_reason",
            "onboarding_status",
        ]
    )