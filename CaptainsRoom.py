k = int(input())
rooms = list(map(int, input().split()))
room_set = set()
sum_rooms = 0
for room in rooms:
    room_set.add(room)
    sum_rooms += room
captain_room = (sum(room_set) * k - sum_rooms) // (k - 1)
print(captain_room)
