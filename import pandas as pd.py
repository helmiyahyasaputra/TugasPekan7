import pandas as pd
pizza = {'Nama' : ['Yuliah','Uci','Fifi','Niar','Agus','Yanuar'],'Tinggi Badan':[163, 164, 162, 161, 171, 178],'Berat Badan':[50, 65, 64, 48, 60, 70]}
pizza_df = pd.DataFrame(pizza)
pizza_df
print(pizza_df)