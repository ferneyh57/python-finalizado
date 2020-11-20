from pydal import DAL, Field    # importamos las librerias necesarias

class dataSource:
    db = ""                 # Conector Base de datos

     # constructor
    def __init__(self, host, user, passw, database, port, tipo_bd):

        if tipo_bd == "sqlite":
            self.db = DAL("sqlite://" + database + ".db")
        elif tipo_bd == "mysql":
            self.db = DAL("mysql://" + user + ":" + passw + "@" + host + "/" + database + "")
        elif tipo_bd == "postgres":
            self.db = DAL("postgres://" + user + ":"  + passw + "@" + host + "/" + database + "")
        elif tipo_bd == "sqlserver":
            self.db = DAL("mssql4://" + user+ ":" + passw+ "@" + host+ "/"+ database+ "")
        elif tipo_bd == "firebird":
            self.db = DAL("firebird://"+ user+ ":" + passw+ "@" + host+ "/"+ database+ "")
        elif tipo_bd == "oracle":
            self.db = DAL("oracle://"+ user+ ":" + passw+ "@" + host+ "/"+ database+ "")  
        elif tipo_bd == "db2":
            self.db = DAL("db2://"+ user+ ":" + passw+ "@"+ database+ "")
        """
        Ingres	ingres://usuario:contraseña@localhost/nombrebd
        Sybase	sybase://usuario:contraseña@localhost/nombrebd
        Informix	informix://usuario:contraseña@nombrebd
        Teradata	teradata://DSN=dsn;UID=usuario;PWD=contraseña;DATABASE=nombrebd
        Cubrid	cubrid://usuario:contraseña@localhost/nombrebd
        SAPDB	sapdb://usuario:contraseña@localhost/nombrebd
        IMAP	imap://user:contraseña@server:port
        MongoDB	mongodb://usuario:contraseña@localhost/nombrebd
        """

        # Vincular a una table preexistente.
        self.db.define_table(
            "users",
            # Indicarle a pyDAL cuál es la clave principal.
            Field("id", type="id"),
            Field("usuario"),
            Field("password"),
            Field("idrol", type="integer"),
            # Desactivar migraciones.
            migrate=False
        )

        

        """ Tipos de datos

        string          text        blob            boolean
        integer         double      decimal(n, m)   date
        time            datetime    password        upload
        reference <tabla>           list:string     list:integer
        list:reference <tabla>      json            bigint
        big-id          big-reference
        """


    def query (self, sql):
        try:
            self.db.executesql(sql)
            self.db.commit()
            return True
        except:
            return False
    
    def transaction (self, list):
        try:
            for l in list:
                self.db.executesql(l)
            self.db.commit()
            return True
        except:
            return False
            
    def getData(self, sql):
        q = self.db.executesql(sql)
        self.db.commit()
        return q
    