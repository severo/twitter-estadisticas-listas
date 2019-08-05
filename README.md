# twitter-estadisticas-listas

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/5c0e1f6c5ebf4c44834b81cb2cfc0a44)](https://www.codacy.com/app/severo/twitter-estadisticas-listas?utm_source=github.com&utm_medium=referral&utm_content=severo/twitter-estadisticas-listas&utm_campaign=Badge_Grade)

A script to get some statistics (followers, follows, tweets, last tweet) about accounts of a Twitter list.

## Use

First install the required Python packages:

- [PyYAML](https://pypi.org/project/PyYAML/)
- [python-twitter](https://pypi.org/project/python-twitter/)

Then copy `config.yml.example` to `config.yml` and modify the parameters:

- [create a Twitter app](https://developer.twitter.com/en/apps/create) with read-only privilege. See also the [python-twitter documentation](https://python-twitter.readthedocs.io/en/latest/getting_started.html).
- copy the keys and secret to the `twitter` section of `config.yml`:

  ```yaml
  twitter:
    consumer_key: 123
    consumer_secret: 123
    access_token_key: 123
    access_token_secret: 123
  ```

- provide the Twitter lists to analyze. For example, to analyze the lists https://twitter.com/payorivero/lists/monit-medios and https://twitter.com/payorivero/lists/instituciones-p%C3%BAblicas:
  ```yaml
  lists:
    - user: payorivero
      list: monit-medios
    - user: payorivero
      list: instituciones-públicas
  ```
- specify where the files will be written:

  ```yaml
  export:
    filepath: /tmp/
    filename_base: listas
  ```

Call the script with:

```bash
python3 get_list_statistics.py
```

With the default configuration, the result file created on 2018/05/25 at 12:29:35 will be located at `/tmp/listas_20180525-122935.csv`. It contains one row per user of a Twitter list:

```csv
usuario_lista,lista,usuario,nombre,seguidores,siguiendo,tweets,ultimo_tweet
"payorivero","monit-medios","OpinionIdeas","Opinion E Ideas","31","96","53","2019-08-02 21:34:01"
"payorivero","monit-medios","primeralineabo","Primera Línea","710","380","983","2019-08-02 22:06:07"
"payorivero","monit-medios","CriterioBolivia","Revista Criterio","22","278","100","2019-07-10 00:58:38"
"payorivero","monit-medios","esUltimobo","#esÚltimo","100","716","394","2019-06-27 03:56:53"
"payorivero","monit-medios","FMBOLVAR1","FM BOLÍVAR","90","19","71","2019-05-17 05:32:35"
"payorivero","monit-medios","BoliviaForbes","ForbesBoliviaOficial","463","191","799","2019-08-02 19:58:48"
"payorivero","monit-medios","revistaelmiope","El Miope","76","41","18","2019-03-30 14:56:16"
"payorivero","monit-medios","SoloFutbolBo","SoloFutbolRadio","70","185","781","2019-07-31 11:31:22"
...
```

Note that the columns are named in Spanish, as it was required for a job in Bolivia. Their meaning is:

- `usuario_lista`: username of the Twitter list owner
- `lista`: name of the Twitter list
- `usuario`: username listed in the Twitter list
- `nombre`: displayed name
- `seguidores`: number of followers
- `siguiendo`: number of follows
- `tweets`: number of tweets
- `ultimo_tweet`: date of the last tweet
