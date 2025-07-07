import subprocess
import os
from pathlib import Path


def test_fake_analyzer_exitoso(monkeypatch, tmp_path):
    # se prepara el stub
    directorio_stub = tmp_path / "temporal"
    directorio_stub.mkdir() # con esto creamos una carpeta temporal
    ruta_stub = directorio_stub / "external-analyzer"
    stub_original = Path(__file__).parent / "stubs" / "fake-analyzer.sh"
    ruta_stub.write_text(stub_original.read_text())
    ruta_stub.chmod(0o755) # esto hace que el stub sea ejecutable
    # aqui modficiamos la variable del entorno PATH
    path_anterior = os.environ.get("PATH", "")
    monkeypatch.setenv("PATH", f"{directorio_stub}:{path_anterior}")
    # aqui ejeuctamos el stub
    resultado = subprocess.run(["external-analyzer", "--success"], capture_output=True, text=True)
    assert resultado.returncode == 0


def test_fake_analyzer_falla(monkeypatch, tmp_path):
    directorio_stub = tmp_path / "temporal"
    directorio_stub.mkdir()
    ruta_stub = directorio_stub / "external-analyzer"
    stub_original = Path(__file__).parent / "stubs" / "fake-analyzer.sh"
    ruta_stub.write_text(stub_original.read_text())
    ruta_stub.chmod(0o755)
    path_anterior = os.environ.get("PATH", "")
    monkeypatch.setenv("PATH", f"{directorio_stub}:{path_anterior}")
    resultado = subprocess.run(["external-analyzer", "--fail"], capture_output=True, text=True)
    assert resultado.returncode == 1


def test_analizador_por_defecto(monkeypatch, tmp_path):
    directorio_stub = tmp_path / "temporal"
    directorio_stub.mkdir()
    ruta_stub = directorio_stub / "external-analyzer"
    stub_original = Path(__file__).parent / "stubs" / "fake-analyzer.sh"
    ruta_stub.write_text(stub_original.read_text())
    ruta_stub.chmod(0o755)
    path_anterior = os.environ.get("PATH", "")
    monkeypatch.setenv("PATH", f"{directorio_stub}:{path_anterior}")
    resultado = subprocess.run(["external-analyzer"], capture_output=True, text=True)
    assert resultado.returncode == 0