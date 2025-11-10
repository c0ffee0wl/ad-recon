from modules import query

def hvt_queries(driver):
    print("----")
    print("Analyzing High Value Targets Inbound Rights")
    print("----")
    query.get_hvtRights(driver)
    query.get_hvtAdminFalse(driver)
