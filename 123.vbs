Sub 分类汇总()


    '  如遇错误，自动继续下一个
    On Error Resume Next
    '  作用是对某一个表的某一列进行去重统计
    '  字典法去重
    Dim d
    Dim i&, Myr&, Arr
    
    Set d = CreateObject("Scripting.Dictionary")
    With Sheet2
        Myr = .[j65536].End(3).Row
        Arr = .Range("j3:j" & Myr)
    End With
    For i = 1 To UBound(Arr)
        d(Arr(i, 1)) = d(Arr(i, 1)) + 1
    Next
    k = d.keys
    t = d.items

    
    
    With Sheet3
        .Activate
        .Cells.ClearContents
        .[b2].Resize(d.Count, 1) = Application.Transpose(k)
        .[c2].Resize(d.Count, 1) = Application.Transpose(t)
        .[a1].Resize(1, 3) = Array("排名", "院线名称", "影院数量")
        .Range("a2:c" & [a65536].End(3).Row).Sort key1:=[c2], Order1:=xlDescending
        With .Columns
            .AutoFit
            .VerticalAlignment = xlCenter
            .HorizontalAlignment = xlCenter
        End With
        With .Rows
            .AutoFit
            .VerticalAlignment = xlCenter
            .HorizontalAlignment = xlCenter
        End With
        Dim brr
        brr = .UsedRange
        Dim b%
        For b = 1 To UBound(brr) - 1
            .Cells(b + 1, 1) = b
        Next
    End With
    
      
    
    Set d = Nothing
End Sub

