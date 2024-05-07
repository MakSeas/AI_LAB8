import csv
import random

def MixArray(rowArray):
        length=len(rowArray)
        usedRows=[]

        i=0

        for row in rowArray:

            if len(usedRows)==len(rowArray)-1:
                break

            if not (i in usedRows):
                while(True):
                    targetLineNumber=random.randint(i,length-1)
            
                    flag=False

                    if(targetLineNumber in usedRows) or targetLineNumber==i:
                        flag=True

                    if(flag==False):
                        break

                buffer=row
                rowArray[i]=rowArray[targetLineNumber]
                rowArray[targetLineNumber]=buffer

                print(f'Строка № {i} заменена на строку № {targetLineNumber}')

                usedRows.append(targetLineNumber)

            i+=1

        print('Список перемешан')

def SplitSelection(rowArray, trainingSelectionArray, testSelectionArray, trainingSelectionPercent):
    length=len(rowArray)
    testSelectionSize=(length/100)*trainingSelectionPercent

    for i in range(length):
        if(i<=testSelectionSize-1):
            trainingSelectionArray.append(rowArray[i])
        else:
            testSelectionArray.append(rowArray[i])

    print(f'Выборка поделена на тренировочную и тестовую в соотношении {trainingSelectionPercent} : {100-trainingSelectionPercent}')

def KFoldSplit(rowArray, kFoldArray, k, testSelection):
    length=len(rowArray)
    restOfSelection=[]

    SplitSelection(rowArray, restOfSelection, testSelection, 88)

    CellSize=int(len(restOfSelection)/k)

    ColumnArray=[]
    CellArray=[]


    for i in range(k):
        for j in range(k):
            for l in range(CellSize):

                index=l+(CellSize*j)

                if(index<len(restOfSelection)):
                    CellArray.append(restOfSelection[index])
            ColumnArray.append(CellArray)
            CellArray=[]
        kFoldArray.append(ColumnArray)
        ColumnArray=[]


    print('Формирование K Fold выборки выполнено')

trainingSelectionArray7030=[]
testSelectionArray7030=[]

trainingSelectionArray8020=[]
testSelectionArray8020=[]

kFoldTestSelection=[]

trainingSelectionArrayKfold=[]
testSelectionArrayKfold=[]

with open("16.csv", "r") as readFile:
    rowArray=list(csv.reader(readFile, delimiter=";"))
    
    MixArray(rowArray)
    SplitSelection(rowArray, trainingSelectionArray7030, testSelectionArray7030,70)
    SplitSelection(rowArray, trainingSelectionArray8020, testSelectionArray8020,80)
    KFoldSplit(rowArray, trainingSelectionArrayKfold, 8, testSelectionArrayKfold)
   
    k=0
    l=0


    for row in trainingSelectionArrayKfold:
        for collumn in row:
                if k==l:
                    print(f'Ряд {k}, Столбец {l}, выборка(Валидационная):')
                else:
                    print(f'Ряд {k}, Столбец {l}, выборка:')
                for i in range(5):
                    print(collumn[i])
                print('...')
                print('')
                l+=1
        k+=1
        l=0

    input()