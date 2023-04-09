def solution(players, callings):
    idx_dic = {i: player for i,player in enumerate(players)}
    player_dic = {player : i for i,player in enumerate(players)}
    for i in callings:
        call_idx = player_dic[i]
        prev_player = idx_dic[call_idx-1]
        player_dic[i]=call_idx-1
        player_dic[prev_player] = call_idx
        idx_dic[call_idx] = prev_player
        idx_dic[call_idx-1] = i
    return list(idx_dic.values())