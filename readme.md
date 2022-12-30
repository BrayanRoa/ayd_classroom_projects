<p align="center">
  <a href="https://ingsistemas.cloud.ufps.edu.co/" target="blank"><img src="https://ww2.ufps.edu.co/public/archivos/elementos_corporativos/logo-horizontal.jpg" width="400" alt="UFPS Logo" /></a>
</p>


# Run In Development

1. clone the repository

2. Execute
```
export FLASK_APP=entrypoint
export FLASK_DEBUG=1
flask shell
    from app.db import db
    db.create_all()
    exit the shell -> ctrl + d

flask run
```