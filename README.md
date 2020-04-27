# Twitch Stream Viewer

This is currently targeted at **Valorant Drops Enabled** streams, Valorant is in closed beta, as of writing this. It can be obtained by watching __Drops Enabled__ twitch streams. But what if you cant watch them?

### Then, my tool comes to rescue!

- Just install `xvfb and google-chrome` from your favourite package manager.

- Export `TWITCH_USERNAME` and `TWITCH_PASSWORD` to environment variables.

- Run `pip install selenium xvfbwrapper`

- Run the associated python file, twitch.py, boom!


### How it works?

Valorant reportedly gives drops for people watching a stream more than 2hrs, so this tool watches a stream for exactly 2.1hrs and then gets looping to the next stream. It just keeps rotating on and on till you interrupt it or it somehow fails.
