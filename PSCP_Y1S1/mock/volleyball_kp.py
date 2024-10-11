"""Volleyball"""
def winner(stats_winner_team_a, stats_winner_team_b, value):
    """winner function"""
    return stats_winner_team_a >= value or stats_winner_team_b >= value

def is_not_deal_mode(stats_winner_team_a, stats_winner_team_b):
    """not deal mode"""
    return abs(stats_winner_team_a - stats_winner_team_b) >= 2

def main():
    """Volleyball"""
    value = input() + " "
    stats_winner_team_a = 0
    stats_winner_team_b = 0
    stats_round_team_a = 0
    stats_round_team_b = 0
    string_builder = ""
    increment = 0
    finished = False
    while len(value) != 0:
        for text in value:
            if winner(stats_winner_team_a, stats_winner_team_b, 25) \
                and is_not_deal_mode(stats_winner_team_a, stats_winner_team_b) and increment <= 3:
                finished = True
                break
            if winner(stats_winner_team_a, stats_winner_team_b, 15) \
                and is_not_deal_mode(stats_winner_team_a, stats_winner_team_b) and increment == 4:
                finished = True
                break
            if text == "A":
                stats_winner_team_a = stats_winner_team_a + 1
            elif text == "B":
                stats_winner_team_b = stats_winner_team_b + 1
            string_builder = string_builder + text
        increment = increment + 1
        if stats_winner_team_a > stats_winner_team_b:
            stats_round_team_a = stats_round_team_a + 1
        else:
            stats_round_team_b = stats_round_team_b + 1
        if increment <= 5:
            print(f"Set {increment}: A ({stats_winner_team_a}) | B ({stats_winner_team_b})")
        value = value.replace(string_builder, "", 1)
        if increment >= 4 and finished and stats_round_team_a-stats_round_team_b != 0 \
            or (abs(stats_round_team_a-stats_round_team_b) == 3):
            print(f"A won {stats_round_team_a}:{stats_round_team_b} set"%(stats_round_team_a, stats_round_team_b)*(stats_round_team_a > stats_round_team_b)+"B won %d:%d set"%(stats_round_team_b, stats_round_team_a)*(stats_round_team_a < stats_round_team_b))
            break
        #Set to default at all!
        finished = False
        stats_winner_team_a = 0
        stats_winner_team_b = 0
        string_builder = ""
    if not finished:
        print("The game has not finished yet.")
main()
