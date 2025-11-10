from modules import query

def transitive_queries(driver):
    print("----")
    print("Transitive Query will take a long time...probably like 5hrs")
    print("----")
    query.get_startingPoints(driver) # Check
    query.get_computerOutboundRights_trans(driver) # check
    query.get_userOutboundRights_trans(driver) # check 
    query.get_disabledUserOutboundRights_trans(driver) #check
    query.get_userinboundRights_trans(driver) # unique
