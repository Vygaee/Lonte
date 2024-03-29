class TEXTS:
    ABOUT_SONG = (
        "**💬 Title:** __{0}__ \n\n"
        "**📺 Channel:** __{1}__ \n"
        "**🕰 Published:** __{2}__ \n"
        "**🔖 Views:** __{3}__ \n"
        "**⏳ Duration:** __{4}__ \n\n"
        "**❆** {5}"
    )
    ABOUT_USER = (
        "**Top User Info:**\n\n"
        "**💬 Name:** {0}\n"
        "**💠 ID:** `{1}`\n"
        "**⚜️ Level:** __{2}__\n"
        "**🎶 Songs Played:** __{3}__\n"
        "**〥 Joined Since:** __{4}__\n\n"
        "**❆** {5}"
    )
    BOOTED = (
        "#START\n\n"
        "**is alive!**\n\n"
        "__» Stream Version:__ `{1}`\n"
        "__» Python Version:__ `{2}`\n"
        "__» Pyrogram Version:__ `{3}`\n"
        "__» PyTgCalls Version:__ `{4}`\n\n"
        "**</>** {5}"
    )
    PING_REPLY = (
        "**📌 Pinged Bot Server!**\n\n"
        "**🏁 Speed:** __{0} ms__\n"
        "**⏳ Uptime:** __{1}__\n"
        "**🎶 VC Ping:** __{2} ms__"
    )
    PLAYING = (
        "**❆** {0}\n\n"
        "**♪ Song Name:** __{1}__\n"
        "**♪ Duration:** __{2}__\n"
        "**♪ Auxed By:** {3}"
    )
    PROFILE = (
        "**{0}\nUser Profile**\n\n"
        "**💬 Name:** {1}\n"
        "**💠 ID:** `{2}`\n"
        "**📝 User Type:** __{3}__\n"
        "**⚜️ Level:** __{4}__\n"
        "**🎶 Songs Played:** __{5}__\n"
        "**〥 Joined Since:** __{6}__\n\n"
        "**❆** {7}"
    )
    QUEUE = (
        "**Added to Queue (#{0})** \n\n"
        "**» Song Name:** __{1}__\n"
        "**» Duration:** __{2}__\n"
        "**» Queued By:** {3}"
    )
    SONG_CAPTION = (
        "**⊸ Title:** [{0}]({1})\n\n"
        "**⊸ Views:** {2}\n"
        "**⊸ Duration:** {3}\n"
        "**⊸ Requested By:** {4}\n\n"
    )
    SOURCE = (
        "**Support:**\n\n"
        "**Note:** \n__The Support is available on Telegram. You can find the link below.__\n"
        "__» This bot was created to make it easier for you to play music on Telegram Voice.__\n"
        "__» Anyone pretending to be the developer of this bot and selling the code, is a scammer.__\n\n"
        "__» If you like the projects created by my developers, help support us!.__\n"
        "__» If you want to use this music repo, please contact the bot developer.__\n\n"
    )
    STATS = (
        "**⤞ Server Stats:**\n"
        "    __Total Users:__ `{0} users`\n"
        "    __Total Chats:__ `{1} chats`\n"
        "    __Total Gbans:__ `{2} users`\n"
        "    __Blocked Users:__ `{3} users`\n"
        "    __Songs Played:__ `{4} songs`\n"
        "    __Active VC:__ `{5} vc`\n\n"
        "**⤞ System Stats:**\n"
        "    __Core:__ `{6} cores`\n"
        "    __CPU Usage:__ `{7}`\n"
        "    __Disk Usage:__ `{8}`\n"
        "    __RAM Usage:__ `{9}`\n"
        "    __Uptime:__ `{10}`\n\n"
    )
    SYSTEM = (
        "**⤞ System Info:**\n\n"
        "   __Core:__ `{0} cores`\n"
        "   __CPU Usage:__ `{1}`\n"
        "   __Disk Usage:__ `{2}`\n"
        "   __RAM Usage:__ `{3}`\n"
        "   __Uptime:__ `{4}`\n\n"
    )
    HELP_ADMIN = (
        "**Authorized Users Commands:**\n\n"
        "**» /auth ; /unauth**\n"
        "    Authorize or unauthorize user to use admins command such as /skip, /pause, etc.\n\n"
        "**» /authlist**\n"
        "    List all authorized users.__\n\n"
        "**» /authchat**\n"
        "    This enables all the users in the chat to use admins command such as /skip, /pause, etc.\n\n"
        "**» /mute ; /unmute**\n"
        "    Mute or unmute the ongoing track in the voice chat.\n\n"
        "**» /pause ; /resume**\n"
        "    Pause or resume the ongoing track in the voice chat.\n\n"
        "**» /stop ; /end**\n"
        "    Stop the ongoing track in the voice chat.\n\n"
        "**» /loop**\n"
        "    Loop the playing track in the voice chat. Use [/loop 0] to disable the loop.\n\n"
        "**» /skip**\n"
        "    Skip the playing track in the voice chat.\n\n"
        "**» /replay**\n"
        "    Replay from the beginning of the playing track in the voice chat.\n\n"
        "**» /seek**\n"
        "    Seek the playing track in the voice chat. Use [/seek 10] to seek forward and [/seek-10] to seek backwards.\n\n"
        "**» /clean**\n"
        "    Clear the queue when bot seems to be bugged.\n\n"
    )
    HELP_USER = (
        "**Normal Users Commands:**\n\n"
        "**» /play ; /vplay**\n"
        "    Play replied audio/video file or youtube video or searched query on voice chat.\n\n"
        "**» /fplay ; /fvplay**\n"
        "    Force play replied audio/video file or youtube video or searched query on voice chat.\n\n"
        "**» /favs ; /myfavs ; /favorites**\n"
        "    Show your favorite songs list.\n\n"
        "**» /delfavs**\n"
        "    Delete your favorite songs from your list.\n\n"
        "**» /current ; /playing**\n"
        "    Show the current playing song.\n\n"
        "**» /queue ; /que ; /q**\n"
        "    Show the queued songs list.\n\n"
        "**» /song**\n"
        "    Download the searched song from youtube.\n\n"
        "**» /lyrics**\n"
        "    Get the lyrics of the searched song. Give artist name after ' - ' for accurate results. [/lyrics Without Me - Eminem]\n\n"
        "**» /profile ; /me**\n"
        "    Show your profile and stats.\n\n"
    )
    HELP_SUDO = (
        "**Sudo Users Commands:**\n\n"
        "**» /active**\n"
        "    Check active voice chats of the bot.\n\n"
        "**» /autoend**\n"
        "    Enable or disable autoend inactive voice chats.\n\n"
        "**» /block ; /unblock**\n"
        "    Block or unblock user from using the bot.\n\n"
        "**» /blocklist**\n"
        "    List all blocked users.__\n\n"
        "**» /gban ; /ungban**\n"
        "    Globally ban or unban user from using the bot.\n\n"
        "**» /gbanlist**\n"
        "    List all globally banned users.\n\n"
        "**» /logs**\n"
        "    Get the logs of the bot.\n\n"
        "**» /restart**\n"
        "    Restart the bot globally.\n\n"
        "**» /sudolist**\n"
        "    List all sudo users.\n\n"
        "**» /stats**\n"
        "    Show full stats of the bot.\n\n"
    )
    HELP_OTHERS = (
        "**Other Commands:**\n\n"
        "**» /start**\n"
        "    Check if the bot is alive.\n\n"
        "**» /ping**\n"
        "    Check ping of the bot.\n\n"
        "**» /help**\n"
        "    Show this menu.\n\n"
        "**» /sysinfo**\n"
        "    Show system information of the bot.\n\n"
        "**» /leaderboard ; /topusers**\n"
        "Show the top 10 users with most number of songs played.\n\n"
    )
    HELP_OWNERS = (
        "**Owner Commands:**\n\n"
        "**» /eval ; /run**\n"
        "    Execute the python script.\n\n"
        "**» /exec ; /term ; /sh**\n"
        "    Execute the bash script.\n\n"
        "**» /getvar ; /gvar ; /var**\n"
        "    Get the value of the config variable.\n\n"
        "**» /addsudo**\n"
        "    Add sudo user of the bot who can use sudo commands.\n\n"
        "**» /rmsudo ; /delsudo**\n"
        "Remove sudo user of the bot.\n\n"
    )
    HELP_GC = (
        "Get the help menu in your PM. "
        "Click the button below!"
    )
    HELP_PM = (
        "**Help ⚙️**\n\n"
        "» All commands are categorized based on their usability and target users.\n"
        "» You can use these buttons below to navigate each category and get respective commands.\n"
        "» Feel free to contact us if you need any help regarding the bot.\n\n"
    )
    START_GC = (
        "Yeah, I'm alive! "
        "Wanna listen to some music?"
    )
    START_PM = (
        "**Hello** {0}**!**\n\n"
        "**Saya** {1} **, bot musik yang dapat memutar musik di Obrolan Suara.**\n"
        "**Tambahkan saya ke grup Anda dan putar musik dengan bebas!**\n\n"
        "» Jangan ragu untuk menambahkan saya, dan mencoba berbagai perintah!\n"
        "» Nikmati musiknya dan beri tahu kami jika Anda memiliki saran untuk perbaikan.\n\n"        
    )
    PERFORMER = "[ Spotify ]"
