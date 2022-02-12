'''
Renam_eBot
Thanks to Spechide Unkle as always for the concept  ♥️
This file is a part of TE_GitHub rename repo 
Dont kang !!!
© TE_GitHub
'''
import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
@Client.on_message(filters.command("help"))
async def help_user(c,m):
    try:
       await m.reply_text(Translation.HELP_USER,quote=True)
    except Exception as e:
        log.info(str(e))
        
@Client.on_message(filters.command("start"))
async def start_msg(c,m):
    button = [[
               InlineKeyboardButton("𝗡𝗘𝗪 𝗬𝗢𝗥𝗞 ✈", url=f"https://t.me/us7a5")
             ]]
    markup = InlineKeyboardMarkup(button) 
    try:
       await m.reply_text(Translation.START_TEXT,quote=True,reply_markup=markup,disable_web_page_preview=True) 
    except Exception as e:
        log.info(str(e))       
@Client.on_message(filters.command("log") & filters.private & filters.user(Config.OWNER_ID))
async def log_msg(c,m):
  z =await m.reply_text("Processing..", True)
  if os.path.exists("Log.txt"):
     await m.reply_document("Log.txt", True)
     await z.delete()
  else:
    await z.edit_text("Log file not found")
