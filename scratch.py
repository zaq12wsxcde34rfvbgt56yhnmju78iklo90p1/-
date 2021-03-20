def make_map():
    game_map = []
    for i in range(9):
        game_map.append("-")
    return game_map

def print_map(_map):

    print(nk_map[0] + '|' + nk_map[1] + '|' + nk_map[2])
    print('-----')
    print(nk_map[3] + '|' + nk_map[4] + '|' + nk_map[5])
    print('-----')
    print(nk_map[6] + '|' + nk_map[7] + '|' + nk_map[8])

nk_map = make_map()

a = 'o'
b = 'x'

for i in range(9):

    while True:
        num = int(input("Enter the your pusition : "))
        if nk_map[num] == "-":
            nk_map[num] = a
            break


print_map(nk_map)
'''
b = 'x'

while True:
    num = int(input("Enter the your pusition : "))
    if nk_map[num] == "-":
        nk_map[num] = b
        print_map(nk_map)
        break
'''





"""
def make_map():
    game_map = []
    for i in range(9):
        game_map.append("#")
    return game_map

def print_map(game_map):

    print(game_map[0] +"|"+ game_map[1] +"|"+ game_map[2])
    print("------")
    print(game_map[3] +"|"+ game_map[4] +"|"+ game_map[5])
    print("------")
    print(game_map[6] +"|"+ game_map[7] +"|"+ game_map[9])


game_map = make_map()

a = "o"

position = int(input("Enter the position"))
game_map[position] = a
make_map()
print_map()
"""









































"사당귀를 보고 있으면 항상 궁금한 사실이 있지"
"현주엽님은 왜 인성이 글러먹었을까?"
"혹시 이런건 아닐까?"
"악마한테 농구실력이랑 인성을 교환한건 아닌지?"
"그게 아니라면 왜 대선배한테도 무례함을 보일 수도 있지?"
"회장도 저러지는 않는데"
"현주엽님과 같이 찍는 광재님과 호영님이 불쌍하다"
"농구 선수들은 다 이러나?"
"이제는 kbs회장분께도 무례하게 대하겠네."
"진짜로 나이를 똥꼬로 드셨죠?"
"실력이 안돼니까 나이로 굴복시키려는 현주엽 클라스"
"애지고요, 지리고요"
"지나가던 박명수님도"
"현주엽한테 꼰대력으로 털리는 각이고요"

