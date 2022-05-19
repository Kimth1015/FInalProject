import marbles.game as r1
import tug_of_war.game as r2
import glass_stepping_stones.game as r3
from participant import computer as com
from participant import my_own_player as player

def report(winner, team, game): #아마 승리자, 승리팀 결과를 엑셀로 작성하는 것 같음
    with open('result_term_project.csv', 'a') as f:  # the file name may change
        # team_num, game, win, defeat, violation, error
        if winner == team.name: #만약 팀의 이름과 team의 name이 같다면
            f.writelines(str(team.team_num) + ', ' + game + ', 1, 0, 0, 0\n') #팀 넘버, 게임, 1, 0, 0, 0 작성
        else:
            f.writelines(str(team.team_num) + ', ' + game + ', 0, 1, 0, 0\n') #팀 넘버, 게임, 0, 1, 0, 0 작성

if __name__ == '__main__':
    computer, team = '', '' #computer와 team에 '' 지정

    # for initialize your own player as a variable
    computer = com.computer() #컴퓨터 객체 생성
    team = player.my_own_player() #

    players = [computer, team]

    winner_name = ''
    print("\n □ : 모든 참가자가 성공적으로 입장하였습니다.\n")

    #print("\n □ : 홀짝게임을 먼저 시작합니다.\n")
    #for i in range(2):
    #    print("\n □ : {}번째 게임을 시작합니다.\n".format(i + 1))
    #    stage = r1.marbles(players)
    #    winner_name = stage.run_game(players)
    #    report(winner_name, team, 'marble')

    #print("\n □ : 다음으로 줄다리기 게임을 시작합니다.\n")
    #for i in range(2):
    #    print("\n □ : {}번째 게임을 시작합니다.\n".format(i + 1))
    #    stage_map = r2.Map(5)
    #    stage = r2.tug_of_war(stage_map, players)
    #    winner_name = stage.run_game(players, stage_map)
    #    report(winner_name, team, 'Tug')

    print("\n □ : 마지막으로 징검다리 게임을 시작합니다.\n")
    for i in range(2):
        print("\n □ : {}번째 게임을 시작합니다.\n".format(i + 1))
        stage_map = r3.Map(20)
        stage = r3.glass_stepping_stones(stage_map, players)
        winner_name = stage.run_game(stage_map)
        report(winner_name, team, 'glass')


