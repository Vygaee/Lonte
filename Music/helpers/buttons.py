from pyrogram.types import InlineKeyboardButton


class MakeButtons:
    def __init__(self):
        self.ikb = InlineKeyboardButton

    def close_markup(self):
        buttons = [[self.ikb("🗑", callback_data="close")]]
        return buttons

    def queue_markup(self, count: int, page: int):
        if count != 1:
            buttons = [
                [
                    self.ikb("⪨", callback_data=f"queue|prev|{page}"),
                    self.ikb("🗑", callback_data="close"),
                    self.ikb("⪩", callback_data=f"queue|next|{page}"),
                ]
            ]
        else:
            buttons = [
                [
                    self.ikb("🗑", callback_data="close"),
                ]
            ]

        return buttons

    def playfavs_markup(self, user_id: int):
        buttons = [
            [
                self.ikb("Audio", callback_data=f"favsplay|audio|{user_id}"),
                self.ikb("Video", callback_data=f"favsplay|video|{user_id}"),
            ],
            [
                self.ikb("🗑", callback_data=f"favsplay|close|{user_id}"),
            ]
        ]
        return buttons

    async def favorite_markup(
        self, collection: list, user_id: int, page: int, index: int, db, delete: bool
    ):
        btns = []
        txt = ""
        d = 0 if delete == True else 1
        if len(collection) != 1:
            nav_btns = [
                [
                    self.ikb("Play Favorites", callback_data=f"myfavs|play|{user_id}|0|0"),
                ],
                [
                    self.ikb("⪨", callback_data=f"myfavs|prev|{user_id}|{page}|{d}"),
                    self.ikb("🗑", callback_data=f"myfavs|close|{user_id}|{page}|{d}"),
                    self.ikb("⪩", callback_data=f"myfavs|next|{user_id}|{page}|{d}"),
                ]
            ]
        else:
            nav_btns = [
                [
                    self.ikb("Play Favorites", callback_data=f"myfavs|play|{user_id}|0|0"),
                ],
                [
                    self.ikb("🗑", callback_data=f"myfavs|close|{user_id}|{page}|{d}"),
                ],
            ]
        try:
            for track in collection[page]:
                index += 1
                favs = await db.get_favorite(user_id, str(track))
                txt += f"**{'0' if index < 10 else ''}{index}:** {favs['title']}\n"
                txt += f"    **Duration:** {favs['duration']}\n"
                txt += f"    **Since:** {favs['add_date']}\n\n"
                btns.append(self.ikb(text=f"{index}", callback_data=f"delfavs|{track}|{user_id}"))
        except:
            page = 0
            for track in collection[page]:
                index += 1
                favs = await db.get_favorite(user_id, track)
                txt += f"**{'0' if index < 10 else ''}{index}:** {favs['title']}\n"
                txt += f"    **Duration:** {favs['duration']}\n"
                txt += f"    **Since:** {favs['add_date']}\n\n"
                btns.append(self.ikb(text=f"{index}", callback_data=f"delfavs|{track}|{user_id}"))

        if delete:
            btns = [btns]
            btns.append([self.ikb(text="Hapus Semua!!", callback_data=f"delfavs|all|{user_id}")])
            buttons = btns + nav_btns
        else:
            buttons = nav_btns

        return buttons, txt

    def active_vc_markup(self, count: int, page: int):
        if count != 1:
            buttons = [
                [
                    self.ikb(text="⪨", callback_data=f"activevc|prev|{page}"),
                    self.ikb(text="🗑", callback_data="close"),
                    self.ikb(text="⪩", callback_data=f"activevc|next|{page}"),
                ]
            ]
        else:
            buttons = [[self.ikb(text="🗑", callback_data="close")]]
        return buttons

    def authusers_markup(self, count: int, page: int, rand_key: str):
        if count != 1:
            buttons = [
                [
                    self.ikb(text="⪨", callback_data=f"authus|prev|{page}|{rand_key}"),
                    self.ikb(text="🗑", callback_data=f"authus|close|{page}|{rand_key}"),
                    self.ikb(text="⪩", callback_data=f"authus|next|{page}|{rand_key}"),
                ]
            ]
        else:
            buttons = [
                [
                    self.ikb(text="🗑", callback_data=f"authus|close|{page}|{rand_key}")
                ]
            ]
        return buttons

    def player_markup(self, chat_id, video_id, username):
        if video_id == "telegram":
            buttons = [
                [
                    self.ikb("🎛️", callback_data=f"controls|{video_id}|{chat_id}"),
                    self.ikb("🗑", callback_data="close"),
                ]
            ]
        else:
            buttons = [
                [
                    self.ikb("About Song", url=f"https://t.me/{username}?start=song_{video_id}"),
                ],
                [
                    self.ikb("❤️", callback_data=f"add_favorite|{video_id}"),
                    self.ikb("🎛️", callback_data=f"controls|{video_id}|{chat_id}"),
                ],
                [
                    self.ikb("🗑", callback_data="close"),
                ],
            ]
        return buttons

    def controls_markup(self, video_id, chat_id):
        buttons = [
            [
                self.ikb(text="⟲", callback_data=f"ctrl|bseek|{chat_id}"),
                self.ikb(text="⦿", callback_data=f"ctrl|play|{chat_id}"),
                self.ikb(text="⟳", callback_data=f"ctrl|fseek|{chat_id}"),
            ],
            [
                self.ikb(text="⊡ End", callback_data=f"ctrl|end|{chat_id}"),
                self.ikb(text="↻ Replay", callback_data=f"ctrl|replay|{chat_id}"),
                self.ikb(text="∞ Loop", callback_data=f"ctrl|loop|{chat_id}"),
            ],
            [
                self.ikb(text="⊝ Mute", callback_data=f"ctrl|mute|{chat_id}"),
                self.ikb(text="⊜ Unmute", callback_data=f"ctrl|unmute|{chat_id}"),
                self.ikb(text="⊹ Skip", callback_data=f"ctrl|skip|{chat_id}"),
            ],
            [
                self.ikb(text="Back", callback_data=f"player|{video_id}|{chat_id}"),
                self.ikb(text="🗑", callback_data="close"),
            ],
        ]
        return buttons

    def song_markup(self, rand_key, url, key):
        buttons = [
            [
                self.ikb(text="Visit Youtube", url=url),
            ],
            [
                self.ikb(text="Audio", callback_data=f"song_dl|adl|{key}|{rand_key}"),
                self.ikb(text="Video", callback_data=f"song_dl|vdl|{key}|{rand_key}"),
            ],
            [
                self.ikb(text="⪨", callback_data=f"song_dl|prev|{key}|{rand_key}"),
                self.ikb(text="⪩", callback_data=f"song_dl|next|{key}|{rand_key}"),
            ],
            [
                self.ikb(text="🗑", callback_data=f"song_dl|close|{key}|{rand_key}"),
            ],
        ]

        return buttons

    def song_details_markup(self, url, ch_url):
        buttons = [
            [
                self.ikb(text="🎥", url=url),
                self.ikb(text="📺", url=ch_url),
            ],
            [
                self.ikb(text="🗑", callback_data="close"),
            ],
        ]
        return buttons

    def source_markup(self):
        buttons = [
            [
                self.ikb(text="Donasion", url="https://t.me/Usern4meDoestExist404"),
                self.ikb(text="Developer", url="https://t.me/Usern4meDoesNotExist404"),                        
            ],
            [
                self.ikb(text="Support", url="https://t.me/SpotifyStreamMusic"),
                self.ikb(text="Updates", url="https://t.me/SpotifyStream_Id"),
            ],
            [
                self.ikb(text="Back", callback_data="help|start"),
                self.ikb(text="🗑", callback_data="close"),
            ]
        ]
        return buttons

    def start_markup(self, username: str):
        buttons = [
            [
                self.ikb(text="Start", url=f"https://t.me/{username}?start=start"),
                self.ikb(text="🗑", callback_data="close"),
            ]
        ]
        return buttons

    def start_pm_markup(self, username: str):
        buttons = [
            [
                self.ikb(text="Help ⚙️", callback_data="help|back"),
                self.ikb(text="Support 🧰", callback_data="source"),
            ],
            [
                self.ikb(text="Add Me To Grup", url=f"https://t.me/{username}?startgroup=true"),
            ],
            [
                self.ikb(text="🗑", callback_data="close"),
            ]
        ]
        return buttons

    def help_gc_markup(self, username: str):
        buttons = [
            [
                self.ikb(text="Get Help ❓", url=f"https://t.me/{username}?start=help"),
                self.ikb(text="🗑", callback_data="close"),
            ]
        ]
        return buttons

    def help_pm_markup(self):
        buttons = [
            [
                self.ikb(text="Admins", callback_data="help|admin"),
                self.ikb(text="Users", callback_data="help|user"),
            ],
            [
                self.ikb(text="Sudos", callback_data="help|sudo"),
                self.ikb(text="Others", callback_data="help|others"),
            ],
            [
                self.ikb(text="Owner", callback_data="help|owner"),
            ],
            [
                self.ikb(text="Back", callback_data="help|start"),
                self.ikb(text="🗑", callback_data="close"),
            ],
        ]
        return buttons

    def help_back(self):
        buttons = [
            [
                self.ikb(text="Back", callback_data="help|back"),
                self.ikb(text="🗑", callback_data="close"),
            ]
        ]
        return buttons


Buttons = MakeButtons()
