import psycopg2

POSTGRES_URL="postgres://default:x0iJr8jFOVcE@ep-late-poetry-27723165-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb"
POSTGRES_PRISMA_URL="postgres://default:x0iJr8jFOVcE@ep-late-poetry-27723165-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb?pgbouncer=true&connect_timeout=15"
POSTGRES_URL_NON_POOLING="postgres://default:x0iJr8jFOVcE@ep-late-poetry-27723165.us-east-1.postgres.vercel-storage.com:5432/verceldb"
POSTGRES_USER="default"
POSTGRES_HOST="ep-late-poetry-27723165-pooler.us-east-1.postgres.vercel-storage.com"
POSTGRES_PASSWORD="x0iJr8jFOVcE"
POSTGRES_DATABASE="verceldb"

connect = psycopg2.connect(host=POSTGRES_HOST, database=POSTGRES_DATABASE, 
                           user=POSTGRES_USER, password=POSTGRES_PASSWORD)

cursor = connect.cursor()

