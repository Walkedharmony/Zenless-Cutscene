import os
import sqlite3

def extract_audio_from_db(input_filename, db_name="audio_files.db", output_folder="extracted_audio"):
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT filename FROM audio_files")
    all_files = cursor.fetchall()

    normalized_input_filename = input_filename.replace('.usm', '').lower() + '.wav'

    cursor.execute("SELECT filename, audio FROM audio_files WHERE filename = ?", (normalized_input_filename,))
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            filename, audio_data = row
            output_path = os.path.join(output_folder, filename)

            with open(output_path, 'wb') as f:
                f.write(audio_data)

    else:
        print(f"Tidak ditemukan file audio yang cocok dengan {input_filename}")

    conn.close()

