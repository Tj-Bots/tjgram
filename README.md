<p align="center">
    <a href="https://github.com/tj-bots/tjgram">
        <b>tjgram</b>
    </a>
    <br>
    <b>Telegram MTProto API Framework for Python</b>
    <br/>
    <br/>
    <a href="https://pypi.python.org/pypi/tjgram">
        <img src="https://img.shields.io/pypi/v/tjgram.svg?logo=pypi&logoColor=white" alt="PyPI package version">
    </a>
    <a href="https://pypi.python.org/pypi/tjgram">
        <img src="https://img.shields.io/pypi/l/tjgram.svg" alt="License">
    </a>
    <a href="https://pypi.python.org/pypi/tjgram">
        <img src="https://img.shields.io/pypi/pyversions/tjgram.svg" alt="Python versions">
    </a>
</p>

## tjgram

> Elegant, modern and asynchronous Telegram MTProto API framework in Python for users and bots

tjgram is an actively maintained pyrogram fork for Python designed as a drop-in replacement for Pyrogram, tjgram provides support for the latest Telegram features including Gifts, Stories, Topics, Business Accounts, and more.

```python
from pyrogram import Client, filters

app = Client("my_account")


@app.on_message(filters.private)
async def hello(client, message):
    await message.reply("Hello from tjgram!")


app.run()
```

**tjgram** is a modern, elegant and asynchronous MTProto API framework. It enables you to easily interact with
the main Telegram API through a user account (custom client) or a bot identity (bot API alternative) using Python.

### Key Features

- **Ready**: Install tjgram with pip and start building your applications right away.
- **Easy**: Makes the Telegram API simple and intuitive, while still allowing advanced usages.
- **Elegant**: Low-level details are abstracted and re-presented in a more convenient way.
- **Fast**: Boosted up by [TgCrypto](https://github.com/pyrogram/tgcrypto), a high-performance cryptography library written in C.
- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.
- **Async**: Fully asynchronous (also usable synchronously if wanted, for convenience).
- **Powerful**: Full access to Telegram's API to execute any official client action and more.

### Installing

Stable version

``` bash
pip install tjgram
```

Dev version

``` bash
pip install https://github.com/tj-bots/tjgram/archive/dev.zip --force-reinstall
```

### Acknowledgements

tjgram is a fork of [Kurigram](https://github.com/KurimuzonAkuma/kurigram), itself a fork of [Pyrogram](https://github.com/pyrogram/pyrogram).
Credit for the vast majority of this codebase goes to their respective authors and maintainers.
