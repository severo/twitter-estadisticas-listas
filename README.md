# twitter-estadisticas-listas

Un script para sacar estadísticas de las cuentas de una lista.

## Uso

Primero instalar el entorno necesario, ver [INSTALL.md](INSTALL.md).

Luego llamar el script con:

```bash
python get_list_statistics.py
```

El resultado se encuentra en el archivo especificado en `config.yml`, por ejemplo, si `config.yml` contiene:

```yaml
export:
  filepath: /tmp/
  filename_base: listas
```

el archivo creado el 25/05/2018 a las 12:29:35 será `/tmp/listas_20180525-122935.csv`.
