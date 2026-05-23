import pandas as pd
from sqlalchemy import create_engine

# DB 연결
DATABASE_URL = "postgresql://user:pass@localhost:5432/app_db"

engine = create_engine(DATABASE_URL)

# CSV 읽기
df = pd.read_csv("places.csv")

print(df.columns)

# DB에 저장
#df.to_sql(
#    name="places",
#    con=engine,
#    if_exists="append",
#    index=False
#)

print("데이터 삽입 완료")