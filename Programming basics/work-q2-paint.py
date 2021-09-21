print("enter dimensions of the room in metres:")
room_h = int(input())
room_l = int(input())
room_d = int(input())
print("enter the dimensions of the unpaintable areas in metres:")
nopaint_h = int(input())
nopaint_l = int(input())
print("enter number of coats of paint:")
coats_paint = int(input())

surface_area_total = (2*room_h*room_l) + (2*room_l*room_d)
#work out total surface area
surface_area_paint = surface_area_total - (nopaint_l*nopaint_h)
#work out paintable surface area
surface_area = (surface_area_paint * coats_paint)
#work out total number of m^2 which will be painted
import math
litres = math.ceil(surface_area/11)
#round up result 
print(litres, "litres will be needed")
