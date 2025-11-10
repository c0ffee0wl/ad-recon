from modules import query

def owned_queries(driver):
    print("----")
    print("Analyzing Owned User Rights")
    print("----")
    query.get_ownedUserOutboundRights_firstDegree(driver)
