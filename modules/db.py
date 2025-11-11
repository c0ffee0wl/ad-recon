from neo4j import GraphDatabase

def db_connect(URI, AUTH):
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver
