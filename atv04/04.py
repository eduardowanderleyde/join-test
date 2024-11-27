import psycopg2

# Function to connect to the database
def connect_to_db():
    return psycopg2.connect(
        dbname="join_test",  # Database name
        user="postgres",     # Database user
        password="join",     # Replace with your password
        host="localhost",    # Host where the database is running
        port="5432"          # Default PostgreSQL port
    )

# Query A: Employees and their roles ordered by admission date
def consulta_a(conn):
    query_a = """
        SELECT p.nome AS funcionario, c.nome_cargo AS cargo
        FROM pessoas p
        JOIN cargos c ON p.id_cargo = c.id
        ORDER BY p.admissao ASC;
    """
    with conn.cursor() as cur:
        cur.execute(query_a)
        return cur.fetchall()

# Query B: Oldest employee in the company
def consulta_b(conn):
    query_b = """
        SELECT p.nome AS funcionario, c.nome_cargo AS cargo
        FROM pessoas p
        JOIN cargos c ON p.id_cargo = c.id
        ORDER BY p.admissao ASC
        LIMIT 1;
    """
    with conn.cursor() as cur:
        cur.execute(query_b)
        return cur.fetchall()

# Query C: Number of employees per role
def consulta_c(conn):
    query_c = """
        SELECT c.nome_cargo AS cargo, COUNT(p.id) AS quantidade_funcionarios
        FROM cargos c
        LEFT JOIN pessoas p ON c.id = p.id_cargo
        GROUP BY c.nome_cargo;
    """
    with conn.cursor() as cur:
        cur.execute(query_c)
        return cur.fetchall()

def main():
    try:
        # Connect to the database
        conn = connect_to_db()
        print("Connected to the database.")

        # Execute Query A
        print("\nQuery A: Employees ordered by admission date")
        result_a = consulta_a(conn)
        for row in result_a:
            print(row)

        # Execute Query B
        print("\nQuery B: Oldest employee in the company")
        result_b = consulta_b(conn)
        for row in result_b:
            print(row)

        # Execute Query C
        print("\nQuery C: Number of employees per role")
        result_c = consulta_c(conn)
        for row in result_c:
            print(row)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
