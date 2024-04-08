def get_product_image(product):
    image_fields = ["bicycle_images", "accessory_images", "components_images", "equipment_images"]

    for field in image_fields:
        if hasattr(product, field):
            images = getattr(product, field)
            if images.exists():
                return images.first()

    return None