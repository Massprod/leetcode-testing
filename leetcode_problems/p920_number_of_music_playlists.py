# Your music player contains n different songs.
# You want to listen to goal songs (not necessarily different) during your trip.
# To avoid boredom, you will create a playlist so that:
#   Every song is played at least once.
#   A song can only be played again only if k other songs have been played.
# Given n, goal, and k, return the number of possible playlists that you can create.
# Since the answer can be very large, return it modulo 10 ** 9 + 7.
# ------------------
# 0 <= k < n <= goal <= 100


def num_music_playlists(n: int, goal: int, k: int) -> int:
    # working_sol (36.84%, 36.84%) -> (89ms, 17.2mb)  time: O(m * n) | space: O(m * n)
    # Cull calculation time.
    modulus: int = 10 ** 9 + 7
    playlists: list[list[int]] = [[-1 for _ in range(n + 1)] for _ in range(goal + 1)]

    # y -> length of a playlist.
    # x -> number of unique songs.
    def playlists_num(y, x):
        # Empty playlist with 0 songs,
        # there's only 1 way to create == 1.
        if y == 0 and x == 0:
            return 1
        # We can't build playlist with 0 length and more than 0 songs.
        # And we can't build playlist with 1+ length and 0 songs.
        if y == 0 or x == 0:
            return 0
        # Reuse stored.
        if playlists[y][x] != -1:
            return playlists[y][x]
        # Last case -> x == 0 , y == 0 => return first playlist option == 1.
        # prev_call => (n - (1 - 1) => we can use (n) songs with it, standard
        # combinations 1 * n -> first playlist with all unique songs used at least once.
        # For every backwards call we're going to have -1 to unique song options.
        # Multiply playlist_combinations by unique_songs == (n - (x - 1)).
        playlists[y][x] = (playlists_num(y - 1, x - 1) * (n - (x - 1)))
        # If we already used more songs than repeat_limit == K.
        if x > k:
            # We can reuse previous unique_songs == (x - k).
            # used x == 4 and k == 3,
            # we can reuse 1st song after this K played => (4 - 3) == (x - k)
            playlists[y][x] += (playlists_num(y - 1, x) * (x - k))
        # ! Since the answer can be very large, return it modulo 10 ** 9 + 7 !
        playlists[y][x] %= modulus
        return playlists[y][x]

    return playlists_num(goal, n)


# Time complexity: O(m * n) -> creating and traversing with recursion whole matrix, once => O(m * n).
# m - input == goal^^|
# n - input == n^^|
# Auxiliary space: O(m * n) -> creating and using same matrix with rows == m, cols == n => O(m * n).


test_n: int = 3
test_goal: int = 3
test_k: int = 1
test_out: int = 6
assert test_out == num_music_playlists(test_n, test_goal, test_k)

test_n = 2
test_goal = 3
test_k = 0
test_out = 6
assert test_out == num_music_playlists(test_n, test_goal, test_k)

test_n = 2
test_goal = 3
test_k = 1
test_out = 2
assert test_out == num_music_playlists(test_n, test_goal, test_k)
