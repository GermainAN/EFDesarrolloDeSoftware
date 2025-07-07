# EFDesarrolloDeSoftware

### Estrutura del proyecto

```bash
.
├── Dockerfile
├── github
│   └── workflows
│       └── ci.yml
├── README.md
└── tests
    ├── stubs
    │   └── fake-analyzer.sh
    └── test_analyzer.py
```

### clonar el repositorio

```bash
git clone https://github.com/GermainAN/EFDesarrolloDeSoftware.git
```
### primero creamos el entorno virtual

```bash
python3 -m venv final
```

### activamos el entorno virtual
```bash
source final/bin/activate
```

### instalamos los requerimientos
```bash
pip install -r requirements
```

### nos dirigimos a la carpeta tests

```bash
cd tests
```

### ejecucion de pytest

```
pytest
```
