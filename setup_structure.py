import os

def create_project_structure(base_dir="."):
    folders = [
        "data",
        "data/datasets",
        "models",
        "services",
        "tests"
    ]
    files = [
        "main.py",
        "requirements.txt",
        "README.md",
        "data/loaders.py",
        "models/portfolio.py",
        "models/metrics.py",
        "models/risk_analysis.py",
        "services/email_service.py",
        "tests/test_portfolio.py"
    ]

    for folder in folders:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)
    for file in files:
        file_path = os.path.join(base_dir, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("")  # Crea un archivo vacío
    print(f"Estructura del proyecto creada en '{base_dir}'")

# Ejecutar la función
if __name__ == "__main__":
    create_project_structure()
