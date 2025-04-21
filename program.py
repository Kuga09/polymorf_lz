# Импорт используемых библиотек
import pandas as pd


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
    def divide(self):
        df_fiz = self.data[self.data["Участники гражданского оборота"] == "физ. лицо"]
        df_yur = self.data[self.data["Участники гражданского оборота"] == "юр. лицо"]

        df_fiz.to_csv("fiz_lica.csv", index=False)
        df_yur.to_csv("yur_lica.csv", index=False)






