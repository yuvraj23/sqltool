from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request,'sqltoolapp/select_query.html')

import csv
import io  # python 3 only



def show_select_form(request):
    s=0
    return render(request,'sqltoolapp/select_query.html',{'s':s})


def show_update_form(request):
    s=1
    return render(request,'sqltoolapp/select_query.html',{'s':s})



def show_delete_form(request):
    s=2
    return render(request,'sqltoolapp/select_query.html',{'s':s})



def SELECT_QUERY_GENERATOR(request):
    s=0
    csv_content=[]
    f=1



    if request.method=='POST':
        try:
            file = request.FILES['file']
            #file_data = file.read().decode("utf-8")
            #print(file_data)
            for i in file:
                i=str(i)
                try:

                    num=i[2:len(i)-5]
                    num=int(num)
                    csv_content.append(num)


                except:
                    i=str(i)
                    string_value=i[2:len(i)-5].strip('""')
                    string_value=string_value.replace('""',"")
                    string_value=string_value.split(",")
                    csv_content.append(string_value)

        except:
            f=0

    v=1
    if request.method=='POST':
        try:
            selectval = request.POST.get('selectq')

        except:
            v=0
            selectval=None

    if request.method=='POST':
        try:
            tableval = request.POST.get('table_name')

        except:
            v=0
            tableval=None

    if request.method=='POST':
        try:

            whereval = request.POST.get('where_clause')

        except:
            v=0
            whereval=None
    if request.method=='POST':
        try:
            opval = request.POST.get('operator_q')

        except:
            v=0
            opval=None
    if request.method=='POST':
        try:
            val = request.POST.get('values_q')
            print("hhhhhhhhh",val,opval,'hhhhhhhhhhh')

        except:
            v=0
            val=None
    if request.method=='POST':
        try:
            print(selectval,tableval,whereval,opval,val)
        except:
            print("nhi milll kio bhi value")
    Query_List=[]
    if request.method=='POST' and v==1 and f==1:
        for i in csv_content:
            try:
                num=int(i[0])
                qry=f'SELECT {selectval} FROM {tableval} WHERE {whereval} {opval}  {num}'
                Query_List.append(qry)

            except:
                qry=f'SELECT {selectval} FROM {tableval} WHERE  {whereval} {opval}   \"{i[0]}\" '
                Query_List.append(qry)
        return  render(request,'sqltoolapp/select_query.html',{'s':s,'Query_List':Query_List})
    else:
        try:
            num=int(val)
            qry=f'SELECT {selectval} FROM {tableval} WHERE {whereval} {opval}  {num}'
            Query_List.append(qry)

        except:
            qry=f'SELECT {selectval} FROM {tableval} WHERE  {whereval} {opval}   \"{val}\" '
            Query_List.append(qry)



    return  render(request,'sqltoolapp/select_query.html',{'s':s,'Query_List':Query_List})

def UPDATE_QUERY_GENERATOR(request):
    s=1
    csv_content=[]
    f=1
    if request.method=='POST':
        try:
            file = request.FILES['file']
            #file_data = file.read().decode("utf-8")
            #print(file_data)
            for i in file:
                i=str(i)
                try:

                    num=i[2:len(i)-5]
                    num=int(num)
                    csv_content.append(num)


                except:
                    i=str(i)
                    string_value=i[2:len(i)-5].strip('""')
                    string_value=string_value.replace('""',"")
                    string_value=string_value.split(",")
                    csv_content.append(string_value)

        except:
            f=0

    v=1
    if request.method=='POST':
        try:
            updateval = request.POST.get('updateq')

        except:
            v=0
            print('You have not selected file')

    if request.method=='POST':
        try:
            setval = request.POST.get('setqry')

        except:
            v=0
            print('You have not selected file')

    if request.method=='POST':
        try:

            whereval = request.POST.get('where_clause')

        except:
            v=0
            print('You have not selected file')
    if request.method=='POST':
        try:
            opval = request.POST.get('operator_q')

        except:
            v=0
            print('You have not selected file')
    if request.method=='POST':
        try:
            val = request.POST.get('values_q')

        except:
            v=0
            print('You have not selected file')
    if request.method=='POST':
        try:
            print(updateval,setval,whereval,opval,val)
        except:
            print("nhi milll kio bhi value")
    Query_List=[]
    if request.method=='POST' and v==1 and f==1:
        for i in csv_content:
            try:
                num=int(i[0])
                qry=f'UPDATE {updateval} SET {setval} WHERE {whereval} {opval}  {num}'
                Query_List.append(qry)

            except:
                qry=f'UPDATE {updateval} SET {setval} WHERE  {whereval} {opval}   \"{i[0]}\" '
                Query_List.append(qry)
        return  render(request,'sqltoolapp/select_query.html',{'s':s,'Query_List':Query_List})
    elif v==1:
        try:
            num=int(val)
            qry=f'UPDATE {updateval} SET {setval} WHERE {whereval} {opval}  {num}'
            Query_List.append(qry)

        except:
            qry=f'UPDATE {updateval} SET {setval} WHERE  {whereval} {opval}   \"{val}\" '
            Query_List.append(qry)

    else:
        pass




    return  render(request,'sqltoolapp/select_query.html',{'s':s,'Query_List':Query_List})





def DELETE_QUERY_GENERATOR(request):
    s=2
    csv_content=[]
    f=1
    if request.method=='POST':
        try:
            file = request.FILES['file']
            #file_data = file.read().decode("utf-8")
            #print(file_data)
            for i in file:
                i=str(i)
                try:

                    num=i[2:len(i)-5]
                    num=int(num)
                    csv_content.append(num)


                except:
                    i=str(i)
                    string_value=i[2:len(i)-5].strip('""')
                    string_value=string_value.replace('""',"")
                    string_value=string_value.split(",")
                    csv_content.append(string_value)

        except:
            f=0

    v=1
    if request.method=='POST':
        try:
            delval = request.POST.get('delcol')

        except:
            v=0
            print('You have not selected file')

    if request.method=='POST':
        try:

            whereval = request.POST.get('where_clause')

        except:
            v=0
            print('You have not selected file')
    if request.method=='POST':
        try:
            opval = request.POST.get('operator_q')

        except:
            v=0
            print('You have not selected file')
    if request.method=='POST':
        try:
            val = request.POST.get('values_q')

        except:
            v=0
            print('You have not selected file')

    Query_List=[]
    if request.method=='POST' and v==1 and f==1:
        for i in csv_content:
            try:
                num=int(i[0])
                qry=f'DELETE  FROM {delval}  WHERE {whereval} {opval}  {num}'
                Query_List.append(qry)

            except:
                qry=f'DELETE  FROM {delval} WHERE  {whereval} {opval}   \"{i[0]}\" '
                Query_List.append(qry)
        return  render(request,'sqltoolapp/select_query.html',{'s':s,'Query_List':Query_List})
    elif v==1:
        if request.method=='POST' and v==1:
            try:
                num=int(val)
                qry=f'DELETE   FROM {delval} WHERE {whereval} {opval}  {num}'
                Query_List.append(qry)

            except:
                qry=f'DELETE  FROM {delval} WHERE  {whereval} {opval}   \"{val}\" '
                Query_List.append(qry)

    else:
        pass

    return  render(request,'sqltoolapp/select_query.html',{'s':s,'Query_List':Query_List})
