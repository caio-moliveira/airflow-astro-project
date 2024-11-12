# Pokemon API Airflow Project
## Overview
This project demonstrates a refactoring of a small project that fetches a random Pokémon from the Pokémon API and stores it in a PostgreSQL database. The primary goal is to showcase how orchestration techniques can enhance simplicity and scalability using Apache Airflow and Astro CLI. By implementing orchestration, we ensure seamless, automated handling of data fetching, transformation, and loading processes.

## Table of Contents

- [Overview](#project-overview)
- [Project Structure](#technologies-and-libraries-used)
- [Technologies Used](#architecture)
- [Usage](#setup-instructions)
- [Airflow DAG](#data-flow)

---

## Project Overview
![Capturar](https://github.com/user-attachments/assets/1400c72b-1370-4b34-95d1-4dc2da5220fe)



# Explanation of Structure

- **dags**: Contains the main DAG script (`pokemon_dag.py`) that orchestrates the ETL process.
- **include/sql**: Contains SQL scripts for database table creation and any necessary database operations.
- **plugins**: Custom operators, hooks, or sensors that extend Airflow functionality.
- **Dockerfile**: Specifies the Docker environment setup, provided by Astro CLI.
- **requirements.txt**: Lists required Python packages for Airflow.

# Technologies Used

- **Apache Airflow**: Workflow orchestration and scheduling.
- **Astro CLI**: Simplifies Airflow project setup and management.
- **Pokémon API**: Provides random Pokémon data.
- **PostgreSQL**: Database to store Pokémon data.

# Setup

## Prerequisites

- Docker installed and running.
- Astro CLI installed.
- Access to a PostgreSQL instance.

## Steps
  

1. **Clone the repository**:
   ```bash
   mkdir airflow-astro-project
   cd airflow-astro-project
   git clone git@github.com:caio-moliveira/airflow-astro-project.git
   
   ```



2. **Configure .env**
  
  ```bash
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
POSTGRES_HOST=POSTGRES_HOST
POSTGRES_DB=POSTGRES_DB

  AIRFLOW__CORE__ALLOWED_DESERIALIZATION_CLASSES=include.schema.PokemonSchema
  ```

3. **Start Astro CLI**: 
  ```bash
  astro dev start
  ```


 ## Airflow DAG

 The DAG, (`pokemon_dag.py`), follows these steps:

1. **Fetch Pokémon**: 
   - Requests a random Pokémon from the Pokémon `API`.
2. **Transform Data**:
   - Parses and structures data for storage
3. **Load to PostgreSQL**:
   - Inserts the structured data into the `PostgreSQL` database.


## Conclusion

This project successfully demonstrates the use of **Astro CLI** for managing and deploying an **Airflow DAG** that interacts with an external API and stores data in **PostgreSQL**. This setup exemplifies how **orchestration** can be added to an existing project with minimal changes, using Astro CLI as a tool for rapid Airflow development.


