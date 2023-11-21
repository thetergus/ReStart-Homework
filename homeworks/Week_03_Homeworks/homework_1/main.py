from dto.itemOrigin import ItemOrigin
from dto.inventoryItem import  InventoryItem

def main():
    item_origin = ItemOrigin(country="Ethiopia", production_date= "02/12/2023")
    my_item1=InventoryItem(name="Prita",
                           quantity=5,
                           serial_num="a53r3ge",
                           origin=item_origin)
    my_serialized_object = my_item1.__dict__
    print(f'serialized obj: {my_serialized_object}')
    my_item2 =InventoryItem(**my_serialized_object)
    print(f'my item 2       {my_item2.__dict__}')

if __name__=="__main__":
    main()