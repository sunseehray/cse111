"""Compute the storage efficiency of cans"""
import math

def main():
    # open text file
    with open('can_sizes.txt') as f:
        next(f)
        for line in f:
            clean_line = line.strip()
            parts = clean_line.split(sep=",")
            name = parts[0]
            radius = float(parts[1])
            height = float(parts[2])
            cost = float(parts[3])

            # print(f'{name} {radius}cm {height}cm {cost}cm')
            volume = compute_volume(radius, height)
            surface_area = compute_surface_area(radius, height)
            storage_efficiency = compute_storage_efficiency(volume, surface_area)

            print(f'{name} {storage_efficiency:.2f}')
    # calculate efficiency for each can

    # print results

def compute_volume(radius, height):
    """Compute the volume of a cylinder
        Parameters:
            radius: radius of the cylinder
            height: height of the cylinder
        Return value:
            volume: volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    """Compute the surface area of a cylinder
        Parameters:
            radius: the radius of the cylinder
            height: the height of the cylinder
        Return value:
            surface_area: the surface area of the cylinder
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    """Compute the storage efficiency of a can
        Parameters:
            volume: volume of the can
            surface_area: surface area of the can
        Return value:
            storage_efficiency: storage efficiency of the can
    """
    storage_efficiency = volume / surface_area
    return storage_efficiency

main()