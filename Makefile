run-db:
	docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=password -e POSTGRES_DB=test_database -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres

update-db:
	alembic upgrade head

serve:
	uvicorn src.main:app --reload

add-revision:
	alembic revision --autogenerate -m $(message)

downgrade-db:
	alembic downgrade ${rev_count}
