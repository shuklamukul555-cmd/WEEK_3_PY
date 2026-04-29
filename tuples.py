# what is tuple - the collection of immutable (means once created then can't be changed) items 
print("===TUPLE EXAMPLE===")
coordinates = (10.5,20.3,10.5,1,'a')
print("Tuple:",coordinates)
print("First coordinates:",coordinates[0])
x,y,z,p,q = coordinates
print(f"Unpackes: x={x},y={y},z={z},p={p},q={q}")