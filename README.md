# twitter-estadisticas-listas

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/dc0deef981494a0097ab7395a28c8697)](https://app.codacy.com/app/severo/twitter-estadisticas-listas?utm_source=github.com&utm_medium=referral&utm_content=severo/twitter-estadisticas-listas&utm_campaign=badger)

Un script para sacar estadísticas de las cuentas de una lista.

## Uso

Primero instalar el entorno necesario, ver [INSTALL.md](INSTALL.md).

Luego llamar el script con:

```bash
python3 get_list_statistics.py
```

El resultado se encuentra en el archivo especificado en `config.yml`, por ejemplo, si `config.yml` contiene:

```yaml
export:
  filepath: /tmp/
  filename_base: listas
```

el archivo creado el 25/05/2018 a las 12:29:35 será `/tmp/listas_20180525-122935.csv`.

#modificacion del archivo
#pruba
#UASB

#prueba desde mi cuenta github

