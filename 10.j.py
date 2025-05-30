import math

# Lambda function to calculate the volume of a cone
volume_of_cone = lambda r, h: (1/3) * math.pi * r**2 * h

# Example usage
radius = 5
height = 10
volume = volume_of_cone(radius, height)
print(f"The volume of the cone is: {volume} cubic units")
