# Импорт используемых библиотек
import pandas as pd


# Получение данных из csv
df = pd.read_csv('var1.csv')

# Создание класса
class Data:
    def __init__(self, data : pd.DataFrame):
        self.data = data

    # Функция, считающая количество дубликатов в датафрейме и удаляющая их
    def similar_count(self):
        count = self.data.duplicated().sum()
        print(f'Количество повторяющихся строк в наборе данных: {count}')
    
    # Функция, реализующая унарный оператор, удаляющий дубликаты в датафрейме
    def __invert__(self):
        df_unique = self.data.drop_duplicates()
        return df_unique.to_csv('var1_unique.csv')
    
    # Функция, которая разделяет датафрей на два датафейма по признку "Участники гражданского оборота"
    def divide():
        # Фильтруем DataFrame для физ. лиц
        df_fiz = df[df['Участники гражданского оборота'] == 'физ.лицо']
        print(df_fiz)

        # Фильтруем DataFrame для юр. лиц
        df_yur = df[df['Участники гражданского оборота'] == 'юр.лицо']  







