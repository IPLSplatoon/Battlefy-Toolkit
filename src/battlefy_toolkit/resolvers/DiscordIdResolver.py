import json
import time
import requests
from typing import Optional


class DiscordInformation:
    def __init__(self, response: dict):
        """
        Constructor for DiscordInformation
        :param response: Dictionary of the response from Discord.
        """
        self.id = response["id"]
        self.username = response["username"]
        self.discriminator = response["discriminator"]
        self.avatar = response["avatar"]
        self.public_flags = response["public_flags"]

    @property
    def qualified_username(self):
        """Get the username with the discriminator after the #"""
        return self.username + '#' + self.discriminator


class DiscordIdResolver:
    def __init__(self, discord_token: str):
        """
        Constructor for DiscordIdResolver
        :param discord_token: The discord bot token. The token is made up of an alphanumeric string.
        """
        if discord_token:
            self.discord_token = discord_token
        else:
            raise ValueError('discord_token must be specified.')

        self._reset_time = None

    def resolve_discord_id(self, discord_id: int, verbose: bool = False) -> Optional[DiscordInformation]:
        """
        Get Discord information about a specified Discord id.
        :param discord_id: The Discord Id.
        :param verbose: If we should print out results and debug.
        :return: The Discord Information found or None.
        """
        url = 'https://discord.com/api/users/' + discord_id.__str__()
        headers = {'Authorization': 'Bot ' + self.discord_token}

        if self._reset_time is not None:
            now_seconds = int(time.time())
            if self._reset_time >= now_seconds:
                diff = (self._reset_time - now_seconds) + 2
                if verbose:
                    print(f'Sleeping for {diff}s before continuing.')
                time.sleep(diff)
                _reset_time = None

        response = requests.get(url, headers=headers)
        if verbose:
            print(f'{response.status_code}: {response.content}')

        # The number of remaining requests that can be made
        remaining_requests = int(response.headers["X-RateLimit-Remaining"])

        # Epoch time (seconds since 00:00:00 UTC on January 1, 1970) at which the rate limit resets
        reset_time = int(response.headers["X-RateLimit-Reset"])

        if remaining_requests < 3:
            now_seconds = time.time()
            remaining = (reset_time - now_seconds)
            if verbose:
                print(f'{remaining_requests} request(s) remaining ({remaining} seconds till reset).')

            # Setting this will cause us to wait before sending another request.
            if remaining_requests == 0:
                _reset_time = reset_time

        dictionary = json.loads(response.content)
        if verbose:
            print(f"Returning: {dictionary}")
        try:
            return DiscordInformation(dictionary)
        except (KeyError, TypeError):
            return None


# For example:
# if __name__ == '__main__':
    # result = DiscordIdResolver(BOT_TOKEN).backtrace_discord_id(97288493029416960)
    # print(result.qualified_username)
