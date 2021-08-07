import wikipedia

from . import *


@ultroid_cmd(pattern="wiki ?(.*)")
async def wiki(e):
    srch = e.pattern_match.group(1)
    if not srch:
        return await eor(e, "`Axtarmaga bir shey ver`")
    msg = await eor(e, f"`Axtarish {srch} on wikipedia..`")
    try:
        mk = wikipedia.summary(srch)
        te = f"**Axtarish :** {srch}\n\n**Netice :** {mk}"
        await msg.edit(te)
    except Exception as e:
        await msg.edit(f"**XETA** : {str(e)}")
