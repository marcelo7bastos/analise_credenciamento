from db_config import username, password
import jaydebeapi

def get_db_connection():
    # Configuração do driver JDBC e URL de conexão
    jdbc_driver_name = "org.teiid.jdbc.TeiidDriver"
    jdbc_driver_path = "/home/mcb/cgcop/congif_dbeaver/arquivo_novos_user/jboss-dv-6.3.0-teiid-jdbc.jar"
    url = "jdbc:teiid:PNCP@mms://daas.serpro.gov.br:31000"

    # Conectar ao banco de dados
    conn = jaydebeapi.connect(jdbc_driver_name, url, [username, password], jdbc_driver_path)
    return conn
