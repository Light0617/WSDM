def all_zero(data):
	return 0

def listen_old_song(x,table,users,songs):
    x = x.split(',')
    user, song = users.get(x[1], -1), songs.get(x[2], -1)
    if user == -1 or song == -1:
        return 0
    elif song in table[user]:
        return 1
    else:
        return 0

def listen_old_singer(x,table,users,songs, song_to_singer, user_to_singer):
    x = x.split(',')
    user, song = x[1], x[2]
    singer = song_to_singer.get(song)
    favorite_singers = user_to_singer.get(user, set([]))
    if singer in favorite_singers:
        return 1
    else:
        return 0


