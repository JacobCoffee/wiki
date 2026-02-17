# PoiExample

```{admonition} Legacy Wiki Page
:class: note

This page was migrated from the old MoinMoin-based wiki. Information may be outdated or no longer applicable. For current documentation, see [python.org](https://www.python.org).
```

# Apache Poi Examples 

back to [OtherExamples](OtherExamples)

------------------------------------------------------------------------

Below are a few Poi examples. These examples requires Apache Poi installed and on the classpath.

### Create Spreadsheet 

This is from the Jython mailing list and was posted September 2007

This is based on Java code at [http://officewriter.softartisans.com/OfficeWriter-306.aspx](http://officewriter.softartisans.com/OfficeWriter-306.aspx) and converted to Jython by Alfonso Reyes

:::: 
::: 
``` 
   1 #jython poi example. from Jython mailing list
   2 
   3 from java.io import FileOutputStream
   4 from java.util import Date
   5 from java.lang import System, Math
   6 
   7 from org.apache.poi.hssf.usermodel import *
   8 from org.apache.poi.hssf.util import HSSFColor
   9 
  10 startTime = System.currentTimeMillis()
  11 
  12 wb = HSSFWorkbook()
  13 fileOut = FileOutputStream("POIOut2.xls")
  14 
  15 
  16 # Create 3 sheets
  17 sheet1 = wb.createSheet("Sheet1")
  18 sheet2 = wb.createSheet("Sheet2")
  19 sheet3 = wb.createSheet("Sheet3")
  20 sheet3 = wb.createSheet("Sheet4")
  21 
  22 # Create a header style
  23 styleHeader = wb.createCellStyle()
  24 fontHeader = wb.createFont()
  25 fontHeader.setBoldweight(2)
  26 fontHeader.setFontHeightInPoints(14)
  27 fontHeader.setFontName("Arial")
  28 styleHeader.setFont(fontHeader)
  29 
  30 # Create a style used for the first column
  31 style0 = wb.createCellStyle()
  32 font0 = wb.createFont()
  33 font0.setColor(HSSFColor.RED.index)
  34 style0.setFont(font0)
  35 
  36 
  37 # Create the style used for dates.
  38 styleDates = wb.createCellStyle()
  39 styleDates.setDataFormat(HSSFDataFormat.getBuiltinFormat("m/d/yy h:mm"))
  40 
  41 
  42 # create the headers
  43 rowHeader = sheet1.createRow(1)
  44 # String value
  45 cell0 = rowHeader.createCell(0)
  46 cell0.setCellStyle(styleHeader)
  47 cell0.setCellValue("Name")
  48 
  49 
  50 # numbers
  51 for i in range(0, 8, 1):
  52     cell = rowHeader.createCell((i + 1))
  53     cell.setCellStyle(styleHeader)
  54     cell.setCellValue("Data " + str( (i + 1)) )
  55 
  56 
  57 # Date
  58 cell10 = rowHeader.createCell(9)
  59 cell10.setCellValue("Date")
  60 cell10.setCellStyle(styleHeader)
  61 
  62 for i in range(0, 100, 1):
  63     # create a new row
  64     row = sheet1.createRow(i + 2)
  65     for j in range(0, 10, 1):
  66         # create each cell
  67         cell = row.createCell(j)
  68         # Fill the first column with strings
  69         if j == 0:
  70             cell.setCellValue("Product " + str(i))
  71             cell.setCellStyle(style0)
  72 
  73         # Fill the next 8 columns with numbers.
  74         elif j < 9:
  75             cell.setCellValue( (Math.random() * 100))
  76 
  77             # Fill the last column with dates.
  78         else:
  79             cell.setCellValue(Date())
  80             cell.setCellStyle(styleDates)
  81 
  82 # Summary row
  83 rowSummary = sheet1.createRow(102)
  84 sumStyle = wb.createCellStyle()
  85 sumFont = wb.createFont()
  86 sumFont.setBoldweight( 5)
  87 sumFont.setFontHeightInPoints(12)
  88 sumStyle.setFont(sumFont)
  89 sumStyle.setFillPattern(HSSFCellStyle.FINE_DOTS)
  90 sumStyle.setFillForegroundColor(HSSFColor.GREEN.index)
  91 
  92 
  93 cellSum0 = rowSummary.createCell( 0)
  94 cellSum0.setCellValue("TOTALS:")
  95 cellSum0.setCellStyle(sumStyle)
  96 
  97 
  98 # numbers
  99 # B
 100 cellB = rowSummary.createCell( 1)
 101 cellB.setCellStyle(sumStyle)
 102 cellB.setCellFormula("SUM(B3:B102)")
 103 
 104 wb.write(fileOut)
 105 fileOut.close()
 106 
 107 stopTime = System.currentTimeMillis()
 108 print 'POI generation took %d ms' %(stopTime - startTime)
```
:::
::::

### Read an Excel file 

Posted to the Jython-users mailing list by Alfonso Reyes on October 14, 2007 This Jython code will open and read an existant Excel file you can download the file at [http://www.nabble.com/file/p13199712/Book1.xls](http://www.nabble.com/file/p13199712/Book1.xls)

To do: - create the excel file if it doesn\'t exist - a nicer printing method - a method to print values or formulas in the cells

:::: 
::: 
``` 
   1 """    read.py
   2 Read an existant Excel file (Book1.xls) and show it on the screen
   3 """   
   4 from org.apache.poi.hssf.usermodel import *
   5 from java.io import FileInputStream
   6 
   7 file = "H:Book1.xls"
   8 print file
   9 fis = FileInputStream(file)
  10 wb = HSSFWorkbook(fis)
  11 sheet = wb.getSheetAt(0)
  12 
  13 # get No. of rows
  14 rows = sheet.getPhysicalNumberOfRows()
  15 print wb, sheet, rows
  16 
  17 cols = 0 # No. of columns
  18 tmp = 0
  19 
  20 # This trick ensures that we get the data properly even if it
  21 # doesn't start from first few rows
  22 for i in range(0, 10,1):
  23     row = sheet.getRow(i)
  24     if(row != None):
  25         tmp = sheet.getRow(i).getPhysicalNumberOfCells()
  26         if tmp > cols:
  27             cols = tmp
  28 print cols
  29 
  30 for r in range(0, rows, 1):
  31     row = sheet.getRow(r)
  32     print r
  33     if(row != None):
  34         for c in range(0, cols, 1):
  35             cell = row.getCell(c)
  36             if cell != None:
  37                 print cell
  38 
  39 #wb.close()
  40 fis.close()
```
:::
::::

back to [OtherExamples](OtherExamples)
