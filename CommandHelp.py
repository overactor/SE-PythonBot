CommandHelp = {
    "translate" : "Translates text using [Google Translate](https://translate.google.com). Syntax: `>>translate input_lang output_lang Text to translate.`. `input_lang` and `output_lang` are language codes such as `en`, `fr` and `auto`.",
    "random": "Returns a random floating-point number. Syntax: `>>random`",
    "randomint": "Returns a random integer. Syntax: `>>randomint [ [ min ] max ]`",
    "randomchoice": "Randomly chooses an item from a given list. Syntax: `>>randomchoice listitem1 listitem2 listitem3 ...`",
    "shuffle": "Shuffles a list of given items. Syntax: `>>shuffle listitem1 listitem2 listitem3 ...`",
    "listcommands": "Returns a list of all commands. Syntax: `>>listcommands`",
    "help": "Shows information about the chat bot, or about a specific command. Syntax: `>>help [ command ]`",
    "xkcdrandomnumber": "Returns a random number, based on an xkcd comic. Syntax: `>>xkcdrandomnumber`",
    "xkcd": "Shows the specified xkcd comic. Syntax: `>>xkcd comic_id`",

    "time": "A command specific for Shadow's Den. Changes how long the bot has to wait before replying. Syntax: `>>time time_in_seconds`",
    "viewspells": "A command specific for Shadow's Den. Shows the awarded spells of a specific user. Syntax: `>>viewspells user_id`",
    "link": "A command specific for Shadow's Den. Links a word to another word. Syntax: `>>link word1 word2`",
    "removelink": "A command specific for Shadow's Den. Removes a link between words. Syntax: `>>removelink word1 word2`",
    "reply": "A command specific for Shadow's Den. Replies to a specific message. Syntax: `>>reply message_id`",

    "stop": "Owner-only command. Stops the bot. Syntax: `>>stop`",
    "disable": "Owner-only command. Disables the bot. Syntax: `>>disable`",
    "enable": "Owner-only command. Enables the bot when it is disabled. Syntax: `>>enable`",
    "ban": "Owner-only command. Bans a user from using the bot. Syntax: `>>ban user_id`",
    "unban": "Owner-only command. Unbans a banned user. Syntax: `>>unban user_id`",
    "translationchain": "Owner-only command. Creates a chain of translations using [Google Translate](https://translate.google.com). Syntax: `>>translationchain steps_number input_lang output_lang Text to translate.`",
    "translationswitch": "Owner-only command. Creates a chain of translations using [Google Translate](https://translate.google.com), consisting of two languages. Syntax: `>>translationswitch steps_number lang1 lang2 Text to translate.`",
    "award": "Owner-only command, and specific for Shadow's Den. Awards a spell to a user. `-n` awards it immediately, `-q` adds it to the spell queue. Syntax: `>>award spell_id user_id -n|-q`",
    "emptyqueue": "Owner-only command, and specific for Shadow's Den. Empties the spell queue by awarding all spells in it. Syntax: `>>emptyqueue`"
}