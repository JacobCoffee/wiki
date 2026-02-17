# RSMD.py

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Apache Derby RSMD.py 

back to [ApacheDerby](ApacheDerby) Example page.

:::: 
::: 
``` 
   1 #--------------------------------------------------------------------------
   2 # RSMD() - Routine used to gather the "interesting" ResultSet MetaData
   3 #--------------------------------------------------------------------------
   4 def RSMD( rs, NumTypes = None ) :
   5   from java.sql import Types as types
   6   #------------------------------------------------------------------------
   7   # Check for first invocation, so we can initialize NumType
   8   #------------------------------------------------------------------------
   9   if NumTypes == None :
  10     NumTypes = [ 
  11       types.BIGINT  ,
  12       types.DECIMAL ,
  13       types.DOUBLE  ,
  14       types.FLOAT   ,
  15       types.INTEGER ,
  16       types.NUMERIC ,
  17       types.REAL    ,
  18       types.SMALLINT,
  19       types.TINYINT  
  20     ]                
  21 
  22   #------------------------------------------------------------------------
  23   # Obtain MetaData for specified ResultSet
  24   #------------------------------------------------------------------------
  25   result = []
  26   rsmd   = rs.getMetaData()
  27   for col in range( 1, rsmd.getColumnCount() + 1 ) :
  28     Type = rsmd.getColumnType( col )
  29     if Type in NumTypes :                   # Only numeric values have...
  30       precision = rsmd.getPrecision( col )  # precision, and
  31       scale     = rsmd.getScale( col )      # scale
  32     else :                                  #
  33       precision = scale = None              #
  34     row =  ( rsmd.getColumnLabel( col ),
  35              rsmd.getColumnDisplaySize( col ),
  36              Type,
  37              precision,
  38              scale,
  39              rsmd.getColumnTypeName( col )
  40            )
  41     result.append( row )
  42   return tuple(result)
  43 
  44 #--------------------------------------------------------------------------
  45 # printRSMD() - Routine used to display the ResultSet MetaData of interest
  46 #--------------------------------------------------------------------------
  47 def printRSMD( rsmd, TableName ) :
  48   truncated = False
  49   print '\n Fields contained in:', TableName
  50   print '\n| Size  |  Label                 |Type |Type Name'
  51   print '+-------+------------------------+-----+--------------------'
  52   for Label, Size, Type, precision, scale, TypeName in rsmd :
  53     if len( Label ) > 24 :
  54       Label = Label[:23] + '*'
  55       truncated = True
  56     print '|%7d|%-24s|%5d|%-20s' % ( Size, Label, Type, TypeName )
  57   print
  58   if truncated : print ' * The specified field was truncated.'
```
:::
::::

back to [ApacheDerby](ApacheDerby) Example page.
