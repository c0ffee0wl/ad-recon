from modules import query

def adminCount_queries(driver):
    print("----")
    print("AdminCount= False Users Outbound Transitive Rights")
    print("----")
    query.get_adminCountFalseUsers_trans(driver)
