#%%
import re
import pandas as pd

def remove_emoji(string):
    # 定义删除emoji的函数
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251"  # Enclosed characters
        "\U0000200D"              # Zero-width Joiner
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

SHOP_NAME = "biller"

df = pd.read_csv("./data.csv")

df.set_index(['order', 'brand'], inplace=True)
df[SHOP_NAME] = df[SHOP_NAME].map(eval)
df = df[SHOP_NAME].explode()
df

#%%
df = df.apply(remove_emoji)
df.reset_index()

# %%
