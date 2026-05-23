import pandas as pd
import numpy as np
import psycopg2

# CSV 읽기
df = pd.read_csv("places_all_최종_with_vector_index.csv")

# NPY 읽기
embeddings = np.load("full_img_embeddings.npy")

print("CSV 행 개수:", len(df))
print("Embedding 개수:", len(embeddings))

# PostgreSQL 연결
conn = psycopg2.connect(
    host="localhost",
    database="app_db",
    user="user",
    password="pass",
    port=5432
)

cur = conn.cursor()

# metadata insert
for idx, row in df.iterrows():

    cur.execute(
        """
        INSERT INTO image_metadata (
            image_id,
            place_name,
            region,
            season,
            time,
            weather,
            scene,
            primary_mood,
            secondary_mood,
            caption,
            content_id,
            vector_index
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            str(row.get("image_id", "")),
            str(row.get("place_name", "")),
            str(row.get("region", "")),
            str(row.get("season", "")),
            str(row.get("time", "")),
            str(row.get("weather", "")),
            str(row.get("scene", "")),
            str(row.get("primary_mood", "")),
            str(row.get("secondary_mood", "")),
            str(row.get("caption", "")),
            int(float(row.get("content_id", 0))),
            int(row.get("vector_index", idx))
        )
    )

# embedding insert
for idx, embedding in enumerate(embeddings):

    embedding_list = embedding.tolist()

    cur.execute(
        """
        INSERT INTO image_embeddings (id, embedding)
        VALUES (%s, %s)
        """,
        (idx, embedding_list)
    )

conn.commit()

cur.close()
conn.close()

print("데이터 insert 완료!")