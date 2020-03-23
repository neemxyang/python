Sub 分类汇总()
    ' 如遇错误，自动继续下一个
    On Error Resume Next
     
    
    '字典法去重
    Dim d
    Dim i&, Myr&, Arr
    
    Set d = CreateObject("Scripting.Dictionary")
    Myr = Sheet2.[j65536].End(3).Row
    Arr = Sheet2.Range("j3:j" & Myr)
    For i = 1 To UBound(Arr)
        d(Arr(i, 1)) = d(Arr(i, 1)) + 1
    Next
    k = d.keys
    t = d.items

    Sheet3.Activate
    
    With Sheet3
        .Cells.ClearContents
        .[b2].Resize(d.Count, 1) = Application.Transpose(k)
        .[c2].Resize(d.Count, 1) = Application.Transpose(t)
        .[a1].Resize(1, 3) = Array("排名", "院线名称", "影院数量")
        .Range("a2:b" & [a65536].End(3).Row).Sort key1:=[b2], Order1:=xlDescending
        with .Columns

        
            
        End With
    End With
    
    
    
    
    Dim brr
    brr = Sheet3.UsedRange
    Dim b%
    For b = 1 To UBound(brr) - 1
        Sheet3.Cells(b + 1, 1) = b
    Next
    
    With Sheet3.Columns
        .AutoFit
        .VerticalAlignment = xlCenter
        .HorizontalAlignment = xlCenter
    End With
    
    With Sheet3.Rows
        .AutoFit
        .VerticalAlignment = xlCenter
        .HorizontalAlignment = xlCenter
    End With
    Set d = Nothing
End Sub
