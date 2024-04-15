### Primegen

> Give a lower and upper bound and choose algorithm type and get back primes within that range.

### Dependencies

#### language

-   **python 3.11**

#### cli

-   **unittest (inbuilt python module for unittesting)**
-   **argparse (inbuilt python module for parsing cli arguments)**

#### server

-   **fastapi**
-   **sqlite (database)**

### How to install and run

```bash
git clone https://github.com/glowfi/primegen
cd primegen
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

> Run cli

```bash
cd cli
./cli.py --help
```

> Run server

```bash
cd server
./run.sh
```
