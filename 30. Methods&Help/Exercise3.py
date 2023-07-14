"""
Check if the sets below form isolated sets (that is, they have no elements in
common), using the isdisjoint() method. Store said result in the isolated_sets
variable:

smartphone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

Search the documentation about the operation of the requested method to find
out how it works and how it functions.

===============================================================================

Verifica si los sets a continuación forman conjuntos aislados (es decir, que no
tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho
resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

Busca en la documentación acerca del funcionamiento del método solicitado para
saber cómo actúa y cómo es su funcionamiento.
"""

smartphone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

tv_brands = {"Sony", "Philips", "Samsung", "LG"}

isolated_sets = smartphone_brands.isdisjoint(tv_brands)


marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)