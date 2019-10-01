import shelve
new=shelve.open('acclist')
new['list']=[]
new.close()
print('now run bank_management_system')
