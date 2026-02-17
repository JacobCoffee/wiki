# mssqlDataset

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# mssqlDataset 

    import pymssql

    class mssqlDatarow(object):
            def __init__(self,fields,values):
                    self.__fields={}
                    for f,v in zip(fields, values):
                            self.__fields[f.upper()]=v
                    self.__values=values
                    
            def getValue(self,fieldName):
                    return self.__fields.get(fieldName.upper())

    class mssqlDataset(object):
            def __init__(self,cnt):
                    self.__cnt=cnt
                    self.rows=None
                    self.fieldNames=None

            def getFieldNameOnSelectAs(self,sqlSelect):
                    sqlSelect=sqlSelect.strip().upper()
                    asFix=' as '.upper()
                    asIndex=sqlSelect.rfind(asFix)
                    if asIndex<=0: return sqlSelect
                    sqlSelect=sqlSelect[asIndex+len(asFix):]
                    return sqlSelect

            def query(self,sqlSelect,sqlFrom,sqlWhere=None
                            ,sqlOrder=None,sqlGroup=None,sqlPre=None):
                    s=sqlSelect.strip()
                    s=s.split(",")
                    self.fieldNames=map(self.getFieldNameOnSelectAs,s)
                    ssql="select %s%s "%(sqlPre+" " if sqlPre else ""
                                    ,sqlSelect if sqlSelect else "")
                    ssql+="\nfrom %s "%(sqlFrom if sqlFrom else "",)
                    ssql+="\n%s "%("where "+sqlWhere if sqlWhere else "",)
                    ssql+="\n%s "%("order by "+sqlOrder if sqlOrder else "",)
                    ssql+="\n%s"%("group by "+sqlGroup if sqlGroup else "",)
                    cur=self.__cnt.cursor()
                    cur.execute(ssql)
                    fetches=cur.fetchall()
                    cur.close()
                    self.rows=list()
                    for fetch in fetches:
                            self.rows.append(mssqlDatarow(self.fieldNames,fetch))
