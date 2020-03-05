import os
import pandas as pd

countries = ["Afghanistan,Albania,Algeria,Andorra,Angola,Antigua,and,Barbuda,Argentina,Armenia,Australia,Austria,Azerbaijan,Bahamas,Bahrain,Bangladesh,Barbados,Belarus,Belgium,Belize,Benin,Bhutan,Bolivia,Bosnia,and,Herzegovina,Botswana,Brazil,Brunei,Bulgaria,Burkina,Faso,Burundi,Cabo,Verde,Cambodia,Cameroon,Canada,Central,African,Republic,(CAR),Chad,Chile,China,Colombia,Comoros,Congo,,Democratic,Republic,of,the,Congo,,Republic,of,the,Costa,Rica,Cote,d'Ivoire,Croatia,Cuba,Cyprus,Czechia,Denmark,Djibouti,Dominica,Dominican,Republic,Ecuador,Egypt,El,Salvador,Equatorial,Guinea,Eritrea,Estonia,Eswatini,(formerly,Swaziland),Ethiopia,Fiji,Finland,France,Gabon,Gambia,Georgia,Germany,Ghana,Greece,Grenada,Guatemala,Guinea,Guinea-Bissau,Guyana,Haiti,Honduras,Hungary,Iceland,India,Indonesia,Iran,Iraq,Ireland,Israel,Italy,Jamaica,Japan,Jordan,Kazakhstan,Kenya,Kiribati,Kosovo,Kuwait,Kyrgyzstan,Laos,Latvia,Lebanon,Lesotho,Liberia,Libya,Liechtenstein,Lithuania,Luxembourg,M,Madagascar,Malawi,Malaysia,Maldives,Mali,Malta,Marshall,Islands,Mauritania,Mauritius,Mexico,Micronesia,Moldova,Monaco,Mongolia,Montenegro,Morocco,Mozambique,Myanmar,(formerly,Burma),N,Namibia,Nauru,Nepal,Netherlands,New,Zealand,Nicaragua,Niger,Nigeria,North,Korea,North,Macedonia,(formerly,Macedonia),Norway,O,Oman,P,Pakistan,Palau,Palestine,Panama,Papua,New,Guinea,Paraguay,Peru,Philippines,Poland,Portugal,Q,Qatar,R,Romania,Russia,Rwanda,S,Saint,Kitts,and,Nevis,Saint,Lucia,Saint,Vincent,and,the,Grenadines,Samoa,San,Marino,Sao,Tome,and,Principe,Saudi,Arabia,Senegal,Serbia,Seychelles,Sierra,Leone,Singapore,Slovakia,Slovenia,Solomon,Islands,Somalia,South,Africa,South,Korea,South,Sudan,Spain,Sri,Lanka,Sudan,Suriname,Sweden,Switzerland,Syria,T,Taiwan,Tajikistan,Tanzania,Thailand,Timor-Leste,Togo,Tonga,Trinidad,and,Tobago,Tunisia,Turkey,Turkmenistan,Tuvalu,U,Uganda,Ukraine,United,Arab,Emirates,(UAE),United,Kingdom,(UK),United,States,of,America,(USA),Uruguay,Uzbekistan,V,Vanuatu,Vatican,City,(Holy,See),Venezuela,Vietnam,Y,Yemen,Z,Zambia,Zimbabwe"]
fileList = os.listdir('2Columns')

for filePath in fileList[0:10]:
    df = pd.read_csv('2Columns/'+filePath)
    xAxis = df.columns[0]
    #automate for: year(yyyy, yy, 'yy), quarters, months, countries, states
    if(xAxis == 'Unnamed: 0'):
        print(df.head())
        newXAxis = input('Replace with:')
        df.columns[0] = newXAxis
        df.to_csv(index=False, path_or_buf=filePath )

        # with open(file, 'rw') as filz:

