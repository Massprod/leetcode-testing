# TinyURL is a URL shortening service where you enter a URL such as
#  https://leetcode.com/problems/design-tinyurl and it returns a short URL such as
#  http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
# There is no restriction on how your encode/decode algorithm should work.
# You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
#  can be decoded to the original URL.
# Implement the Solution class:
#   - Solution() Initializes the object of the system.
#   - String encode(String longUrl) Returns a tiny URL for the given longUrl.
#   - String decode(String shortUrl) Returns the original long URL for the given shortUrl.
#     It is guaranteed that the given shortUrl was encoded by the same object.
# ---------------------
# 1 <= url.length <= 10 ** 4
# url is guaranteed to be a valid URL.
from random import choice
from string import ascii_letters


class Codec:
    # working_sol (92.29%, 15.09%) -> (29ms, 16.64mb)
    def __init__(self):
        self.all_shorts: dict[str, str] = {}
        self.base: str = 'https://tinyurl.com/'
        self.base_length: int = 1

    def encode(self, long_url: str) -> str:
        cur_length: int = 0
        new_short: str = self.base + ''.join([choice(ascii_letters) for _ in range(self.base_length + cur_length)])
        while new_short in self.all_shorts:
            cur_length += 1
            new_short: str = self.base + ''.join([choice(ascii_letters) for _ in range(self.base_length + cur_length)])
        self.all_shorts[new_short] = long_url
        return new_short

    def decode(self, short_url: str) -> str:
        if short_url in self.all_shorts:
            return self.all_shorts[short_url]
        return ''
