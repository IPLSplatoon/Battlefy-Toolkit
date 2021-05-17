# Battlefy-Toolkit
A toolkit to download Battlefy data made by Inkling Research Labs (IPL).
Code on [Github](https://github.com/IPLSplatoon/Battlefy-Toolkit).

## Requirements
- Python 3.9+

## DiscordIdResolver
- Can translate a Discord Id to information.
- If multiple requests are to be made, a single DiscordIdResolver should be created and resolve_discord_id called multiply. 
```python
if __name__ == '__main__':
    resolver = DiscordIdResolver(BOT_TOKEN)
    info1 = resolver.resolve_discord_id(97288493029416960)
    info2 = resolver.resolve_discord_id(763492840038465537)
    print(info1.qualified_username)
    print(info2.qualified_username)
```
