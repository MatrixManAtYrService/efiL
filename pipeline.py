import conducto as co
import os
import zipfile
from pathlib import Path

# much of this code was copied from https://www.kaggle.com/elvenmonk/pycosat-exploration
# thanks elvenmonk!

competition = 'conways-reverse-game-of-life-2020'

def csv_to_numpy_list(df):
    return df[[ f'stop_{n}' for n in range(25**2) ]].values.reshape(-1,25,25)

def life_step(X):
    C = convolve2d(X, window, mode='same', boundary='wrap')
    return (C == 3) | (X & (C == 4))

def read_all():
    import pandas as pd
    #sample_submission_df = pd.read_csv('sample_submission.csv', index_col='id')
    test_df = pd.read_csv('test.csv', index_col='id')
    #deltas = test_df['delta'].values
    return csv_to_numpy_list(test_df)

def life_step(board):
    from scipy.signal import convolve2d
    # https://nicholasrui.com/2017/12/18/convolutions-and-the-game-of-life/

    # a matrix of neighbor-counts
    C = convolve2d(board, np.ones((3,3)), mode='same', boundary='wrap')

    return (C == 3) | (boards & (C == 4))

def pickone(n):
    board = read_all()[0]



def getdata():

    if (Path('.') / 'train.csv').exists():
        print("data present")
        return
    else:
        print(f"fetching data for {competition}")


    # place api keys where kaggle wants them
    kdir = Path.home() / '.kaggle'
    kdir.mkdir(exist_ok=True)
    kjson = os.environ["KAGGLE_JSON"]
    kfile = kdir / 'kaggle.json'
    with open(kfile, 'w') as f:
        f.write(kjson)

    import kaggle
    kaggle.api.competition_download_files(competition)
    with zipfile.ZipFile(competition + '.zip', 'r') as z:
        z.extractall('.')

    print('ok')


img = co.Image(copy_dir=".", reqs_py=['kaggle', 'conducto', 'pandas', 'numpy', 'scipy'])

def main() -> co.Serial:
    with co.Serial(image=img) as node:
        node["get data"] = co.Exec(getdata)
    return node


if __name__ == "__main__":
    co.main(default=main)
