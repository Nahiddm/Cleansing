sampledata=open("D:\\TelU\\semester 3\\PRAKTIKUM STRUKDAT\SAMPLE DATA.txt","r")
text=sampledata.read()

print("Text sebelum cleansing : ",text)


s=str(text)

tandabaca=".,-"
Cleansing= ""
for x in text:
    if x not in tandabaca:
        Cleansing = Cleansing + x

print("Text sesudah cleansing : ",Cleansing)
