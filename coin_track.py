from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN = "7648014049:AAHRVap0OpFaP39tlG-LxjC1NOnTkoNbCWc"
URL = "https://brsapi.ir/Api/Market/Gold_Currency.php?key=FreeuaqGvMDvclRinL2Fy4Rzdb0jxcES"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/106.0.0.0",
    "Accept": "application/json, text/plain, */*"
}


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_text = """
    سلام دوست خوبم ☺️👋🏻
به ربات <b>CoinTrack</b> خوش اومدی! با این ربات میتونی قیمت لحظه ای ارز های مهم رو زیرنظر داشته باشی!


💰ارز هایی که پشتیبانی میکنیم:

💵 دلار آمریکا (USD)، یورو (EUR)، پوند (GBP)، فرانک سوئیس (CHF)

🧈 طلای 18 عیار، طلای 24 عیار، انس طلا، سکه یک گرمی، ربع سکه، نیم سکه، سکه امامی، سکه بهار آزادی

⚜️ بیت کوین (BTC)، اتریوم (ETH)، تتر (USDT)، ایکس آر پی (XRP)، بی ان بی (BNB)، سولانا (SOL)، دوج کوین (DOGE)، کاردانو (ADA)، ترون (TRX)
    
برای اطلاع از تمامی command ها، دکمه menu رو بزنید.
    """
    await update.message.reply_text(start_text, parse_mode='html')


async def fiat_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(URL, headers=headers)
    data = {}
    if response.status_code == 200:
        data = response.json()
    else:
        print(f'Error: {response.status_code}')

    last_update = f'{data["currency"][0]["date"]} - {data["currency"][0]["time"]}'
    usd = data["currency"][0]["price"]
    eur = data["currency"][1]["price"]
    gbp = data["currency"][3]["price"]
    chf = data["currency"][11]["price"]
    fiat_text = f"""
🇺🇸 دلار آمریکا: <b>{"{:,}".format(usd)}</b> تومان
🇪🇺 یورو: <b>{"{:,}".format(eur)}</b> تومان
🇬🇧 پوند: <b>{"{:,}".format(gbp)}</b> تومان 
🇨🇭 فرانک سوئیس: <b>{"{:,}".format(chf)}</b> تومان 

آخرین به روز رسانی:
⏳{last_update}
    """
    await update.message.reply_text(fiat_text, parse_mode="html")


async def gold_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(URL, headers=headers)
    data = {}
    if response.status_code == 200:
        data = response.json()
    else:
        print(f'Error: {response.status_code}')

    last_update = f'{data["gold"][3]["date"]} - {data["gold"][3]["time"]}'
    IR_GOLD_18K = data["gold"][0]["price"]
    IR_GOLD_24K = data["gold"][1]["price"]
    XAUUSD = data["gold"][3]["price"]
    IR_COIN_1G = data["gold"][4]["price"]
    IR_COIN_QUARTER = data["gold"][5]["price"]
    IR_COIN_HALF = data["gold"][6]["price"]
    IR_COIN_EMAMI = data["gold"][7]["price"]
    IR_COIN_BAHAR = data["gold"][8]["price"]
    gold_text = f"""
🟡 طلای 18 عیار: <b>{"{:,}".format(IR_GOLD_18K)}</b>  تومان
🟡 طلای 24 عیار: <b>{"{:,}".format(IR_GOLD_24K)}</b>  تومان
🟡 انس طلا: <b>{"{:,}".format(XAUUSD)}</b>  دلار
🟡 سکه یک گرمی: <b>{"{:,}".format(IR_COIN_1G)}</b> تومان
🟡 ربع سکه: <b>{"{:,}".format(IR_COIN_QUARTER)}</b> تومان
🟡 نیم سکه: <b>{"{:,}".format(IR_COIN_HALF)}</b> تومان
🟡 سکه امامی: <b>{"{:,}".format(IR_COIN_EMAMI)}</b> تومان
🟡 سکه بهار آزادی: <b>{"{:,}".format(IR_COIN_BAHAR)}</b> تومان

آخرین به روز رسانی:
⏳{last_update}
    """
    await update.message.reply_text(gold_text, parse_mode="html")


async def crypto_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = requests.get(URL, headers=headers)
    data = {}
    if response.status_code == 200:
        data = response.json()
    else:
        print(f'Error: {response.status_code}')

    last_update = f'{data["cryptocurrency"][0]["date"]} - {data["cryptocurrency"][0]["time"]}'
    btc = data["cryptocurrency"][0]["price"]
    eth = data["cryptocurrency"][1]["price"]
    usdt = data["cryptocurrency"][2]["price"]
    xrp = data["cryptocurrency"][3]["price"]
    bnb = data["cryptocurrency"][4]["price"]
    sol = data["cryptocurrency"][5]["price"]
    usdc = data["cryptocurrency"][6]["price"]
    doge = data["cryptocurrency"][7]["price"]
    ada = data["cryptocurrency"][8]["price"]
    trx = data["cryptocurrency"][9]["price"]
    crypto_text = f"""
🔷 Bitcoin (<b>BTC</b>): 💲<b>{btc}</b>
🔷 Ethereum (<b>ETH</b>): 💲<b>{eth}</b>
🔷 Tether (<b>USDT</b>): 💲<b>{usdt}</b>
🔷 XRP (<b>XRP</b>): 💲<b>{xrp}</b>
🔷 BNB (<b>BNB</b>): 💲<b>{bnb}</b>
🔷 Solana (<b>SOL</b>): 💲<b>{sol}</b>
🔷 USD Coin (<b>USDC</b>): 💲<b>{usdc}</b>
🔷 Dogecoin (<b>DOGE</b>): 💲<b>{doge}</b>
🔷 Cardano (<b>ADA</b>): 💲<b>{ada}</b>
🔷 TRON (<b>TRX</b>): 💲<b>{trx}</b>

آخرین به روز رسانی:
⏳{last_update}
"""
    await update.message.reply_text(crypto_text, parse_mode="html")


if __name__ == '__main__':
    print("Starting bot ...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('fiat', fiat_command))
    app.add_handler(CommandHandler('gold', gold_command))
    app.add_handler(CommandHandler('crypto', crypto_command))
    print("Polling...")
    app.run_polling(poll_interval=3)
