from pyrogram import Client, filters
import anonsurf_handler
import stock_info

def stock_run():   
    api_id = 26915099
    api_hash = "58296f4f25526a31f8c9c2175b73afee"
    bot_token = "578152924:AAF9QwKqxydHJ9kToFuNqPu8kp2-Rvd6u9s"


    # تعریف آرگومان های مورد نیاز
    bot = Client("mtest bot" ,
                api_id = api_id ,
                api_hash = api_hash , 
                bot_token = bot_token ,
    )


    user_data = {}

    # anonsurf_handler.start_anonsurf("90708060")

    # Define the command to view the desired share information
    @bot.on_message(filters.command('stock') & filters.private)
    def get_excel_info_command(client, message):
            message.reply_text("لطفا نام سهم مورد نظر را وارد کنید")
            user_data[message.chat.id] = {'state': 'waiting_for_stock_name'}

    # Receive share information and check the price and...
    @bot.on_message(not filters.command and filters.create(lambda message, _: message.chat.id in user_data and user_data[message.chat.id]['state'] == 'waiting_for_stock_name'))
    def handle_message1(client, message):
        chat_id = message.chat.id
        if chat_id in user_data and user_data[chat_id]['state'] == 'waiting_for_stock_name':
            customer_input = message.text
            
            user_data[chat_id]['state'] = 'processing'
        if chat_id in user_data and user_data[chat_id]['state'] == 'processing':
            try:
    
                message.reply_text(stock_info.get_stock_info(customer_input))
                


            except Exception as e:
                message.reply_text(f"خطایی رخ داد: {e}")
            user_data[chat_id]['state'] = 'complete'


    bot.run()

