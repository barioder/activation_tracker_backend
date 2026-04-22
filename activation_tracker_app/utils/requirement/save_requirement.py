def save_requirement(instance) -> None:
    """
    Custom save logic for requirement model to automatically update the parent Merchant's 
    status and stuck reason whenever a requirement changes.
    """

    # 1. Update the status to 'UPLOADED' if a file was just added
    if instance.requirement_type and instance.status == 'PENDING':
        instance.status = 'UPLOADED'






