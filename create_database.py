import pandas as pd
import sqlite3
import os
import glob

# 1. Путь к папке с данными и имя базы
data_path = "./data/nhl_stat"
db_name = "nhl_stat.db"

def build_database():
    # Создаем подключение к базе данных
    conn = sqlite3.connect(db_name)
    print(f"База данных создана/открыта: {db_name}")

    # Ищем все CSV файлы в указанной папке и подпапках
    csv_files = glob.glob(os.path.join(data_path, "**", "*.csv"), recursive=True)
    
    if not csv_files:
        print(f"CSV файлы не найдены в '{data_path}'! Проверьте путь.")
        return

    for file_path in csv_files:
        # Формируем чистое имя таблицы: без .csv, пробелы и тире -> '_'
        file_name = os.path.basename(file_path)
        table_name = file_name.replace(".csv", "").replace(" ", "_").replace("-", "_").lower()
        
        print(f"Импорт файла {file_name} в таблицу '{table_name}'...")
        
        try:
            # Попытка №1: Читаем с кодировкой Windows-1252 (актуально для имен игроков NHL)
            # Если файл окажется в UTF-8, pandas зачастую тоже его прочитает, но мы добавим обработку исключения на всякий случай.
            try:
                df = pd.read_csv(file_path, on_bad_lines='skip', encoding='Windows-1252')
            except UnicodeDecodeError:
                # Попытка №2: Если Windows-1252 не подошла, пробуем UTF-8
                df = pd.read_csv(file_path, on_bad_lines='skip', encoding='utf-8')
            
            # Записываем данные в SQL: if_exists='replace' перезапишет таблицу, если она уже была
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"Успешно: Таблица '{table_name}' готова!")
            
        except Exception as e:
            print(f"Ошибка при импорте {file_name}: {e}")

    conn.close()
    print("\nСборка базы данных завершена! Файл: nhl_stat.db")

if __name__ == "__main__":
    build_database()