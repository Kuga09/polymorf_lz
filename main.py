# Импорт используемых библиотек
import pandas as pd
# Импорт класса
from program import Data


# Функция main
def main():
    df = Data(pd.read_csv('var1.csv'))
    df.similar_count()
    df.divide()
    ~df
    


if __name__ == "__main__":
    main()